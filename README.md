# HoverPad DUHACKS 4.0

**A touch-free, AI-powered gesture control system for seamless computer interaction.**

## 🚀 The Problem it Solves  

HoverPad eliminates the need for a physical mouse, enabling hands-free computer control. It is beneficial for:  

- **🦠 Hygienic hands-free control** – Reduces the need to touch surfaces in public/shared spaces.  
- **♿ Accessibility** – Helps individuals with mobility impairments interact with computers.  
- **⚡ Productivity & Multitasking** – Enables seamless tab switching, scrolling, and zooming with natural hand gestures.  

With AI-powered hand tracking, users can move the cursor, click, scroll, drag, and zoom effortlessly using simple gestures.  

---

## 🔧 Challenges We Ran Into  

- **🔄 Gesture stability** – Fine-tuned detection confidence and applied smoothing filters.  
- **🖱 Clicking accuracy** – Optimized pinch distance thresholds for better response.  
- **📑 Tab switching** – Implemented full-hand detection to ensure reliable switching between applications.  
- **⚡ Latency issues** – Optimized frame processing to improve real-time responsiveness.  

---

## 🛠 Technologies Used  

- **OpenCV** (Computer Vision)  
- **MediaPipe** (Hand Tracking)  
- **Flask** (Backend API)  
- **PyAutoGUI** (Simulating Mouse & Keyboard Actions)  
- **JavaScript, HTML, CSS** (Frontend UI)  

---

## ✋ HoverPad - Gesture Controls  

### ✋ Single-Hand Gestures  

| Gesture | Action |
|---------|--------|
| 🖱 **Move Cursor** | Move your hand in the air |
| ✊ **Left Click** | Pinch thumb & index finger together (distance < 30px) |
| 🤏 **Drag & Drop** | Pinch thumb & middle finger together (distance < 40px) |
| 🖐 **Scroll** | Move hand up/down while fingers spread |
| ✋ **Stop Gesture Mode** | Show a fist for 2 seconds |

### 👐 Two-Hand Gestures  

| Gesture | Action |
|---------|--------|
| 🔄 **Zoom In/Out** | Move both hands apart/together |
| ↔ **Switch Tabs** | Move left or right hand far left/right |
| 🔄 **Scroll Up/Down** | Adjust distance between index fingers of both hands |

---

### 🎯 Future Enhancements  
- **Voice Commands** to complement gesture control  
- **Machine Learning-Based Gesture Customization**  
- **Multi-User Hand Tracking for Collaboration Mode**  

---

### 📌 Setup Instructions  

1. Install dependencies using:  
   ```bash
   pip install -r requirements.txt
2. Run the Flask server:
   ```bash
   python pri.py
3. Open index.html in your browser and start using HoverPad!
