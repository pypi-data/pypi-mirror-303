# pyMPPost
[![Static Badge](https://img.shields.io/badge/Dveloped%20by-DNNG_%40_umich-blue)](https://dnng.engin.umich.edu)
[![PyPI - Version](https://img.shields.io/pypi/v/pyMPPost)](https://pypi.org/project/pyMPPost)
[![PyPI - License](https://img.shields.io/pypi/l/pyMPPost)](#License)

pyMPPost is a python based post processor for [MCNPX-PoliMi](https://rsicc.ornl.gov) which converts particle transport interactions for detector volumes into proper detector responses. 

## Table of Contents
1.   [Features](#features)
2.   [Installation](#installation)
3.   [Usage](#Usage)
4.   [License](#License)
5.   [Acknowledgements](#Acknowledgements)
6.   [Contact](#Contact)

## Features
### Pulse Height Module
The Pulse Height Module calculates pulse metrics and generates the pulse shape response for a detector based on the input data and specifications. The post process results can be used to generate scatter plots measuring the relationship between pulse height and counts/second.

The ouput of the Pulse Height Module consists of 3 files:
- All Pulses File: Contains all post process pulse calculation results
- Log File: Details timestamps of Pulse Height subprocesses
- Post Process Summary: Presents analysis and logistics of Pulse Height calculations
### Cross Correlation Module
The Cross Correlation Module time differences between events in different detectors within the simulation. The "start detector" can be designated by the user. Final time differences are plotted on a histogram. Time differences may be used in further data processing for the determination of certain metrics like neutron energy, system time offsets, detector positioning, etc.

The ouput of the Cross Correlation Module consists of 2 files:
- Cross Correlation History File: Contains absolute count of NN, GN, and GG occurences
- All Time Difference File: Details all time differences between pulses
## Installation
Using python >= 3.9.0
```bash
$ pip install pyMPPost
```

## Usage 
To run pyMPPost properly, you must have 3 key files
- [Input File](#input-file) 
- [Material Card](#Material-Card)
- [Stopping Power Table](#Stopping-Power-Table)

### Input File
The input file specifies the modules to run and the values of the parameters relevant to pyMPPost calculations. It contains the path to the file of the material card. It is in `.toml` format, which allows users to comment relevant information and context regarding the parameters used. Here is an example of the <a id="raw-url" href="https://gitlab.eecs.umich.edu/umich-dnng/pymppost/-/raw/build/input_files/example_input.toml?ref_type=heads&inline=false" >Input File</a>

### Material Card
The material card specifies the constants relevant to the detectors used in the POLIMI simulation. This includes the path to the stopping power table file. Like the input file, the material card is in `.toml` format to allow users to add comments and annotations. Here is an example of the <a id="raw-url" href="https://gitlab.eecs.umich.edu/umich-dnng/pymppost/-/raw/build/input_files/blank_organic_card.toml?ref_type=heads&inline=false" >Material Card</a>

### Stopping Power Table
Stopping power tables contain the stop power constants of the detector materials. They are `.txt` files. Here is an example of the <a id="raw-url" href="https://gitlab.eecs.umich.edu/umich-dnng/pymppost/-/raw/build/stopping_power_tables/ogs_dEdx.txt?ref_type=heads&inline=false" >Stopping Power Table</a>

### Example


```bash
$ pyMPPost example_input.toml
```

## License
Released under the <a id="raw-url" href="https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt" >MIT License</a>


## Acknowledgements


## Contact
John Cashy: jtcashy@umich.edu

Ricardo Lopez: rlopezle@umich.edu