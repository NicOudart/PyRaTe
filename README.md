[<img src="Logo_PyRaTe.png" width="500"/>](Logo_PyRaTe.png)

# PyRaTe: Python tools for remote-sensing raster classification

_Python library made for Versailles Saint-Quentin-en-Yvelines university (UVSQ) students in remote-sensing_

---

## Description

PyRaTe is a Python library for the classification of pixels within raster image, in the context of satellite remote-sensing.

PyRaTe implements functions for:

* The importation of different bands of satellite images, in GeoTIFF format.

* The display of RGB images with georeferencing.

* Labelling pixels in a given image, to generate a training or test dataset, as a Pandas DataFrame.

* Display the distribution of pixels in a dataset (by band and by label).

* Training a classifier to identify pixels in an image.

* Testing a classifier on pixels from another image.

* Display the predictions made on a given image, with georeferencing.

## Installation

To install the library, get the `path` of PyRaTe on your computer and use the following Python command:

**Installation:**
~~~bash
pip install path/PyRaTe
~~~

If you want to update library, get the `path` of the new version of PyRaTe on your computer and use the following Python command: 

**Update:**
~~~bash
pip install path/PyRaTe --upgrade
~~~

Once the library is installed, you can import it with the Python command:

~~~bash
import PyRaTe
~~~

---

## License

This package is released under a MIT open source license. See **LICENSE**.

## Credits

© Nicolas OUDART

LATMOS/IPSL, UVSQ Université Paris-Saclay, Guyancourt, France