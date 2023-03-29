from machine import Pin
import utime
import random

led_green = Pin(16,Pin.OUT)
led_yellow = Pin(18,Pin.OUT)
led_red = Pin(20,Pin.OUT)

led_green.off()
led_yellow.off()
led_red.off()

led_list = [(led_green,'LED-GREEN'),
            (led_yellow,'LED-YELLOW'),
            (led_red,'LED-RED')]

import socket
import network
import time
wifi = 'Uncle Engineer(2.4GHz)'
password = '212224236'
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
time.sleep(1)

def send_data(data):
    serverip  = '192.168.0.100'
    port = 9000
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    server.connect((serverip,port))
    server.send(data.encode('utf-8'))
    data_server  = server.recv(1024).decode('utf-8')
    print('Server: ', data_server)
    server.close()
    
#send_data('Hello World')
for i in range(5):
    select = random.choice(led_list)
    led = select[0]
    name = select[1]
    text = '---{}---'.format(name)
    led.on()
    time.sleep(2)
    led.off()
    send_data(text)
    time.sleep(5)
    