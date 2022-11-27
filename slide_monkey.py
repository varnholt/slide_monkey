#!/usr/bin/env python3

# listens to microphone input and turns the recognized commands into 
# left/right keyboard controls that are sent to powerpoint
#
# SpeechRecognition API documentation:
# https://pypi.org/project/SpeechRecognition/
#
# pip install SpeechRecognition
# pip install keyboard
# pip install pyautogui

import keyboard
from pyautogui import hotkey
import time
import speech_recognition as sr

def callback(recognizer, audio):

    try:
        # sentences to recognize:
        # - go to the next
        # - go to the previous
        recognized_text = recognizer.recognize_google(audio).lower()
        print("recognized: {}".format(recognized_text))

        if "to the next" in recognized:
            print("go to next slide")
            hotkey("right")
        elif "to the previous" in recognized:
            print("go to previous slide")
            hotkey("left")
    except sr.UnknownValueError as e:
        print("unknown value error: {}".format(e))
    except sr.RequestError as e:
        print("request error: {}".format(e))

recognizer = sr.Recognizer()
mic = sr.Microphone(device_index=1)
with mic as source:

    # calibrate once, before we start listening
    recognizer.adjust_for_ambient_noise(source)

# start listening in background 
stop_listening = recognizer.listen_in_background(mic, callback)

# idle
print("listening, press 'q' to stop")
while True:
    try:
        if keyboard.is_pressed('q'):
            print("done")
            break
    except:
        break 
    time.sleep(0.1)

# stop listening
stop_listening(wait_for_stop=False)


