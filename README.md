Downloads h5 cross sections and writes out each nuclide to a JSON file

```
mkdir nuclear_data && wget https://anl.box.com/shared/static/uhbxlrx7hvxqw27psymfbhi7bx7s6u6a.xz -O nuclear_data/endf.tar.xz && tar -xvJf nuclear_data/endf.tar.xz -C nuclear_data

pip install openmc_data_to_json

python convert_json.py
```