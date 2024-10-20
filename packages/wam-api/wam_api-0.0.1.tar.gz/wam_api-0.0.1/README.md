# Usage
The purpose of this README is to show the user how to install the WAM_Interpolate pip package <br>
and how to get the interpolated density at the given datetime, latitude, longitude, and altitude.

```
#from a high level, we want this all put into a pip-installable package with a call sequence like the following:
from wam_api import WAMInterpolator
foo = WAMInterpolator() # <-- as a class/object
dt = datetime(2024, 5, 11, 18, 12, 22)
lat, lon, alt = -33.4, -153.24, 550.68  # degrees north, degrees east, km
my_density = foo.get_density(dt, lat, lon, alt)
```
