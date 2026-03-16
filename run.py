import cv2
import socket
import time
from ultralytics import YOLO

# ---------------- CONFIG ----------------
MODEL_PATH = "Classroom_Project/Zone_AI_Brain/weights/best.pt"
PORT = 5000

# ----------------------------------------

# Load AI model
model = YOLO(MODEL_PATH)

# Find PC IP
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

print("===================================")
print("AI Classroom Control Server")
print("Server IP:", local_ip)
print("Waiting for ESP32 connection...")
print("===================================")

# Start TCP server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", PORT))
server.listen(1)

conn, addr = server.accept()
print("ESP32 Connected:", addr)

# Open camera
cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    if not ret:
        break

    # Run AI detection
    results = model(frame)

    # Default values
    fanA = 0
    fanB = 0
    fanC = 0
    ledA = 0
    ledB = 0

    for r in results:
        for box in r.boxes:

            cls = int(box.cls[0])
            label = model.names[cls]

            # -------- ZONE LOGIC --------

            if label == "Zone_A":
                fanA = 255
                ledA = 1

            elif label == "Zone_B":
                fanB = 255
                ledB = 1

            elif label == "Zone_C":
                fanC = 255

            elif label == "Zone_AB":
                fanA = 255
                fanB = 255
                ledA = 1
                ledB = 1

            elif label == "Zone_AC":
                fanA = 255
                fanC = 255
                ledA = 1

            elif label == "Zone_BC":
                fanB = 255
                fanC = 255
                ledB = 1

    # Create message
    message = f"{fanA},{fanB},{fanC},{ledA},{ledB}\n"

    try:
        conn.send(message.encode())
    except:
        print("ESP32 Disconnected")
        break

    print("Sent:", message.strip())

    # Display camera
    annotated = results[0].plot()
    cv2.imshow("Classroom AI", annotated)

    if cv2.waitKey(1) == 27:
        break

    time.sleep(0.2)

cap.release()
cv2.destroyAllWindows()
conn.close()
server.close()