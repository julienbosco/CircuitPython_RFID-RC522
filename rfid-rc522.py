# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2023 Julien Bosco
#
# SPDX-License-Identifier: MIT
"""
`rfid-rc522`
================================================================================

CircuitPython helper library form RFID-RC522 board.


* Author(s): Julien Bosco

Implementation Notes
--------------------

**Hardware:**

.. todo:: Add links to any specific hardware product page(s), or category page(s).
  Use unordered list & hyperlink rST inline format: "* `Link Text <url>`_"

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads

.. todo:: Uncomment or remove the Bus Device and/or the Register library dependencies
  based on the library's use of either.

# * Adafruit's Bus Device library: https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
# * Adafruit's Register library: https://github.com/adafruit/Adafruit_CircuitPython_Register
"""

# imports

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/julienbosco/CircuitPython_RFID-RC522.git"

import time
import board
import busio
from adafruit_bus_device.i2c_device import I2CDevice

class RFID_RC522:
    """
    Helper library for MFRC522 in I2C
    """

    def __init__(self, i2c):
        #Do something
        self._i2c = i2c

    def read_token():
        i2c.read()
