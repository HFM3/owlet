<div align="center">
  <img src="https://raw.githubusercontent.com/HFM3/owlet/master/images/owlet_horiz.png" width="60%"><br>
</div>

---
![PyPI](https://img.shields.io/pypi/v/owlet?label=PyPi)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/owlet?label=Python)
![PyPI - License](https://img.shields.io/pypi/l/owlet?label=License)

# A Geospatial Python Package for Field Researchers

## Owlet and EGF: Developed for Field Researchers
Owlet is a Python library for interacting with and mapping EGF files.

EGF, or Exact Geometry Format, is a file structure designed specifically for recording geo-data without traditional GIS software. An EGF file contains all of the necessary components required to define geospatial features— without overcomplicating it.

## EGF File Example

### Overview
An EGF file is comprised of three sections:

1. **A Feature Type Declaration** (point, line, polygon)
2. **Attribute Headers**
3. **Features**: attributes & coordinate sets


#### Example EFG file of two placemarks:
```
PT



Park Name, City, Pond, Fountain



Post office Square, Boston, FALSE, TRUE
42.356243, -71.055631, 2



Boston Common, Boston, TRUE, TRUE
42.355465, -71.066412, 10

```

*In an EGF file, each section / feature is separated by three blank lines and the file ends with a single blank line.*

*An EGF file is a '.txt' file renamed to '.egf'*

[Full EGF Documentation](https://github.com/HFM3/owlet/blob/master/docs/egf.md)



## How to Use Owlet


### Install

###### Windows
```python
>>> py -m pip install  owlet
```
###### MacOS / Linux
```python
>>> python3 pip install owlet
```
<!---
##### Install specific version
```shell
pip install owlet==0.0.1
```

##### Upgrade to latest version
```shell
pip install --upgrade owlet
```
-->

### Reading an EGF file
```python
import owlet

file_path = r"path/to/file/PostOfficeSquare.egf"

my_shape = owlet.egf_read(file_path)

```

### Converting EGF file to Other Formats

###### CSV
```python
csv = my_shape.table()
```

###### GeoJSON
```python
json = my_shape.geo_json()
```
<!--
###### GCA
```python
gca = my_shape.gca_str()
```
-->

###### EGF
```python
egf = my_shape.egf()
```



## Owlet in Use
### Owlet Code Snippets

#### Visualizing an EGF
```Python
import owlet

# File path of EGF file
file_path = r"path/to/file/PostOfficeSquare.egf"

# Loading EGF into Owlet
my_shape = owlet.egf_read(file_path)

# Opening a preview with http://geojson.io
my_shape.geo_json(visualize=True)

```

#### Writing a GeoJSON file for use with GIS software
```Python
import owlet

# File path of EGF file
file_path = r"path/to/file/PostOfficeSquare.egf"

# Loading EGF into Owlet
my_shape = owlet.egf_read(file_path)

# Saving GeoJSON to a variable
json = my_shape.geo_json()

# Full path of file to create- including file extension ".json"
json_path = r"path/to/file/PostOfficeSquare.json"

# Writing GeoJSON to file
owlet.text_writer(json_path, json)
```


#### Converting EGF file to CSV for external filtering / manipulation

```Python
import owlet

# File path of EGF file
file_path = r"path/to/file/PostOfficeSquare.egf"

# Loading EGF into Owlet
my_shape = owlet.egf_read(file_path)

# Converting EGF into a table that can be wrtten to a '.csv' file
csv_data = myshape.table()

# Full path of file to create- including file extension ".csv"
csv_path = r"path/to/file/PostOfficeSquare.csv"

# Writing table to file
owlet.write_csv(csv_path, csv_data)

```


#### Loading CSV back into Owlet
```Python
# Full path of file to read
csv_path = r"path/to/file/PostOfficeSquare.csv"

geom_type = 'PT'  # Tells Owlet what type of feature to expect when reading csv

# Loading csv into Owlet
owlet.from_csv(geom_type, csv_path)

```

<!---
## Owlet is Currently Under Development

### ROADMAP

- **Register Project** -- ![shield](https://img.shields.io/badge/Owlet-v0.0.1-blue)
- **Develop EGF (Exact Geometry Format) file standard** -- ![shield](https://img.shields.io/badge/Owlet-v0.0.0-blue)
- **Add EGF Reader to Owlet** -- ![shield](https://img.shields.io/badge/Owlet-v0.0.0-blue)
- **Internal Geometry Standard** - GCA (Geometry, Coordinates, Attributes) -- ![shield](https://img.shields.io/badge/Owlet-v0.0.0-blue)
- **GeoJSON Export** -- ![shield](https://img.shields.io/badge/Owlet-v0.0.0-blue)
- **CSV Compatibility** -- ![shield](https://img.shields.io/badge/Owlet-v0.0.0-blue)
- **Basic GCA Manipulation** -- ![shield](https://img.shields.io/badge/-In%20Development-orange)
-->

&nbsp;
&nbsp;

Owlet License: [GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
