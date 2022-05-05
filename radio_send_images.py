# radio_send_images.py

from microbit import *
import radio

radio.on()
radio.config(channel=7)

sleep(1000)

print("Image.HAPPY =", Image.HAPPY)
sleep(500)
packet = "HAPPY"
print( "getattr(Image, packet) =", getattr(Image, packet) )    
sleep(500)

string_list = ["HAPPY", "SAD", "ANGRY"]

while True:
    
    for packet in string_list:
        print("packet:", packet)
        display.show(getattr(Image, packet))
        packet = caesar(3, packet)
        print("Send encrypted:", packet)
        radio.send(packet)
        sleep(2500)
