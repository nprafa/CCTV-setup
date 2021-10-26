#run this script on server
import cv2
import os
import face_recognition
import pickle


TRAIN_DIR = "faces/data"

TOLERANCE = 0.5
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = "cnn"


print("loading train data")

all_face_encodings={}

for name in os.listdir(TRAIN_DIR):
    for filename in os.listdir(f"{TRAIN_DIR}/{name}"):
        image = face_recognition.load_image_file(f"{TRAIN_DIR}/{name}/{filename}")
        all_face_encodings[name] = face_recognition.face_encodings(image)[0]


with open('dataset_faces.dat','wb') as f:
    pickle.dump(all_face_encodings,f)