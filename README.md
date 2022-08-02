# FML-splitter
A simple Python script for splitting an existing FML file into a file per floor.
This script can be used in case a different program would only process the first floor in a file.

## Usage
```cmd
$ splitfml.py -h

usage: splitfml.py [-h] INPUT [OUTPUT]

Split FML file into separate floor

positional arguments:
  INPUT       Input .fml file
  OUTPUT      Output .fml file format (default: INPUT_#.fml)

optional arguments:
  -h, --help  show this help message and exit
```
