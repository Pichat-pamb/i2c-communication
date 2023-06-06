class Control(object):
    # --------------------------------
# define led address to display on main node
led_addresses = [16, 17, 18]  # LED locations: 0x10, 0x11, 0x12
# --------------------------------

# Turn on LEDs at each location
for loc in led_addresses:
    for i in range(8):
        led_loc(loc, i, 1)
        time.sleep(0.01)

time.sleep(1.5)

# Turn off LEDs at each location
for loc in led_addresses:
    for i in range(8):
        led_loc(loc, i, 0)
        time.sleep(0.01)