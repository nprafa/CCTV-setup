#run this script on server
import cv2
import os
import face_recognition


TRAIN_DIR = "faces/data"
print("Streaming started")
video_capture = cv2.VideoCapture(0)

TOLERANCE = 0.5
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = "cnn"


print("loading train data")
known_faces = []
known_names = []

for name in os.listdir(TRAIN_DIR):
    for filename in os.listdir(f"{TRAIN_DIR}/{name}"):
        image = face_recognition.load_image_file(f"{TRAIN_DIR}/{name}/{filename}")
        encodings = face_recognition.face_encodings(image)[0]
        known_faces.append(encodings)
        known_names.append(name)


print("loading test data")

while True:
    # grab the frame from the threaded video stream
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # convert the input frame from BGR to RGB 
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    encodings = face_recognition.face_encodings(rgb)
    print(encodings)
    for face_encoding in encodings:
        results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
        if True in results:
            match = known_names[results.index(True)]
            print(f"match found:{match}")
        else:
            print("match not found")

video_capture.release()
    