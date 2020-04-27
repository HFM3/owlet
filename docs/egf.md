# EGF - Exact Geometry Format

## About

Designed for field researchers, EGF a is file structure that allows geo-data to be easily recorded without traditional GIS software.

An EGF file contains all of the necessary components required to define geospatial features without over-complicating it.

## EGF Structure

### Overview
An EGF file is comprised of three sections:

1. Feature type declaration (point, line, polygon)
2. Attribute headers
3. Features: attributes & vertices *(coordinate sets)*

*In an EGF file, each section is separated by three blank lines and the file ends with a single blank line.*


##### Example EGF File *(Point EGF)*
```console
PT



Park Name, City, Pond, Fountain



Post office Square, Boston, FALSE, TRUE
-71.055631, 42.356243, 2


```

##### EGF Structure - Commented Example
```python
PT  # Geometry type (PT = point)
# (blank line 1)
# (blank line 2)
# (blank line 3)
Park Name, City, Pond, Fountain  # File attribute headers
# (blank line 1)
# (blank line 2)
# (blank line 3)
Post office Square, Boston, FALSE, TRUE  # First feature's attributes
-71.055631, 42.356243, 2  # First feature's coordinates (x, y, z)
# (blank line 1)
# (blank line 2)
# (blank line 3)
Boston Common, Boston, TRUE, TRUE  # Second feature's attributes
-71.066412,  42.355465, 10  # Second feature's coordinates (x, y, z)
# end file with blank line
```



### Structure

#### 1. Feature Type Declaration
An EGF file can be declared as either a **POINT**, **LINE**, or **POLYGON** file. The feature type declaration goes on the first line of the file and each feature within the EGF file must match the declared type.

The table below lists the valid EGF type declarations that can go on the first line of an EGF file:

FEATURE TYPE | EGF DECLARATION
-- | --
POINT | PT
LINE STRING | LS
POLYGON | POLY



#### 2. Attribute Headers
Attribute headers are the "titles" to the attributes of every feature within the EGF file.

Consider an EGF file that marks several parks within a city. The headers could be:
- **Park Name**: name of park
- **City**: City that the park is in
- **Pond**: Does the park have a pond?
- **Fountain**: Does the park have a fountain?

How would that look as a table? Attribute Headers are equivalent to the first row of a table.

Park Name | City | Pond | Fountain
-- | -- | -- | --
Fan Pier Park | Boston | FALSE | FALSE
Post Office Square | Boston | FALSE | TRUE
Boston Common | Boston | TRUE | TRUE



#### 3. Features (Attributes & Vertices)
Together, attributes and vertices define a geo-feature.


##### Attributes
Attributes describe the feature in accordance with the headers.

Using the city parks example from the Attribute Headers section, the attributes for Post Office Square would be:
- **Post Office Square** *(park name)*
- **Boston** *(city)*
- **FALSE** *(pond)*
- **TRUE** *(fountain)*


##### Vertices
Vertices are the coordinate sets that define the location, path, or shape of a feature.

Coordinate sets and are defined in **X, Y, Z** *(Longitude, Latitude, Elevation)* order and are recorded as Decimal Degrees.

The coordinate set for Post Office Square (EGF Point) would be:

X (LAT) | Y (LNG) | Z (ELV)
-- | -- | --
-71.055631 | 42.356243 | 2

*In this example, elevation is ground height above mean sea level.*

### Bringing it Together

To record Post Office Square as an EGF file, we need to bring the following together:
1. **Geometry Type** *(Point)*
2. **Headers** *(Park Name, City, Pond, Fountain)*
3. **Geo-Feature** *(Attributes & Vertices)*
    - **Attributes** *(Post office Square, Boston, FALSE, TRUE)*
    - **Vertex** *(-71.055631, 42.356243, 2)*

Remember to separate each section/feature by 3 blank lines and to end the file with a single blank line.


##### PostOfficeSquare.egf

```console
PT



Park Name, City, Pond, Fountain



Post office Square, Boston, FALSE, TRUE
-71.055631, 42.356243, 2


```

## Further Reading
[EGF Geometry Specifications (Point, Line, Polygon)](egf_geometry.md)

[Tutorial](egf_file_tut.md)
