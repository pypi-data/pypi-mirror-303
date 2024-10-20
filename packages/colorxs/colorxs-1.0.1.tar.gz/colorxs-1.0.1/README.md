# ColorXs
Make your terminal output a little more colorful.

![PyPI - Version](https://img.shields.io/pypi/v/colorxs)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/colorxs)
![PyPI - License](https://img.shields.io/pypi/l/colorxs)

## Table of Contents
* [Install](#install)
* [Quick Start](#quick-start)
* [Docs](#docs)
* [Contributing](#contributing)

## Install
To install ColorXs use `pip`.
```
pip3 install colorxs
```

## Quick Start
To get started with ColorXs first import functions from `colorxs` into your project like this.
```py
from colorxs import FUNCTIONS_HERE
```

To find out what to import, and how to use ColorXs check out the [docs](#docs).


## Docs

### Color
A Color made from an RGBValue.

Usage:
```py
from colorxs import Color, RGBValue, HexValue

# Make from RGBValue
color = Color(RGBValue(255, 255, 255))

# Make from HexValue
color = Color(HexValue("#ffffff").toRGB())

# Make from preset
color = Color.WHITE

# print with color
# Color.RESET sets color back to normal
print(f"{color}Hello World{Color.RESET}")
# Hello World (in white)
```

### RGBValue
Used to store basic RGB data.

Usage:
```py
from colorxs import RGBValue

rgb = RGBValue(255, 255, 255)
hexFromRGB = rgb.toHex()

print(rgb)
# RGBValue(255, 255, 255)
print(hexFromRGB)
# #ffffff
```

### HexValue
Used to store basic Hex data.

Usage:
```py
from colorxs import HexValue

h = HexValue("#FFFFFF")
rgbFromHex = h.toRGB()

print(h)
# #ffffff
print(rgbFromHex)
# RGBValue(255, 255, 255)
```

## Contributing
All types of contibutions are welcome for the ColorXs project, whether its updating the documentation, reporting issues, or simply mentioning TSafe in your projects.

Remember this before contibuting, you should open an **Issue** if you don't think you can contribute and open a **Pull Request** if you have a patch for an issue.



### Reporting Bugs
Before you submit a bug report make sure you have the following information or are using the following things.

* Make sure you're on the latest version.
* Make sure its not just on your end (if you were possibly using a python version we dont support).
* Check issues to see if it has already been reported.
* Collect the following info about the bug:
    * Stack Trace.
    * OS, Platform and Version (Windows, Linux, macOS, x86, ARM).
    * Possibly your input and the output.
    * Can you reliably reproduce the issue?

If you have all of that prepared you are more than welcome to open an issue for the community to take a look at.
