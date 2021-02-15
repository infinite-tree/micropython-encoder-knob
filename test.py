import time
from encoder import EncoderKnob


def rotated(amount):
    print("Knob Rotated ", amount)

def pressed():
    print("Button Pressed")

def test():
    enc = EncoderKnob(18, 19, btn_pin=4, rotary_callback=rotated, btn_callback=pressed)
    while True:
        time.sleep(1)
        print()
        print("Knob Value: ", enc.value())
        print()

#
# Entry point
#
print("Turn the knob and press the button...")
test()