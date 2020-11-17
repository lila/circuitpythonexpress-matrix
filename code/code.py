import board
import neopixel

from adafruit_led_animation.animation.sparkle import Sparkle
from adafruit_led_animation.animation.sparklepulse import SparklePulse
from adafruit_led_animation.sequence import AnimationSequence
from adafruit_led_animation.color import AMBER, JADE, AQUA, PINK

# Update to match the pin connected to your NeoPixels
pixel_pin = board.A1
# Update to match the number of NeoPixels you have connected
pixel_num = 64

pixels = neopixel.NeoPixel(pixel_pin, pixel_num, brightness=0.9, auto_write=False)

animations = AnimationSequence(
    SparklePulse(pixels, speed=0.05, period=3, color=JADE), 
    SparklePulse(pixels, speed=0.05, period=3, color=AQUA),
    SparklePulse(pixels, speed=0.05, period=3, color=PINK),
    advance_interval=10, auto_clear=False,
)

while True:
    animations.animate()
