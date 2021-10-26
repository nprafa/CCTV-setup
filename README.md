# CCTV-setup
CCTV set up using pi and esp32

This a home made cctv setup cost being within 6000 rs with front and rear camera. ESp32 has 2MP and pi camera 5Mp. With live streaming. For saving the video stream a server is used. The server setup details are also shared with the required commands.

#face recognition

The model training file "train_save.py" should run on ubuntu server when there is an update to the image data base, that is, adding new person

the saved model file by the name "dataset_faces.dat" should be copied to location on pi (not yet decided). From this location use the model to reload the model

and re-run the face recognition script "face_recognition_pi.py".

capture_stream.py - this should be used in the ubuntu server for saving live stream data

compress_image.py- this script is for resizing the image. I needed to use this because the pictures where taken using mobile

Note: make sure the picture is front facing other wise the model wont run.
