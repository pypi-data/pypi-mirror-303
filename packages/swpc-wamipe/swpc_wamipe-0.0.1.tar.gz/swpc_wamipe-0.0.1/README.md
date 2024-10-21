# Project Overview
This software package is a collaboration between the [National Oceanic and Atmospheric Administration Space Weather Prediction Center (NOAA SWPC)](https://www.swpc.noaa.gov/)
and [App Dev Club LLC](https://appdevclub.com) at the University of Maryland. Using [outputs](https://noaa-nws-wam-ipe-pds.s3.amazonaws.com/index.html) from the Whole Atmosphere Model-Ionosphere Plasmasphere Electrodynamics (WAM-IPE) model, it allows users to input date, time, and satellite location (longitude + latitude) and output the neutral density value near the satellite at that date and time. 

# Prerequisites
Installation of latest package versions of netCDF4, numpy, scipy, and requests. 

# Usage
To install the package, open the terminal of a code editor and run the following command. <br>
 **Update this command after each package version change to keep documentation up to date.**
```
pip install swpc-wamipe
```

To print a density value run the following code:
```
from wam_api import WAMInterpolator
foo = WAMInterpolator() 
dt = foo.datetime(2024, 5, 11, 18, 12, 22)
lat, lon, alt = -33.4, -153.24, 550.68  # degrees north, degrees east, km
my_density = foo.get_density(dt, lat, lon, alt)
print(my_density)
```

# Updating the package version

To update the package version on PyPI from local with any changes you have made to the project, 
first change the version number
in ```pyproject.toml```. 

Next, 
run the following commands in order:
```
pip install -e .
```
``` 
pip install --upgrade build  
```
```
python -m build 
```
```
pip install --upgrade twine
```
```
python -m twine upload --repository testpypi dist/*
```

A new version of the package will be created in PyPI.
To make sure you have the latest package version installed in local run the following command:
```
pip install wam_api --upgrade
```