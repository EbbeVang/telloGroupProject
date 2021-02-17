'''
Tello Drone project
'''

import socket 
import time

UDP_IP = "192.168.10.1"
UDP_PORT = 8889 # defined by tello sdk
print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
"""  """
print("Start communicating with drone")

sock = socket.socket(socket.AF_INET, # Internet
socket.SOCK_DGRAM) # UDP
sock.sendto(b'command', (UDP_IP, UDP_PORT))
time.sleep(5)
sock.sendto(b'takeoff', (UDP_IP, UDP_PORT))
time.sleep(5)
sock.sendto(b'forward 100', (UDP_IP, UDP_PORT))
time.sleep(5)
sock.sendto(b'flip f', (UDP_IP, UDP_PORT))
time.sleep(5)
sock.sendto(b'back 100', (UDP_IP, UDP_PORT))
time.sleep(5)
sock.sendto(b'land', (UDP_IP, UDP_PORT))