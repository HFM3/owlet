# OWLET

A Geospatial Python Package for Field Researchers

## Owlet is Currently Under Development

### ROADMAP

- **Register project** -- ![shield](https://img.shields.io/badge/Owlet-V0.0.1-blue?style=flat)
- **Develop EGF (Exact Geometry Format) file standard** -- ![shield](https://img.shields.io/badge/Developed-brightgreen)
- Add EGF reader to Owlet -- ![shield](https://img.shields.io/badge/-In%20Development-orange)
- Internal geometry standard - GCA (Geometry, Coordinates, Attributes) -- ![shield](https://img.shields.io/badge/-In%20Development-orange)
- Basic file manipulation -- ![shield](https://img.shields.io/badge/-Upcoming-lightgrey)
- GeoJSON export -- ![shield](https://img.shields.io/badge/-Upcoming-lightgrey)
- CSV compatability -- ![shield](https://img.shields.io/badge/-Upcoming-lightgrey)
- Google Earth (KML) export -- ![shield](https://img.shields.io/badge/-Upcoming-lightgrey)
- Geospatial functions (Distance, Area, Convex Hull, etc) -- ![shield](https://img.shields.io/badge/-Upcoming-lightgrey)


## Owlet and EGF

### Developed for Field Researchers
Owlet is a Python library for interacting with EGF files and mapping them.

EGF a is file structure that allows geo-data to be easily recorded without traditional GIS software. An EGF file contains all of the necessary components required to define geospatial features— without overcomplicating it.

## EGF File Example

### Overview
An EGF file is comprised of three sections:

1. **Feature Type Declaration** (point, line, polygon)
2. **Attribute Headers**
3. **Features**: attributes & vertices *(coordinate sets)*

*In an EGF file, each section is separated by three blank lines and the file ends with a single blank line.*


##### Example of a point recorded in EGF
```
PT



Park Name, City, Pond, Fountain



Post office Square, Boston, FALSE, TRUE
-71.055631, 42.356243, 2


```

##### EGF Structure - Commented Example
```
PT  # Geometry type (PT = point)
# (blank line 1)
# (blank line 2)
# (blank line 3)
Park Name, City, Pond, Fountain  # File attribute headers
# (blank line 1)
# (blank line 2)
# (blank line 3)
Post Office Square, Boston, FALSE, TRUE  # First feature's attributes
-71.055631, 42.356243, 2  # First feature's coordinates (x, y, z)
# (blank line 1)
# (blank line 2)
# (blank line 3)
Boston Common, Boston, TRUE, TRUE  # Second feature's attributes
-71.066412,  42.355465, 10  # Second feature's coordinates (x, y, z)
# end file with blank line
```


[Full EGF Documentation](https://github.com/HFM3/owlet/blob/master/docs/egf.md)


## Owlet License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
