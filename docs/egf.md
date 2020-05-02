# EGF - Exact Geometry Format

## About

Designed for field researchers, is a file structure created specifically for recording geo-data without traditional GIS software.

An EGF file contains all of the necessary components required to define geospatial features— without overcomplicating it.

## EGF Structure

### Overview
An EGF file is comprised of three sections:

1. **A Feature Type Declaration** (point, line, polygon)
2. **Attribute Headers**
3. **Features**: attributes & coordinate sets

*In an EGF file, each section is separated by three blank lines and the file ends with a single blank line.*


##### Example EGF File *(Point EGF)*
```
PT



Park Name, City, Pond, Fountain



Post office Square, Boston, FALSE, TRUE
42.356243, -71.055631, 2



Boston Common, Boston, TRUE, TRUE
42.355465, -71.066412, 10

```

##### EGF Structure - Commented Example
```
PT  # Geometry type (PT = point)
# (blank line 1)
# (blank line 2)
# (blank line 3)
Park Name, City, Pond, Fountain  # File's attribute headers
# (blank line 1)
# (blank line 2)
# (blank line 3)
Post Office Square, Boston, FALSE, TRUE  # Attributes of first point feature
42.356243, -71.055631, 2  # First points's coordinates (y, x, z)
# (blank line 1)
# (blank line 2)
# (blank line 3)
Boston Common, Boston, TRUE, TRUE  # Second feature's attributes
42.355465, -71.066412, 10  # Second feature's coordinates (y, x, z)
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

Coordinate sets and are defined in **Y, X, Z** *(Latitude, Longitude, Elevation)* order and are recorded as Decimal Degrees.

The coordinate set for Post Office Square (EGF Point) would be:

Y (LNG) | X (LAT) | Z (ELV)
-- | -- | --
42.356243 | -71.055631 | 2

*In this example, elevation is ground height above mean sea level.*

### Bringing it Together

To record Post Office Square as an EGF file, we need to bring the following together:
1. **Geometry Type** *(Point)*
2. **Headers** *(Park Name, City, Pond, Fountain)*
3. **Geo-Feature** *(Attributes & Vertices)*
  - **Attributes** *(Post office Square, Boston, FALSE, TRUE)*
  - **Vertex** *(42.356243, -71.055631, 2)*

**Remember**:
- Separate each section and each feature by 3 blank lines
- End the file with a single blank line


#### PostOfficeSquare.egf
*Type or paste the following into a text editor:*
```
PT



Park Name, City, Pond, Fountain



Post Office Square, Boston, FALSE, TRUE
42.356243, -71.055631, 2

```
#### Saving an EGF file
When saving an EGF file from a text editor, replace '.txt' with '.egf'





# EGF Geometry Specifications

## POINT

### Defining a Point Feature
A point feature is the pairing of one attribute row and one set of coordinate (y, x, z).

###### Example Point Feature:
```
Post office Square, Boston, FALSE, TRUE  # Attributes
42.356243, -71.055631, 2  # Coordinate set
```

###### Example Point EGF File
```
PT



Park Name, City, Pond, Fountain



Post office Square, Boston, FALSE, TRUE
42.356243, -71.055631, 2

```

###### EGF Points File - Commented Example
```
PT  # Geometry type (PT = point)
# (blank line 1)
# (blank line 2)
# (blank line 3)
Park Name, City, Pond, Fountain  # File's attribute headers
# (blank line 1)
# (blank line 2)
# (blank line 3)
Post Office Square, Boston, FALSE, TRUE  # Attributes of first point feature
42.356243, -71.055631, 2  # First points's coordinates (y, x, z)
# (blank line 1)
# (blank line 2)
# (blank line 3)
Boston Common, Boston, TRUE, TRUE  # Second feature's attributes
42.355465, -71.066412, 10  # Second feature's coordinates (y, x, z)
# end file with blank line
```



## LINE STRING
### Defining a Line String Feature
A line string feature is the pairing of one attribute row and multiple ordered sets of coordinates (y, x, z).

*PT1 --> PT2 --> PT3 --> PT4 --> PT5*

A minimum of two coordinate sets are required to define a line string.

###### Example Line String Feature:
```
Post Office Square, A walk by the fountain
42.356716, -71.055685, 0
42.356587, -71.055769, 0
42.356566, -71.055754, 0
42.356539, -71.055746, 0
42.356511, -71.055757, 0
42.356495, -71.055790, 0
42.356485, -71.055830, 0
42.356389, -71.055842, 0
42.356252, -71.055796, 0
42.356046, -71.055642, 0
42.355876, -71.055697, 0
42.355828, -71.055758, 0
```

###### Example Line String EGF File
```
LS



Park Name, Feature Description



Post Office Square, A walk by the fountain
42.356716, -71.055685, 0
42.356587, -71.055769, 0
42.356566, -71.055754, 0
42.356539, -71.055746, 0
42.356511, -71.055757, 0
42.356495, -71.055790, 0
42.356485, -71.055830, 0
42.356389, -71.055842, 0
42.356252, -71.055796, 0
42.356046, -71.055642, 0
42.355876, -71.055697, 0
42.355828, -71.055758, 0

```

###### EGF Line String File - Commented Example
```
LS  # Geometry type (LS = Line String)
# (blank line 1)
# (blank line 2)
# (blank line 3)
Park Name, Feature Description   # File's attribute headers
# (blank line 1)
# (blank line 2)
# (blank line 3)
Post Office Square, A walk by the fountain  # Attributes of first line feature
42.356716, -71.055685, 0  # Line's 1st coordinate set (y, x, z)
42.356587, -71.055769, 0  # Line's 2nd coordinate set (y, x, z)
42.356566, -71.055754, 0  # Line's 3rd coordinate set (y, x, z)
42.356539, -71.055746, 0  # Line's 4th coordinate set (y, x, z)
42.356511, -71.055757, 0  # Line's 5th coordinate set (y, x, z)
42.356495, -71.055790, 0  # Line's 6th coordinate set (y, x, z)
42.356485, -71.055830, 0  # Line's 7th coordinate set (y, x, z)
42.356389, -71.055842, 0  # Line's 8th coordinate set (y, x, z)
42.356252, -71.055796, 0  # Line's 9th coordinate set (y, x, z)
42.356046, -71.055642, 0  # Line's 10th coordinate set (y, x, z)
42.355876, -71.055697, 0  # Line's 11th coordinate set (y, x, z)
42.355828, -71.055758, 0  # Line's 12th coordinate set (y, x, z)
# end file with blank line
```



## Polygon
### Defining a Polygon Feature
A Polygon feature is the pairing of one attribute row, one outer ring, and any number of optional inner rings.

**Outer Ring**: The shape of a polygon

**Inner Ring**: A hole in the polygon

Each polygon can only have a single outer ring, but can have any number of inner rings defined.

**Polygon Structure**
- POLYGON
  - OUTER RING
  - INNER RING 1
  - INNER RING 2

Each ring of a polygon is composed of multiple ordered coordinate sets (y, x, z) exactly like a line string feature. A minimum of three coordinate sets are required to define a polygon ring. Rings are separated from each other by a single blank line. Any block of coordinates after the first block (outer ring), is considered to be an inner ring.

###### Example Polygon Feature (No Holes):
```
Post Office Square, Boundary of Post Office Square
42.356856, -71.055757, 0
42.356080, -71.054976, 0
42.355697, -71.055636, 0
42.356003, -71.055941, 0
42.356767, -71.056220, 0
```

###### Example Polygon Feature (1 Hole):
```
Post Office Square, Boundary of Post Office Square
42.356856, -71.055757, 0
42.356080, -71.054976, 0
42.355697, -71.055636, 0
42.356003, -71.055941, 0
42.356767, -71.056220, 0

42.355955, -71.055522, 0
42.355894, -71.055458, 0
42.355846, -71.055546, 0
42.355908, -71.055615, 0
```

###### Example Polygon Feature (2 Holes):
```
Post Office Square, Boundary of Post Office Square
42.356856, -71.055757, 0
42.356080, -71.054976, 0
42.355697, -71.055636, 0
42.356003, -71.055941, 0
42.356767, -71.056220, 0

42.355955, -71.055522, 0
42.355894, -71.055458, 0
42.355846, -71.055546, 0
42.355908, -71.055615, 0

42.356089, -71.055312, 0
42.356005, -71.055226, 0
42.355969, -71.055288, 0
42.356058, -71.055373, 0
```


###### Example Polygon EGF File
```
POLY



Park Name, Feature Description



Post Office Square, Boundary of Post Office Square with holes for buildings
42.356856, -71.055757, 0
42.356080, -71.054976, 0
42.355697, -71.055636, 0
42.356003, -71.055941, 0
42.356767, -71.056220, 0

42.355955, -71.055522, 0
42.355894, -71.055458, 0
42.355846, -71.055546, 0
42.355908, -71.055615, 0

42.356089, -71.055312, 0
42.356005, -71.055226, 0
42.355969, -71.055288, 0
42.356058, -71.055373, 0

```

###### EGF Polygon - Commented Example
```
POLY  # Geometry type (POLY = Polygon)
# (blank line 1)
# (blank line 2)
# (blank line 3)
Park Name, Feature Description   # File's attribute headers
# (blank line 1)
# (blank line 2)
# (blank line 3)
Post Office Square, Boundary of Post Office Square with holes for buildings  # Attributes of first polygon feature
42.356856, -71.055757, 0  # Polygon's outer ring - 1st coordinate set (y, x, z)
42.356080, -71.054976, 0  # Polygon's outer ring - 2nd coordinate set (y, x, z)
42.355697, -71.055636, 0  # Polygon's outer ring - 3rd coordinate set (y, x, z)
42.356003, -71.055941, 0  # Polygon's outer ring - 4th coordinate set (y, x, z)
42.356767, -71.056220, 0  # Polygon's outer ring - 5th coordinate set (y, x, z)
# Blank line signifies that the following coordinate block is a hole in the polygon
42.355955, -71.055522, 0  # Polygon's 1st inner ring - 1st coordinate set (y, x, z)
42.355894, -71.055458, 0  # Polygon's 1st inner ring - 2nd coordinate set (y, x, z)
42.355846, -71.055546, 0  # Polygon's 1st inner ring - 3rd coordinate set (y, x, z)
42.355908, -71.055615, 0  # Polygon's 1st inner ring - 4th coordinate set (y, x, z)
# Second hole in polygon
42.356089, -71.055312, 0  # Polygon's 2nd inner ring - 1st coordinate set (y, x, z)
42.356005, -71.055226, 0  # Polygon's 2nd inner ring - 2nd coordinate set (y, x, z)
42.355969, -71.055288, 0  # Polygon's 2nd inner ring - 3rd coordinate set (y, x, z)
42.356058, -71.055373, 0  # Polygon's 2nd inner ring - 4th coordinate set (y, x, z)
# end file with blank line
```





[HOME](../README.md)
