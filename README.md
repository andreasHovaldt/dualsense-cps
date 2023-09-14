# dualsense-cps
CPS counter for the PS5 Dualsense controller, using [pydualsense](https://github.com/flok/pydualsense).
Program currently only counts the CPS for the X button.

# Installation


## Windows
Download [hidapi](https://github.com/libusb/hidapi/releases) and place the .dll and .lib in your Windows\System32 folder.
After, install both the [hidapi](https://pypi.org/project/hidapi/) and [pydualsense](https://pypi.org/project/pydualsense/) PyPI packages.

```bash
pip install --upgrade hidapi
pip install --upgrade pydualsense
```

## Linux
Check the [pydualsense GitHub page](https://github.com/flok/pydualsense#linux) for Linux installation documentation. 