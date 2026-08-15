🚦 TrafficVision

AI-Powered Vehicle Detection, Tracking & Traffic Analytics

TrafficVision is an end-to-end computer vision-based traffic monitoring system that analyzes traffic videos to detect, track, count, and classify vehicles.

The system processes uploaded traffic footage using YOLO11 and OpenCV, tracks detected vehicles across frames, calculates traffic statistics, and presents the results through a web-based dashboard.

---
📌 Overview

TrafficVision was built to go beyond simple object detection.

Instead of only detecting vehicles in individual frames, the system combines:

Vehicle Detection → Object Tracking → Vehicle Counting → Analytics → Dashboard Visualization

This allows traffic footage to be converted into meaningful traffic statistics through a complete application.

---

✨ Features

* 🚗 Vehicle detection using YOLO11
* 🎯 Multi-object vehicle tracking
* 🔢 Vehicle counting
* 🏷️ Vehicle classification
* 🎥 Video processing with OpenCV
* 📊 Traffic analytics dashboard
* 📈 Separate vehicle counts and statistics
* 🌐 FastAPI-based web application
* 📤 Video upload and processing
* 🎬 Processed video generation
* 🖥️ Browser-based dashboard for results

---

🧠 How It Works

TrafficVision follows an end-to-end processing pipeline:

```text
Traffic Video
      ↓
Video Upload
      ↓
YOLO11 Vehicle Detection
      ↓
Object Tracking
      ↓
Vehicle Classification
      ↓
Vehicle Counting
      ↓
Traffic Analytics
      ↓
Processed Video + Dashboard
```

1. Video Input

A traffic video is uploaded through the web interface.

2. Vehicle Detection

YOLO11 identifies vehicles appearing in each frame.

3. Object Tracking

Detected vehicles are tracked across consecutive frames to maintain their identities and avoid repeatedly counting the same vehicle.

4. Vehicle Counting

The tracking information is used to determine vehicle counts and generate traffic statistics.

5. Analytics

The system aggregates the detection and counting results into useful traffic information.

6. Dashboard

The results are presented through a web-based dashboard along with the processed video.

---

🛠️ Tech Stack

| Category             | Technology              |
| -------------------- | ----------------------- |
| Programming Language | Python                  |
| Object Detection     | YOLO11                  |
| Computer Vision      | OpenCV                  |
| Deep Learning        | PyTorch                 |
| Backend              | FastAPI                 |
| Server               | Uvicorn                 |
| Frontend             | HTML5, CSS3, JavaScript |
| Template Engine      | Jinja2                  |
| Data Processing      | NumPy                   |
| Image Processing     | Pillow                  |
| Version Control      | Git & GitHub            |

---

📂 Project Structure

```text
TrafficVision/
│
├── app/
│   ├── analytics/
│   │   ├── __init__.py
│   │   └── analytics.py
│   │
│   ├── counting/
│   │   ├── __init__.py
│   │   └── counter.py
│   │
│   ├── detection/
│   │   ├── __init__.py
│   │   └── detector.py
│   │
│   ├── tracking/
│   │   ├── __init__.py
│   │   └── tracker.py
│   │
│   ├── video/
│   │   ├── __init__.py
│   │   └── processor.py
│   │
│   └── main.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
├── templates/
│   └── index.html
│
├── .gitignore
├── requirements.txt
├── run.py
└── yolo11n.pt
```

---

⚙️ Installation

1. Clone the repository

```bash
git clone https://github.com/NitishkumarKonar/TrafficVision.git
cd TrafficVision
```

2. Create a virtual environment

```bash
python -m venv .venv
```

3. Activate the virtual environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell execution policy prevents activation, you can also run Python directly from the environment.

4. Install dependencies

```bash
pip install -r requirements.txt
```

---

▶️ Running the Application

Start the FastAPI application with:

```bash
python run.py
```

Or, if using Uvicorn directly:

```bash
uvicorn app.main:app --reload
```

Then open the application in your browser:

```text
http://127.0.0.1:8000
```

---

📊 Dashboard

The dashboard provides a visual overview of the analyzed traffic footage, including vehicle counts and processed video results.

---

🎥 Demo

The demo showcases:

* Uploading traffic footage
* Vehicle detection
* Vehicle tracking
* Vehicle counting
* Traffic analytics
* Processed video output
* Dashboard visualization

---

🎯 Use Cases

TrafficVision can be adapted for applications such as:

* 🚦 Traffic monitoring
* 🛣️ Highway traffic analysis
* 🅿️ Vehicle flow monitoring
* 📊 Traffic pattern analysis
* 🏙️ Smart city applications
* 🚘 Automated vehicle counting
* 📈 Transportation analytics

---

🚀 Future Improvements

Potential improvements include:

* Real-time CCTV camera support
* Traffic congestion estimation
* Vehicle speed estimation
* License plate recognition
* Traffic violation detection
* Historical traffic analytics
* Database integration
* Cloud deployment
* Multiple-camera monitoring
* Advanced traffic prediction using machine learning

---

💡 What I Learned

Building TrafficVision helped me strengthen my practical understanding of:

* Computer vision pipelines
* YOLO-based object detection
* Multi-object tracking
* Video processing with OpenCV
* Object counting logic
* FastAPI backend development
* Frontend/backend integration
* Building ML-powered applications
* Structuring an end-to-end AI project

---

 👨‍💻 Author

Nitish Kumar Konar

B.Sc. Computer Science | AI/ML & Data Science

Interested in Artificial Intelligence, Machine Learning, Computer Vision, and AI Engineering.

---

 ⭐ If you found this project interesting

Consider giving the repository a ⭐ on GitHub!

GitHub:
https://github.com/NitishkumarKonar/TrafficVision
