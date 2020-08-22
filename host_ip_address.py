import socket

hostname = socket.gethostname()
print("Host Name ", hostname)

print("IP Address ",socket.gethostbyname(hostname))