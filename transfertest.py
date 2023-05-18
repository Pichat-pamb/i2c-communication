import time
from smbus import SMBus

i2cbus = SMBus(1)  # Specify the I2C bus number (e.g., 1 for /dev/i2c-1)
address = 0x08  # I2C slave device address
i = 0

def send_command(command, data):
    i2cbus.write_i2c_block_data(address, 0, (command + data))


def main():
    while True:
        i = i + 1
        # Create the command and data.
        command = [0]
        data = [0x00, 0x00, 0xAA]

        # Send the command and data to the display.
        send_command(command, data)

        time.sleep(0.2)


if __name__ == "__main__":
    main()