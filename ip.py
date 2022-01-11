
import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print ("El nombre de tu ordenador es: " + hostname)
print ("tu dirección IP es: " + ip)