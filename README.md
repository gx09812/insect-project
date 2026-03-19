# ⚡ Intelligent Energy-Saving Classroom System (IESCS)

An AI + IoT-based smart classroom system designed to reduce unnecessary energy consumption by detecting student presence in different zones and automatically controlling electrical devices.

---

## 📌 Project Overview

The **Intelligent Energy-Saving Classroom System (IESCS)** uses **Computer Vision + Embedded Systems** to monitor classroom occupancy and intelligently control lights and fans.

### 🔹 Key Functions

* Detects student presence using camera (YOLO/OpenCV)
* Divides classroom into zones (A, B, C)
* Sends real-time data to ESP32
* Automatically switches ON/OFF electrical devices
* Reduces power wastage

---

## 🎯 Objectives

* Minimize energy consumption in classrooms
* Automate electrical control using AI
* Provide real-time monitoring dashboard
* Build a scalable smart classroom solution

---

## 🧠 System Architecture

```
Camera → Python (YOLO/OpenCV) → Zone Detection → WiFi/Socket → ESP32 → Relay/TRIAC → Lights/Fans
                                      ↓
                              Monitoring Dashboard
```

---

## 🌟 Features

* Real-time student detection
* Zone-based energy control
* AI-powered automation
* ESP32 wireless communication
* Dashboard monitoring system
* Scalable for smart buildings

---

## 🤖 AI Training Module

### 📂 Dataset

* Classroom images/videos collected manually
* Labeled into:

  * Zone_A
  * Zone_B
  * Zone_C
  * Zone_AB / Zone_BC

### 🏷️ Annotation Tools

* LabelImg
* Roboflow

### 🧠 Model

* YOLO (Ultralytics)

### ⚙️ Training Command

```bash
pip install ultralytics opencv-python

yolo task=classify mode=train model=yolov8n.pt data=dataset.yaml epochs=50 imgsz=224
```

---

## 🔌 Hardware Components

* ESP32
* TRIAC / Relay Module
* Camera (USB/Webcam)
* Power Supply
* Connecting Wires

---

## 🔄 Workflow

1. Camera captures classroom video
2. Python processes frames using YOLO
3. Zones with students are detected
4. Data sent to ESP32 via WiFi/socket
5. ESP32 controls relays/TRIAC
6. Lights/Fans turn ON/OFF automatically

---

## 🧑‍💻 Project Team

| Member  | Role                        | Responsibility                           |
| ------- | --------------------------- | ---------------------------------------- |
| Prasath | Hardware Soldering          | TRIAC circuit, wiring, AC safety         |
| Thanraj | UI/UX & Backend             | Dashboard + backend logic and hardware   |
| Dharan  | Computer Vision Engineer    | YOLO/OpenCV detection                    |
| Vishunu | Embedded Developer          | ESP32 programming & communication        |
| gx09812 | Coordinator & Documentation | Integration, reporting, overall checking |

---

## 📊 Future Enhancements

* Mobile app for monitoring
* Cloud integration (Firebase/AWS)
* Face recognition for attendance
* Smart scheduling system
* Energy usage analytics

---

## ⚠️ Safety Note

Working with AC mains (TRIAC circuits) can be dangerous.
Ensure proper insulation and supervision while handling hardware.

---

## 📎 License

This project is licensed under the **MIT License**.

---

## 📌 Conclusion

The IESCS project demonstrates how **AI + IoT** can be combined to create an efficient, scalable, and practical smart energy-saving system for classrooms and buildings.
