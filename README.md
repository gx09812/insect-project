# ⚡ Intelligent Energy-Saving Classroom System (IESCS)

An AI + IoT-based smart classroom system designed to reduce unnecessary energy consumption by detecting student presence in different zones and automatically controlling electrical devices.

---

## 📌 Project Overview
The **Intelligent Energy-Saving Classroom System (IESCS)** uses **Computer Vision + Embedded Systems** to monitor classroom occupancy and intelligently control lights and fans.

- Detects student presence using camera (YOLO/OpenCV)
- Divides classroom into zones (A, B, C…)
- Sends real-time data to ESP32
- Automatically switches ON/OFF electrical devices
- Reduces power wastage

---

## 🎯 Objectives
- Minimize energy consumption in classrooms  
- Automate electrical control using AI  
- Provide real-time monitoring dashboard  
- Build a scalable smart classroom solution  

---

## 🧠 System Architecture
Camera → Python (YOLO/OpenCV) → Zone Detection → Socket/WiFi → ESP32 → Relay/TRIAC → Lights/Fans
↓
Monitoring Dashboard

---

---

## 🧑‍💻 Project Team

| Member        | Role                          | Responsibility |
|---------------|-------------------------------|----------------|
| @Prasath      | Hardware Soldering            | Building and wiring TRIAC circuits, ensuring safe AC connections |
| @தன்ராஜ்      | UI/UX & Backend Monitoring    | Designing the monitoring dashboard, handling backend data flow |
| Member 3      | Computer Vision Engineer      | Developing Python/OpenCV scripts for zone detection and occupancy tracking |
| Member 4      | Embedded Systems Developer    | Programming ESP32/Arduino, managing communication |
| Member 5      | Project Coordinator & Docs    | Integration, documentation, timeline, reporting |

---

## 🌟 Features
- Real-time student detection  
- Zone-based energy control  
- AI-powered automation  
- ESP32 wireless communication  
- Dashboard monitoring system  
- Scalable for smart buildings  

---

## 🤖 AI Training Module

### Dataset
- Classroom images/videos collected manually  
- Labeled into:
  - Zone_A  
  - Zone_B  
  - Zone_C  
  - Zone_AB / Zone_BC  

### Annotation
- LabelImg / Roboflow  

### Model
- YOLO (Ultralytics)

### Training
```bash
pip install ultralytics opencv-python

yolo task=classify mode=train model=yolov8n.pt data=dataset.yaml epochs=50 imgsz=224


---

## 🧑‍💻 Project Team

| Member        | Role                          | Responsibility |
|---------------|-------------------------------|----------------|
| @Prasath      | Hardware Soldering            | Building and wiring TRIAC circuits, ensuring safe AC connections |
| @தன்ராஜ்      | UI/UX & Backend Monitoring    | Designing the monitoring dashboard, handling backend data flow |
| Member 3      | Computer Vision Engineer      | Developing Python/OpenCV scripts for zone detection and occupancy tracking |
| Member 4      | Embedded Systems Developer    | Programming ESP32/Arduino, managing communication |
| Member 5      | Project Coordinator & Docs    | Integration, documentation, timeline, reporting |

---

## 🌟 Features
- Real-time student detection  
- Zone-based energy control  
- AI-powered automation  
- ESP32 wireless communication  
- Dashboard monitoring system  
- Scalable for smart buildings  

---

## 🤖 AI Training Module

### Dataset
- Classroom images/videos collected manually  
- Labeled into:
  - Zone_A  
  - Zone_B  
  - Zone_C  
  - Zone_AB / Zone_BC  

### Annotation
- LabelImg / Roboflow  

### Model
- YOLO (Ultralytics)

### Training
```bash
pip install ultralytics opencv-python

yolo task=classify mode=train model=yolov8n.pt data=dataset.yaml epochs=50 imgsz=224


---

## 🧑‍💻 Project Team

| Member        | Role                          | Responsibility |
|---------------|-------------------------------|----------------|
| Prasath       | Hardware Soldering            | Building and wiring TRIAC circuits, ensuring safe AC connections |
| Thanraj       | UI/UX & Backend Monitoring    | Designing the monitoring dashboard, handling backend data flow |
| dharan        | Computer Vision Engineer      | Developing Python/OpenCV scripts for zone detection and occupancy tracking |
| vishunu       | Embedded Systems Developer    | Programming ESP32/Arduino, managing communication |
| me            | Project Coordinator & Docs    | Integration, documentation, timeline, reporting |

---

## 🌟 Features
- Real-time student detection  
- Zone-based energy control  
- AI-powered automation  
- ESP32 wireless communication  
- Dashboard monitoring system  
- Scalable for smart buildings  

---

## 🤖 AI Training Module

### Dataset
- Classroom images/videos collected manually  
- Labeled into:
  - Zone_A  
  - Zone_B  
  - Zone_C  
  - Zone_AB / Zone_BC  

### Annotation
- LabelImg / Roboflow  

### Model
- YOLO (Ultralytics)

### Training
```bash
pip install ultralytics opencv-python

yolo task=classify mode=train model=yolov8n.pt data=dataset.yaml epochs=50 imgsz=224
