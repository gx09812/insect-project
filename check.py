import socket

# ---- GET PC IP ----
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
s.close()

print("PC IP Address:", ip)
print("Start ESP32 now...\n")

# ---- SERVER ----
HOST = "0.0.0.0"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Waiting for ESP32 connection...")

conn, addr = server.accept()

print("ESP32 Connected!")
print("ESP32 IP:", addr[0])

# ---- SEND DATA ----
while True:

    fanA = int(input("Fan A (0-255): "))
    fanB = int(input("Fan B (0-255): "))
    fanC = int(input("Fan C (0-255): "))

    ledA = int(input("LED A (0/1): "))
    ledB = int(input("LED B (0/1): "))

    data = f"{fanA},{fanB},{fanC},{ledA},{ledB}\n"

    conn.send(data.encode())

    print("Sent:", data)