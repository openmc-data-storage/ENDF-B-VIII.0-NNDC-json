

This repository holds a collection of nuclear data in JSON format.

Each file within the json_files folder contains an probability for a specific reaction and nuclide. The reaction numbers are encoded using ENDF MT numbers which can be looked up using code like [this](https://github.com/openmc-dev/openmc/blob/57816e6b8cf23ed0e9b020b72752ed6aeb9501dd/openmc/data/reaction.py#L28-L70) here or found manually in a table like [this](https://www.oecd-nea.org/dbdata/data/manual-endf/endf102_MT.pdf) 


To reproduce the dataset

Download the nuclear data in h5 format 
```
mkdir nuclear_data && wget https://anl.box.com/shared/static/uhbxlrx7hvxqw27psymfbhi7bx7s6u6a.xz -O nuclear_data/endf.tar.xz && tar -xvJf nuclear_data/endf.tar.xz -C nuclear_data
```

Install a program that extracts cross sections from the h5 files
```
pip install openmc_data_to_json
```
Run the script in the repo
```
python convert_json.py
```