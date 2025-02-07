# Motion Detection using OpenCV


### 📌 Overview
##### This project implements a simple motion detection system using OpenCV. It compares consecutive video frames to detect movement and highlights moving objects in real-time.
#


### 🎥 Demo
![Demo](demo.gif)
#


### 🛠 Features
##### ✅ Motion detection based on frame differencing
##### ✅ Adjustable motion sensitivity (motion_threshold & motion_hold)
##### ✅ Works with webcam or pre-recorded videos
##### ✅ Real-time object highlighting
##### ✅ Command-line arguments for easy customization
#


### 🏗 Installation
##### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/motion-detection.git
cd motion-detection
```
##### 2️⃣ Install dependencies
##### Make sure you have Python installed, then run:
```bash
pip install -r requirements.txt
```
##### 3️⃣ Run the program
```bash
python main.py --video path/to/video.mp4 
```
#

### ⚙ Configuration
##### This project supports custom motion detection settings via command-line arguments:
````md
| Argument             | Description |
|----------------------|-------------|
| `--video <path>`     | Path to a video file for motion detection |
| `--webcam`           | Use webcam instead of a video file |
| `--motion-threshold` | Minimum contour area to detect motion (default: `500`) |
| `--motion-hold`      | Number of frames to hold before checking motion (default: `5`) |
````
##### Example:
```bash 
python main.py --webcam --motion-threshold 300 --motion-hold 10
```
#

### 📂 Project Structure
```bash
motion-detection/
│── motion_detection.py   # Motion detection logic
│── config.py             # Handles command-line arguments (argparse)
│── main.py               # Runs the detection
│── requirements.txt      # Dependencies
│── README.md             # Project documentation
```
#

### 🖥 Dependencies
#####	•	🐍 Python 3.x
#####	•	📷 OpenCV (cv2)
#####	•	🔢 NumPy
#

### 📜 License
##### This project is licensed under the MIT License.



