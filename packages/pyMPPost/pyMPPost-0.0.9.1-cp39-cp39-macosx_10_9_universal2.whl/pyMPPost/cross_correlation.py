# -*- coding: utf-8 -*-
"""
file: cross_correlation.py 
discription: 
"""
import logging
import numpy as np
import pandas as pd

def cross_correlation(PH_df, info):
    logging.info("Beginning Cross Correlation")
    PH_df["particle_label"] = PH_df.particle_type.map({1:"n",2:"g", 3:"g"})
    start_detectors = info["cross correlation"]["start_detectors"]
    
    for start_detect in start_detectors:
        logging.info(f"Computing Cross Correlation for start detector {start_detect}")
        start_detect_mask = PH_df["cell"].eq(start_detect).groupby("history").transform("any")
        oth_detect_mask = PH_df["cell"].ne(start_detect).groupby("history").transform("any")
        filtered_df = PH_df[start_detect_mask & oth_detect_mask]
        cell_mask = (filtered_df["cell"] == start_detect)
        start_df = filtered_df[cell_mask]
        oth_df = filtered_df[~cell_mask]
        computed1 = np.split(start_df[["time","particle_label"]].values, np.unique(start_df.index.values, return_index=True)[1][1:])
        computed2 = np.split(oth_df[["time","particle_label"]].values, np.unique(oth_df.index.values, return_index=True)[1][1:])
        
        time_data = [np.subtract.outer(oth[:,0],start[:,0]).flatten() for start, oth in zip(computed1,computed2)]
        label_data = [np.add.outer(start[:,1], (oth[:,1])).flatten() for start, oth in zip(computed1,computed2)]
        time_diff = np.concatenate(time_data)
        labels = np.concatenate(label_data)
        
        CC_df = pd.DataFrame({"time_diff":time_diff, "labels":labels})
        if info["cross correlation"]["all_cc"] == "tsv":
            CC_df.to_csv(f"{info['i/o']['output_root']}_detector_{start_detect}_All_CC", index=False, sep="\t")
            
        total, edges = np.histogram(a=CC_df["time_diff"], bins=info["cross correlation"]["hist_bins"])
        nn, __ = np.histogram(a=CC_df[CC_df.labels == "nn"]["time_diff"], bins=edges)
        gn, __ = np.histogram(a=CC_df[CC_df.labels == "gn"]["time_diff"], bins=edges)
        ng, __ = np.histogram(a=CC_df[CC_df.labels == "nn"]["time_diff"], bins=edges)
        gg, __ = np.histogram(a=CC_df[CC_df.labels == "gg"]["time_diff"], bins=edges)
        np.savetxt(fname=f"{info['i/o']['output_root']}_detector_{start_detect}_CC_Hist", X=np.column_stack((edges[:-1],total, nn, gn, ng, gg)))
        
    logging.info("Cross Correlation Complete")