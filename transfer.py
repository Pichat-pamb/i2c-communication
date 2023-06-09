# --------------------------------
# I2C transfer command python converting
# using "i2ctransfer -y 1 w5@0x08 0x00 0x04 0xFF 0xFF 0x00" as a data format
# use 3rd - 5th digits to get color from user by RGB HEX code
# add optional command to select pattern Ex. "1 = 0, 0, 0", "2 = 255,0,0 (red)"
# --------------------------------

import time
from smbus import SMBus

i2cbus = SMBus(1)  # Specify the I2C bus number (e.g., 1 for /dev/i2c-1)

'''
datalist1 = [0]  # led bytes data to sent
datalist2 = [255, 0, 0]
data = datalist1 + datalist2  # Bytes data to display
time.sleep(0.15)  # display delay
# --------------------------------
# display debugging
# print(data)
# --------------------------------
i2cbus.write_i2c_block_data(address, 0, data)
'''

def led_loc1(address, tagging):
    datalist1 = [0]  # led bytes data to sent
    if tagging == 0:
        datalist2 = [0, 0, 0]
    elif tagging == 1:
        datalist2 = [255, 0, 0]
    data = datalist1 + datalist2  # Bytes data to display
    time.sleep(0.15)  # display delay
    # --------------------------------
    # display debugging
    print(data)
    # --------------------------------
    i2cbus.write_i2c_block_data(address, 0, data)

def led_loc2(address, tagging):
    datalist1 = [1]  # led bytes data to sent
    if tagging == 0:
        datalist2 = [0, 0, 0]
    elif tagging == 1:
        datalist2 = [255, 127, 0]
    data = datalist1 + datalist2  # Bytes data to display
    time.sleep(0.15)  # display delay
    print(data) # display debugging
    i2cbus.write_i2c_block_data(address, 0, data)

def led_loc3(address, tagging):
    datalist1 = [2]  # led bytes data to sent
    if tagging == 0:
        datalist2 = [0, 0, 0]
    elif tagging == 1:
        datalist2 = [255, 255, 0]
    data = datalist1 + datalist2  # Bytes data to display
    time.sleep(0.15)  # display delay
    print(data) # display debugging
    i2cbus.write_i2c_block_data(address, 0, data)

def led_loc4(address, tagging):
    datalist1 = [3]  # led bytes data to sent
    if tagging == 0:
        datalist2 = [0, 0, 0]
    elif tagging == 1:
        datalist2 = [0, 255, 0]
    data = datalist1 + datalist2  # Bytes data to display
    time.sleep(0.15)  # display delay
    print(data) # display debugging
    i2cbus.write_i2c_block_data(address, 0, data)

def led_loc5(address, tagging):
    datalist1 = [4]  # led bytes data to sent
    if tagging == 0:
        datalist2 = [0, 0, 0]
    elif tagging == 1:
        datalist2 = [0, 0, 255]
    data = datalist1 + datalist2  # Bytes data to display
    time.sleep(0.15)  # display delay
    print(data) # display debugging
    i2cbus.write_i2c_block_data(address, 0, data)

def led_loc6(address, tagging):
    datalist1 = [5]  # led bytes data to sent
    if tagging == 0:
        datalist2 = [0, 0, 0]
    elif tagging == 1:
        datalist2 = [75, 0, 130]
    data = datalist1 + datalist2  # Bytes data to display
    time.sleep(0.15)  # display delay
    print(data) # display debugging
    i2cbus.write_i2c_block_data(address, 0, data)

def led_loc7(address, tagging):
    datalist1 = [6]  # led bytes data to sent
    if tagging == 0:
        datalist2 = [0, 0, 0]
    elif tagging == 1:
        datalist2 = [148, 0, 211]
    data = datalist1 + datalist2  # Bytes data to display
    time.sleep(0.15)  # display delay
    print(data) # display debugging
    i2cbus.write_i2c_block_data(address, 0, data)

def led_loc8(address, tagging):
    datalist1 = [7]  # led bytes data to sent
    if tagging == 0:
        datalist2 = [0, 0, 0]
    elif tagging == 1:
        datalist2 = [255, 255, 255]
    data = datalist1 + datalist2  # Bytes data to display
    time.sleep(0.15)  # display delay
    print(data) # display debugging
    i2cbus.write_i2c_block_data(address, 0, data)

led_loc1(0x10, 1)
led_loc2(0x10, 1)
led_loc3(0x10, 1)
led_loc4(0x10, 1)
led_loc5(0x10, 1)
led_loc6(0x10, 1)
led_loc7(0x10, 1)
led_loc8(0x10, 1)

# --------------------------------
# fix color in position by 01 == red 02 == blue etc;
# led address
# --------------------------------

"""
switch_on(16, 1, 1)  # switch_on(adr, 1(red), 0n(1)-off(0))
time.sleep(0.1)
switch_on(17)
time.sleep(0.1)
switch_on(18)
"""
