# py-gpolyencode

This is a fork of the original `rcoup/py-gpolyencode` package, created due to the lack of support for the latest versions of Python. This version has been updated by [Codesyntax](https://www.codesyntax.com/) to ensure compatibility with Python 3.11 and beyond, while maintaining the functionality of the original package.

The package provides a Python port of the JavaScript Google Maps polyline encoder from Mark McClure, released under a BSD license. It includes a pure Python implementation (`gpolyencode`), along with comprehensive unit tests.

- **Original Project Homepage**: (No longer maintained) http://code.google.com/p/py-gpolyencode/
- **Updated Project Homepage**: [Codesyntax py-gpolyencode repository](https://github.com/codesyntax/py-gpolyencode)
- **Google Maps API Documentation**: https://developers.google.com/maps/documentation/utilities/polylinealgorithm
- **Additional Information**: http://facstaff.unca.edu/mcmcclur/GoogleMaps/EncodePolyline/

## Licensing

Copyright (c) 2009, Koordinates Limited

All rights reserved.


Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

- Redistributions of source code must retain the above copyright notice, this list of conditions, and the following disclaimer.
- Redistributions in binary form must reproduce the above copyright notice, this list of conditions, and the following disclaimer in the documentation and/or other materials provided with the distribution.
- Neither the name of Koordinates Limited nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

**Disclaimer**: THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

## Requirements

- Python >= 3.9


## Installing

### Pure Python Module (`py-gpolyencode`)

```bash
$ sudo python setup.py install
```

If you have the Python `easy_install` utility available, you can also type the following to download and install in one step:

```bash
$ pip install py-gpolyencode
$ pip install --upgrade py-gpolyencode  # to force upgrading
```

## Documentation

```bash
>>> import gpolyencode
>>> encoder = gpolyencode.GPolyEncoder()
# points are a sequence of (longitude,latitude) coordinate pairs
>>> points = ((8.94328,52.29834), (8.93614,52.29767), (8.93301,52.29322), (8.93036,52.28938), (8.97475,52.27014),)
>>> encoder.encode(points)
{'points':'soe~Hovqu@dCrk@xZpR~VpOfwBmtG', 'levels':'PG@IP', 'zoomFactor':2, 'numLevels':18}
```

Once you have your dictionary, passing it through a JSON encoder and adding it to some HTML or Javascript should be a piece of cake. See the Google Maps API documentation for GPolyline and GPolygon, or Mark McClure's website for lots of examples.

The constructor takes several arguments:
* `num_levels` specifies how many different levels of magnification the polyline will have. (default: 18)
* `zoom_factor` specifies the change in magnification between those levels. (default: 2)
* `threshold` indicates the length of a barely visible object at the highest zoom level. (default: 0.00001)
* `force_endpoints` indicates whether or not the endpoints should be visible at all zoom levels. (default: True)

See http://facstaff.unca.edu/mcmcclur/GoogleMaps/EncodePolyline/description.html for more details on what these parameters mean and how to tweak them. The defaults are sensible for most situations.

## Running the tests

The unit tests check compatibility with the original Javascript class by Mark McClure. There's a range of tests from simple encode-a-point tests through to 150K point lines.

1. install the Python module
2. run:
     $ python tests/gpolyencode_tests.py -v

## Contributing

Bug reports, suggestions, feedback, and contributions are all very welcome.

  * Homepage:       http://code.google.com/p/py-gpolyencode/
  * Issue Tracker:  http://code.google.com/p/py-gpolyencode/issues/list
  * Email:          robert.coup@koordinates.com