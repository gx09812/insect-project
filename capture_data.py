import cv2
import os

# 1. SETUP - This matches your Tree Path
base_path = "datasets/cardboard_model"
zones = ['Zone_A', 'Zone_B', 'Zone_C', 'Zone_AB', 'Zone_BC', 'Zone_AC']

# Create folders if they don't exist
for z in zones:
    os.makedirs(f"{base_path}/{z}", exist_ok=True)

# 2. CONNECT CAMERA
# Use 0 for Laptop Webcam. 
# Use "http://192.168.1.XX" (your ESP IP) to capture directly from the car camera.
cap = cv2.VideoCapture(0) 

# Initial counts based on existing files
counts = {z: len(os.listdir(f"{base_path}/{z}")) for z in zones}

print("--- DATA COLLECTOR ACTIVE ---")
print("Press 'a', 'b', 'c' for Single Zones")
print("Press '1' for AB, '2' for BC, '3' for AC")
print("Press ESC to Quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Create a display copy to draw text on
    display = frame.copy()
    
    # Overlay the current counts on the screen
    y_offset = 30
    for z in zones:
        color = (0, 255, 0) if counts[z] > 0 else (0, 0, 255)
        cv2.putText(display, f"{z}: {counts[z]} imgs", (10, y_offset), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
        y_offset += 25

    cv2.imshow("Capture Training Data", display)

    # Listen for Key Presses
    key = cv2.waitKey(1) & 0xFF
    target = None

    if key == ord('a'): target = 'Zone_A'
    elif key == ord('b'): target = 'Zone_B'
    elif key == ord('c'): target = 'Zone_C'
    elif key == ord('1'): target = 'Zone_AB'
    elif key == ord('2'): target = 'Zone_BC'
    elif key == ord('3'): target = 'Zone_AC'
    elif key == 27: # ESC key
        break

    # If a valid key was pressed, save the image
    if target:
        filename = f"{base_path}/{target}/img_{counts[target]}.jpg"
        cv2.imwrite(filename, frame)
        counts[target] += 1
        
        # Simple "Flash" effect on the screen to confirm save
        flash = frame.copy()
        cv2.rectangle(flash, (0,0), (frame.shape[1], frame.shape[0]), (255,255,255), -1)
        cv2.imshow("Capture Training Data", flash)
        cv2.waitKey(50) 
        
        print(f"Saved to {target} | Total images: {counts[target]}")

cap.release()
cv2.destroyAllWindows()
print("Data collection complete. Now run train_model.py!")