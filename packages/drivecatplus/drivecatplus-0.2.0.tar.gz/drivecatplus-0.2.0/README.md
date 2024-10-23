# DriveCAT+ - Drive Cycle Analysis Tool Plus

DriveCAT+ is a drivecycle analysis python package that takes in vehicle time, speed, and elevation profiles, processes them, and outputs several useful statistical metrics that help quantify a drivecycle.

## Overview
DriveCAT+ contains a class `Cycle` used for taking a drivecycle as an input. The `DriveStats` class initializes various categories of drivestats like `DistanceStats`, `TotalSpeedStats`, `TimeStats`, etc as subclasses and facilitates the calculation of relevant statical metrics within their constructor methods.

## Installation

First, clone the repository from GitHub:

    git clone https://github.com/NREL/drivecatplus.git drivecatplus

DriveCAT+ depends on python versions >=3.8 and <=3.11. One way to satisfy this is to use conda:

    conda create -n dcp python=3.10
    conda activate dcp

After creating the environment, navigate to the parent directory containing the DriveCAT+ repository e.g. `cd github/drivecatplus/` and run:

    pip install -e .

from within the dcp python 3.10 environment you created.

This will install DriveCAT+ with minimal dependencies such that the code files can be edited. Developers will find the `-e` option handy since DriveCAT+ will be installed in place from the installation location, and any updates will be propagated each time DriveCAT+ is freshly imported.

## Demo

This repo is provided with a sample [drivecycle input file](https://github.com/NREL/drivecatplus/blob/4b69af23fbf9099293ebd1e37b9785eab1d9e460/src/resources/demo_cycle_without_elevation.csv) to test out in a basic demo. From the parent directory:

```bash
cd src/demos/
python demo_drivestats_basic.py
```

or, use VS Code's Interactive Window to run the demo code blocks.

## Run DriveCAT+ for multiple drivecycles

The run_dcp.py module can be used to analyze multiple drivecycles and export the results as a single CSV. --input-path accepts path of a single CSV file input or the path to a directory. When a directory path is provided, the module searches all subdirectories for .CSV files and runs DriveCAT+ for each of them.

```bash
cd src/drivecatplus/
python run_dcp.py --input-path=/path/to/file-or-folder
```
