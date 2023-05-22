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


# led location 0x10 on testing
for i in range(8):
    led_loc(16, i, 1)
    time.sleep(0.1)

# led location 0x11 on testing
for i in range(8):
    led_loc(17, i, 1)
    time.sleep(0.1)

# led location 0x12 on testing
for i in range(8):
    led_loc(18, i, 1)
    time.sleep(0.1)

time.sleep(1.5)

# led location 0x10 off testing
for i in range(8):
    led_loc(16, i, 0)
    time.sleep(0.1)

# led location 0x11 off testing
for i in range(8):
    led_loc(17, i, 0)
    time.sleep(0.1)

# led location 0x12 off testing
for i in range(8):
    led_loc(18, i, 0)
    time.sleep(0.1)


# --------------------------------
# fix color in position by 01 == red 02 == blue etc;
# led address
# --------------------------------
