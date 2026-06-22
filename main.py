import cv2
import pyautogui
import pyttsx3
import mediapipe as mp
import time
import threading
import speech_recognition as sr
import sounddevice as sd

from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# ---------------- SAFETY ----------------
pyautogui.FAILSAFE = True

# ---------------- AUDIO -----------------
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("System started")

# ---------------- VOICE SETUP ----------------
recognizer = sr.Recognizer()
move_distance = 50
running = True
paused = False

def record_audio(duration=3, samplerate=16000):
    audio = sd.rec(int(duration * samplerate),
                   samplerate=samplerate,
                   channels=1,
                   dtype='int16')
    sd.wait()
    return sr.AudioData(audio.tobytes(), samplerate, 2)

def voice_control():
    global running, paused
    while running:
        try:
            print("Listening...")
            audio = record_audio()
            command = recognizer.recognize_google(audio).lower()
            print("Voice:", command)

            if "left" in command:
                pyautogui.moveRel(-move_distance, 0)

            elif "right" in command:
                pyautogui.moveRel(move_distance, 0)

            elif "up" in command:
                pyautogui.moveRel(0, -move_distance)

            elif "down" in command:
                pyautogui.moveRel(0, move_distance)

            elif "click" in command and "double" not in command:
                pyautogui.click()
                speak("Click")

            elif "double click" in command:
                pyautogui.doubleClick()
                speak("Double click")

            elif "pause" in command:
                paused = True
                speak("Paused")

            elif "resume" in command:
                paused = False
                speak("Resumed")

            elif "stop" in command or "exit" in command:
                running = False
                speak("Stopping system")
                break

        except:
            pass

        time.sleep(0.3)

# ---------------- MODEL -----------------
base_options = python.BaseOptions(
    model_asset_path="face_landmarker.task"
)

options = vision.FaceLandmarkerOptions(
    base_options=base_options,
    num_faces=1
)

detector = vision.FaceLandmarker.create_from_options(options)

# ---------------- CAMERA ----------------
cap = cv2.VideoCapture(0)
screen_w, screen_h = pyautogui.size()

# ---------------- VARIABLES ----------------
blink_frames = 0
last_click_time = 0
click_cooldown = 1.0

# Cursor smoothing
prev_x, prev_y = screen_w / 2, screen_h / 2
smooth_factor = 0.7

# EAR calibration
calibrating = True
calibration_start = time.time()
ear_samples = []
blink_threshold = 0.18

frame_count = 0

# ---------------- START VOICE THREAD ----------------
threading.Thread(target=voice_control, daemon=True).start()

# ---------------- MAIN LOOP ----------------
while running:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb
    )

    frame_count += 1
    if frame_count % 2 != 0:
        cv2.imshow("Multimodal HCI", frame)
        if cv2.waitKey(1) & 0xFF in [27, ord('q')]:
            break
        continue

    result = detector.detect(mp_image)

    if result.face_landmarks and not paused:
        landmarks = result.face_landmarks[0]

        # ---------- HEAD MOVEMENT ----------
        nose = landmarks[1]
        x = nose.x * screen_w
        y = nose.y * screen_h

        smooth_x = prev_x * smooth_factor + x * (1 - smooth_factor)
        smooth_y = prev_y * smooth_factor + y * (1 - smooth_factor)

        pyautogui.moveTo(smooth_x, smooth_y)
        prev_x, prev_y = smooth_x, smooth_y

        # ---------- BLINK DETECTION ----------
        top = landmarks[159]
        bottom = landmarks[145]
        left = landmarks[33]
        right = landmarks[133]

        ear = abs(top.y - bottom.y) / abs(left.x - right.x)

        if calibrating:
            ear_samples.append(ear)
            if time.time() - calibration_start > 5:
                baseline_ear = sum(ear_samples) / len(ear_samples)
                blink_threshold = baseline_ear * 0.7
                calibrating = False
                speak("Calibration complete")
        else:
            if ear < blink_threshold:
                blink_frames += 1
            else:
                current_time = time.time()

                if 2 <= blink_frames < 5 and current_time - last_click_time > click_cooldown:
                    pyautogui.click()
                    last_click_time = current_time
                    speak("Single click")

                elif blink_frames >= 5 and current_time - last_click_time > click_cooldown:
                    pyautogui.doubleClick()
                    last_click_time = current_time
                    speak("Double click")

                blink_frames = 0

        cv2.putText(
            frame,
            f"EAR: {round(ear, 2)}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

    # ---------- UI ----------
    status_text = "PAUSED" if paused else "RUNNING"
    cv2.putText(
        frame,
        status_text,
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0) if not paused else (0, 0, 255),
        2
    )

    cv2.imshow("Multimodal HCI", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == 27 or key == ord('q'):
        break

# ---------------- CLEANUP ----------------
cap.release()
cv2.destroyAllWindows()
speak("System stopped")