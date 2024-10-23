#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
file: pulse_height.py 
discription: 
"""
import os
import argparse
import datetime
import time
import logging
import dask.dataframe as dd
from dask.distributed import LocalCluster
import pandas as pd
import numpy as np
import toml

from .pulse_height import pulse_height
from .cross_correlation import cross_correlation

def main():
    parser = argparse.ArgumentParser(
                    prog='pyMPPost',
                    description='What the program does',
                    epilog='Text at the bottom of help')
    
    parser.add_argument('input_file')
    args = parser.parse_args()
    
    with open(args.input_file) as toml_file:
        input_toml = toml.load(toml_file) #Loads toml file into a python dict
    input_toml["input_file"] = args.input_file

    logging.basicConfig(filename=f"{input_toml['i/o']['output_root']}.log", filemode='w+', 
                        format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', 
                        level=logging.DEBUG)
    
    
    dask_cluster = LocalCluster(silence_logs=logging.ERROR)
    
    _mppost_start(input_toml, dask_cluster.get_client())
    

def _mppost_start(info, client):
    # Save Start time
    run_start_time = time.time()
    logging.info("Beginning pyMPPost run...")
      
    detect_map, cell_to_mats = _detector_data(info)
    ### Read in Polimi Data to pyMPPost Object ###
    
    plm_ddf = _read_polimi(info, detect_map, cell_to_mats, client) 
    
    ### Run MPPost Modules ###
    results = {}
    
    # Check if Pulse Height Module On
    if info["pulse height"]["module_on"]:
        PH_df, results["pulse height"] = pulse_height(plm_ddf, info, client)
        
    if info["cross correlation"]["module_on"]:
        cross_correlation(PH_df, info)
    
    _gen_summary(plm_ddf, info, client, results, run_start_time)
    
def _detector_data(info):
    cell_to_mats = {}
    detect_map = {}
    
    for (material, cells) in zip(info["detectors"]["detector_mats"],info["detectors"]["detector_cells"]):
            cell_to_mats[cells[0]] = material
            if len(cells) > 1:
                for cell in cells[1:]:
                    detect_map[cell] = cells[0]
                
    mats = []
    for mat_path in info["detectors"]["material_list"]:
        with open(mat_path) as mat_toml_file:
            mat = toml.load(mat_toml_file)
        mats.append(mat)
    info["mats"] = mats
    
    for mat in mats:
        if mat["mat_type"] == 1:
            mat_birks = mat["calibration"].pop("birks")
            with open(mat_birks["stopping_power"]) as dEdx_file:
                lines = dEdx_file.readlines()
                length = len(lines)
                energy = np.zeros((length,))
                dEdx = np.zeros((length,))
                intergrand = np.zeros((length,))
                for i, line in enumerate(lines):
                    line = line.split()
                    energy[i] = float(line[0])
                    # For stilbene files, only the first and the 3rd line are read in
                    if (os.path.basename(mat_birks["stopping_power"]) == "stilbene_dEdx.txt"):
                        dEdx[i] = float(line[2])
                    else:
                        dEdx[i] = float(line[1])
            energy = np.insert(energy, 0, values=0.0)
            dEdx = np.insert(dEdx, 0, values=0.0)
            intergrand = mat_birks["S"]/(1 + mat_birks["kB"]*dEdx)
            length = len(intergrand)
            birks_light = np.zeros((length,))
            for i in range (length):
                birks_light[i] = np.trapz(y=intergrand[0:i+1], x=energy[0:i+1]) 
            mat["calibration"]["birks_energy"] = energy
            mat["calibration"]["birks_light"] = birks_light
          
    detectors = {}
    for cell in cell_to_mats:
       detectors[cell] = mats[cell_to_mats[cell]]
    return detect_map, cell_to_mats
        
def _read_polimi(info, detect_map, cells_to_mats, client):
    """
    Stores Polimi Data into a Dask Dataframe (plm_ddf) with index on history.
    
    Dataframe Info
        Index: history (int) 
        
        Columns:
            particle_num (int), particle_type (int), interaction_type (int), target_nucleus (int), cell (int), energy_deposited (float), time (float), 
            x-pos (float), y-pos (float), z-pos (float), weight (float), generation_num (int), num_scatters (int), code (int), prior_energy (float) 
    """ 
    
    logging.info(f"Reading in MCNP-Polimi file: {info['i/o']['polimi_det_in']}")
    polimi_collision_file_dtypes = {
        "history":int, 
        "particle_num":int, 
        "particle_type":int,
        "interaction_type":int, 
        "target_nucleus":int, 
        "cell":int, 
        "energy_deposited":float, 
        "time":float, 
        "x-pos":float, 
        "y-pos":float, 
        "z-pos":float, 
        "weight":float, 
        "generation_num":int,
        "num_scatters":int, 
        "code":int, 
        "prior_energy":float
    }
    plm_ddf = dd.read_csv(f"{info['i/o']['polimi_det_in']}", header=None, skipinitialspace=True, sep="\s+",  
                            names=["history", "particle_num", "particle_type","interaction_type", "target_nucleus", "cell", 
                                    "energy_deposited", "time", "x-pos", "y-pos", "z-pos", "weight", "generation_num",
                                    "num_scatters", "code", "prior_energy"], dtype=polimi_collision_file_dtypes).set_index("history", sorted=True)
    if detect_map:
        plm_ddf["cell"] = plm_ddf["cell"].replace(detect_map)
    
    plm_ddf["mat_num"] = plm_ddf["cell"].replace(cells_to_mats)
    
    meta = plm_ddf._meta
    plm_ddf = plm_ddf.map_partitions(lambda df: df.sort_values(by=["history", "cell", "time"]), meta=meta)
    
    return client.persist(plm_ddf)

def _gen_summary(plm_ddf, info, client, results, start_time):
    # Open Summary File
    sum_of = open(f"{info['i/o']['output_root']}.txt", mode="w")
    sum_of.write("Post Processor Output File Summary\n")
    
    date_and_time = datetime.datetime.now()
    sum_of.write(f"Title: {info['title']}\n")      
    sum_of.write(f"Input File: {info['input_file']}\n")  
    sum_of.write(f"User: {info['username']}\n")      
    sum_of.write(f"Processed: {date_and_time}\n\n")  
    
    sum_of.write("MCNP-PoliMi File Characteristics\n")
    sum_of.write("--------------------------------\n")
    sum_of.write(f"Number of lines: {len(plm_ddf)}\n")
    sum_of.write(f"Number of histories: {client.compute(plm_ddf.index.nunique()).result()}\n\n")   
    
    # Check if Pulse Height Module On
    if info["pulse height"]["module_on"]:
        # Write Pulse Height Info to Summary File
        (total_num_pulses, neutron_num_pulses) = results["pulse height"]
        sum_of.write(f"Pulse Height Analysis\n")
        sum_of.write(f"---------------------\n")
        sum_of.write(f"Total number of pulses above threshold: {total_num_pulses}\n")
        sum_of.write(f"Total number of neutron pulses above threshold: {neutron_num_pulses}\n")   
        sum_of.write(f"Total number of photon pulses above threshold: {total_num_pulses - neutron_num_pulses}\n\n")
        
    sum_of.write(f"Runtime\n")    
    sum_of.write(f"-------\n")  
    sum_of.write(f"This run took {time.time() - start_time} seconds")
    sum_of.close()
    
    
if __name__ == "__main__":
    main()