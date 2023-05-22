import time
from smbus import SMBus

i2cbus = SMBus(1)  # Specify the I2C bus number (e.g., 1 for /dev/i2c-1)
# Set the slave address by static addr

def led_loc(address, led_location, color_tagging):
    if led_location == 0:
        datalist1 = [0]  # led bytes data to sent
        if color_tagging == 0:
            datalist2 = [0, 0, 0]
        elif color_tagging == 1:
            datalist2 = [255, 0, 0]
    elif led_location == 1:
        datalist1 = [1]  # led bytes data to sent
        if color_tagging == 0:
            datalist2 = [0, 0, 0]
        elif color_tagging == 1:
            datalist2 = [255, 127, 0]
    elif led_location == 2:
        datalist1 = [2]  # led bytes data to sent
        if color_tagging == 0:
            datalist2 = [0, 0, 0]
        elif color_tagging == 1:
            datalist2 = [255, 255, 0]
    elif led_location == 3:
        datalist1 = [3]  # led bytes data to sent
        if color_tagging == 0:
            datalist2 = [0, 0, 0]
        elif color_tagging == 1:
            datalist2 = [0, 255, 0]
    elif led_location == 4:
        datalist1 = [4]  # led bytes data to sent
        if color_tagging == 0:
            datalist2 = [0, 0, 0]
        elif color_tagging == 1:
            datalist2 = [0, 0, 255]
    elif led_location == 5:
        datalist1 = [5]  # led bytes data to sent
        if color_tagging == 0:
            datalist2 = [0, 0, 0]
        elif color_tagging == 1:
            datalist2 = [75, 0, 130]
    elif led_location == 6:
        datalist1 = [6]  # led bytes data to sent
        if color_tagging == 0:
            datalist2 = [0, 0, 0]
        elif color_tagging == 1:
            datalist2 = [148, 0, 211]
    elif led_location == 7:
        datalist1 = [7]  # led bytes data to sent
        if color_tagging == 0:
            datalist2 = [0, 0, 0]
        elif color_tagging == 1:
            datalist2 = [255, 255, 255]
    data = datalist1 + datalist2  # Bytes data to display
    time.sleep(0.15)  # display delay
    # --------------------------------
    # display debugging
    print(data)
    # --------------------------------
    i2cbus.write_i2c_block_data(address, 0, data)

led_loc(16, 0, 1)
led_loc(16, 1, 1)
led_loc(16, 2, 1)
led_loc(16, 3, 1)
led_loc(16, 4, 1)
led_loc(16, 5, 1)
led_loc(16, 6, 1)
led_loc(16, 7, 1)

# --------------------------------
# fix color in position by 01 == red 02 == blue etc;
# led address
# --------------------------------