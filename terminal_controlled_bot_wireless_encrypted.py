# terminal_controlled_bot_wireless

from cyberbot import *
import radio

radio.on()
radio.config(channel=7,length=64)

sleep(1000)

key = -5

print("Ready...\n")

while True:
    packet = radio.receive()
    if packet is not None:
        print("Encrypted: ", packet)
        packet = ascii_shift(key, packet)
        print("Decrypted: ", packet)

        dictionary = eval(packet)

        vL = dictionary['vL']
        vR = dictionary['vR']
        ms = dictionary['ms']
        
        bot(18).servo_speed(vL)
        bot(19).servo_speed(-vR)
        sleep(ms)
        bot(18).servo_speed(None)
        bot(19).servo_speed(None)
