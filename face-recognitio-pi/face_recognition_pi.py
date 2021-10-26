#run this script on server
import cv2
import os
import face_recognition
import pickle
import numpy as np


TRAIN_DIR = "faces/data"
print("Streaming started")
video_capture = cv2.VideoCapture(0)

TOLERANCE = 0.5
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = "cnn"


all_face_encodings = {}
print("loading trained data")

with open('dataset_faces.dat','rb') as f:
    all_face_encodings = pickle.load(f)


face_names = list(all_face_encodings.keys())
face_encodings = np.array(list(all_face_encodings.values()))

print("loading trained data")

while True:
    # grab the frame from the threaded video stream
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # convert the input frame from BGR to RGB 
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    encodings = face_recognition.face_encodings(rgb)
    for face_encoding in encodings:
        results = face_recognition.compare_faces(face_encodings, face_encoding, TOLERANCE)
        if True in results:
            match = face_names[results.index(True)]
            print(f"match found:{match}")
        else:
            print("match not found")

    