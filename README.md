# 👁️ Face and Eye Detection using OpenCV

This project demonstrates **Face Detection** and **Eye Detection** using Haar Cascade Classifiers in OpenCV.  
It detects faces and eyes from an image and draws bounding boxes around them.

---

## 📌 Project Structure
Face-Eye-Detection/
│
├── face_detection.py
├── eye_detection.py
├── haarcascade_frontalface_default.xml
├── haarcascade_eye.xml
└── README.md

---

## 🛠️ Technologies Used

- Python
- OpenCV (cv2)
- Haar Cascade Classifier

---

## 📂 How It Works

1. Load an image using OpenCV.
2. Resize the image.
3. Convert the image to grayscale.
4. Load the Haar Cascade XML classifier.
5. Detect faces or eyes using `detectMultiScale()`.
6. Draw rectangles around detected objects.
7. Display the output image.
8. Press **ESC (27)** key to close the window.

---

## ▶️ Installation

Install required library:

```bash
pip install opencv-python

```

## ▶️ Run the Project
Run Face Detection
```bash
python face_detection.py
```

Run Eye Detection
```bash
python eye_detection.py
```

## 🧠 Algorithm Used
This project uses the Haar Cascade Classifier, a machine learning-based object detection algorithm.

It works using:

1.Haar feature selection

2.Integral images

3.AdaBoost training

4.Cascade filtering for fast detection

---


## 📸 Output

The program draws a red bounding box around detected faces or eyes.

Press ESC to exit the display window.

---

## 🚀 Future Improvements

- Real-time detection using webcam

- Combine face and eye detection in one script

- Improve detection accuracy

- Deploy as a web application

---

## 👩‍💻 Author

### Suchitra Mary
### MSc Data Science
### Interested in Computer Vision & AI

---

