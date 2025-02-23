import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time
from flask import Flask, jsonify

app = Flask(__name__)

mpHands = mp.solutions.hands
hands = mpHands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7, max_num_hands=2)
mpDraw = mp.solutions.drawing_utils

screen_width, screen_height = pyautogui.size()
running = False  # Flag to control webcam processing
cap = None  # Initialize camera variable

# Gesture tracking variables
prev_click_time = 0
dragging = False
scrolling = False
prev_pinch_distance = None

@app.route('/start', methods=['POST'])
def start_virtual_mouse():
    global running, cap
    if running:
        return jsonify({"message": "Already Running"})
    
    running = True
    cap = cv2.VideoCapture(0)  # Open Camera
    return jsonify({"message": "Virtual Mouse Started"})

@app.route('/stop', methods=['POST'])
def stop_virtual_mouse():
    global running, cap
    running = False
    if cap:
        cap.release()  # Release the camera
        cap = None
    return jsonify({"message": "Virtual Mouse Stopped"})

def map_to_screen(x, y, frame_width, frame_height):
    screen_x = np.interp(x, [100, frame_width - 100], [0, screen_width])
    screen_y = np.interp(y, [100, frame_height - 100], [0, screen_height])
    return int(screen_x), int(screen_y)

def run_virtual_mouse():
    global running, cap, prev_click_time, dragging, scrolling, prev_pinch_distance

    while True:
        if not running:
            time.sleep(0.1)
            continue
        
        if cap is None or not cap.isOpened():
            continue  # Skip iteration if the camera is closed

        ret, frame = cap.read()
        if not ret:
            continue

        frame = cv2.flip(frame, 1)
        frame_height, frame_width, _ = frame.shape
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)

        if results.multi_hand_landmarks:
            hand_count = len(results.multi_hand_landmarks)

            for handLMs in results.multi_hand_landmarks:
                landmarks = [(int(lm.x * frame_width), int(lm.y * frame_height)) for lm in handLMs.landmark]

                if len(landmarks) >= 8:
                    index_finger = landmarks[8]
                    thumb = landmarks[4]
                    middle_finger = landmarks[12]

                    screen_x, screen_y = map_to_screen(index_finger[0], index_finger[1], frame_width, frame_height)
                    pyautogui.moveTo(screen_x, screen_y, duration=0.05)

                    # Single Click Gesture (Index & Thumb Close)
                    click_distance = np.hypot(index_finger[0] - thumb[0], index_finger[1] - thumb[1])
                    if click_distance < 30:
                        current_time = time.time()
                        if current_time - prev_click_time > 0.5:
                            pyautogui.click()
                            prev_click_time = current_time

                    # Drag Gesture (Index & Middle Finger Close)
                    drag_distance = np.hypot(index_finger[0] - middle_finger[0], index_finger[1] - middle_finger[1])
                    if drag_distance < 40 and not dragging:
                        pyautogui.mouseDown()
                        dragging = True
                    elif drag_distance > 40 and dragging:
                        pyautogui.mouseUp()
                        dragging = False

                mpDraw.draw_landmarks(frame, handLMs, mpHands.HAND_CONNECTIONS)

            # Multi-Touch Gesture (Two Hands: Scroll & Zoom)
            if hand_count == 2:
                hand_1 = results.multi_hand_landmarks[0]
                hand_2 = results.multi_hand_landmarks[1]

                index_1 = (int(hand_1.landmark[8].x * frame_width), int(hand_1.landmark[8].y * frame_height))
                index_2 = (int(hand_2.landmark[8].x * frame_width), int(hand_2.landmark[8].y * frame_height))

                pinch_distance = np.hypot(index_2[0] - index_1[0], index_2[1] - index_1[1])

                if pinch_distance < 50 and not scrolling:
                    pyautogui.scroll(-10)
                    scrolling = True
                elif pinch_distance > 70 and scrolling:
                    pyautogui.scroll(10)
                    scrolling = False

                # Zoom Gesture
                if prev_pinch_distance is None:
                    prev_pinch_distance = pinch_distance

                zoom_sensitivity = 5
                if pinch_distance - prev_pinch_distance > zoom_sensitivity:
                    pyautogui.hotkey('ctrl', '+')
                elif prev_pinch_distance - pinch_distance > zoom_sensitivity:
                    pyautogui.hotkey('ctrl', '-')

                prev_pinch_distance = pinch_distance

                # Tab Switching Gesture (Based on Left vs Right Hand)
                left_hand = min(hand_1.landmark[0].x, hand_2.landmark[0].x)  # Leftmost hand
                right_hand = max(hand_1.landmark[0].x, hand_2.landmark[0].x)  # Rightmost hand

                if left_hand < 0.3:  # If left hand moves far left
                    pyautogui.hotkey('ctrl', 'shift', 'tab')  # Switch tab left
                elif right_hand > 0.7:  # If right hand moves far right
                    pyautogui.hotkey('ctrl', 'tab')  # Switch tab right

        cv2.imshow("Virtual Mouse", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            running = False
            if cap:
                cap.release()
                cap = None
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    import threading
    threading.Thread(target=run_virtual_mouse, daemon=True).start()
    app.run(debug=True, port=5000)
