from ultralytics import YOLO
import os

# 1. SETUP - Point to your dataset folder
dataset_path = "datasets/cardboard_model"

def main():
    # Verify folders exist before starting
    if not os.path.exists(dataset_path):
        print(f"Error: Folder {dataset_path} not found! Run capture_data.py first.")
        return

    print("--- STARTING AI TRAINING ---")
    
    # 2. LOAD PRE-TRAINED MODEL
    # We use 'yolov8n-cls.pt' (The Classification Nano model)
    # It is very fast and perfect for small projects like a cardboard prototype.
    model = YOLO("yolov8n-cls.pt") 

    # 3. RUN TRAINING
    # data: Path to your organized folders
    # epochs: Number of times the AI reviews the photos (50-100 is ideal)
    # imgsz: Standard pixel size (224 is standard for classification)
    model.train(
        data=dataset_path, 
        epochs=100, 
        imgsz=224, 
        project="Classroom_Project",
        name="Zone_AI_Brain",
        device='cpu'  # Change to 0 if you have an NVIDIA GPU
    )

    print("\n--- TRAINING COMPLETE ---")
    print("Your new brain is saved as: Classroom_Project/Zone_AI_Brain/weights/best.pt")

if __name__ == "__main__":
    main()