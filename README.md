# HoverPad_DUHACKS_4.0
  
**A touch-free, AI-powered gesture control system for seamless computer interaction.**  

## The Problem it Solves  
HoverPad eliminates the need for a physical mouse, enabling hands-free computer control. It is beneficial for:  

- **Hygienic hands-free control** – Reduces the need to touch surfaces in public/shared spaces.  
- **Accessibility** – Helps individuals with mobility impairments interact with computers.  
- **Productivity & multitasking** – Enables seamless tab switching, scrolling, and zooming with natural hand gestures.  

With AI-powered hand tracking, users can move the cursor, click, scroll, drag, and zoom effortlessly using simple gestures.  

## Challenges We Ran Into  
- **Gesture stability** – Fine-tuned detection confidence and applied smoothing filters.  
- **Clicking accuracy** – Optimized pinch distance thresholds for better response.  
- **Tab switching** – Implemented full-hand detection to ensure reliable switching between applications.  
- **Latency issues** – Optimized frame processing to improve real-time responsiveness.  

## Technologies We Used  
**OpenCV, MediaPipe, Flask, PyAutoGUI, JavaScript, HTML/CSS**  

# HoverPad - Gesture Controls  

## Single-Hand Gestures  
- 🖱 **Move Cursor** → Move your hand in the air  
- ✊ **Left Click** → Pinch thumb & index finger together (distance < 30px)  
- 🤏 **Drag & Drop** → Pinch thumb & middle finger together (distance < 40px)  
- 🖐 **Scroll** → Move hand up/down while fingers spread  
- ✋ **Stop Gesture Mode** → Show a fist for 2 seconds  

## Two-Hand Gestures  
- 🔄 **Zoom In/Out** → Move both hands apart/together  
- ↔ **Switch Tabs** → Move left or right hand far left/right  
- 🔄 **Scroll Up/Down** → Adjust distance between index fingers of both hands  
