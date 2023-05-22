# --------------------------------
# I2C transfer command python converting
# using "i2ctransfer -y 1 w5@0x08 0x00 0x04 0xFF 0xFF 0x00" as a data format
# use 3rd - 5th digits to get color from user by RGB HEX code
# add optional command to select pattern Ex. "1 = 0, 0, 0", "2 = 255,0,0 (red)"
# fix color in position by 01 == red 02 == blue etc;
# led address
# --------------------------------

import time
from smbus import SMBus

i2cbus = SMBus(1)  # Specify the I2C bus number (e.g., 1 for /dev/i2c-1)
# Set the slave address by static addr


def led_loc(address, led_location, color_tagging):
    data_list1 = [led_location]  # led bytes data to send
    if color_tagging == 0:
        data_list2 = [0, 0, 0]
    else:
        if led_location == 0:
            data_list2 = [255, 0, 0]
        elif led_location == 1:
            data_list2 = [255, 127, 0]
        elif led_location == 2:
            data_list2 = [255, 255, 0]
        elif led_location == 3:
            data_list2 = [0, 255, 0]
        elif led_location == 4:
            data_list2 = [0, 0, 255]
        elif led_location == 5:
            data_list2 = [75, 0, 130]
        elif led_location == 6:
            data_list2 = [148, 0, 211]
        elif led_location == 7:
            data_list2 = [255, 255, 255]

    data = data_list1 + data_list2  # Bytes data to display
    time.sleep(0.15)  # display delay

    # --------------------------------
    # display debugging
    print(data)
    # --------------------------------

    i2cbus.write_i2c_block_data(address, 0, data)


#
led_locations = [16, 17, 18]  # LED locations: 0x10, 0x11, 0x12

# Turn on LEDs at each location
for loc in led_locations:
    for i in range(8):
        led_loc(loc, i, 1)
        time.sleep(0.1)

time.sleep(1.5)

# Turn off LEDs at each location
for loc in led_locations:
    for i in range(8):
        led_loc(loc, i, 0)
        time.sleep(0.1)
