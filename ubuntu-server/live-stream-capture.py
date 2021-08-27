import cv2

#print("Before URL")
cap = cv2.VideoCapture('http://192.168.0.101:8080/')
#print("After URL")

# We need to set resolutions.
# so, convert them from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
size = (frame_width, frame_height)

result = cv2.VideoWriter('filename.avi', 
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, size)

while True:

    #print('About to start the Read command')
    ret, frame = cap.read()
    if ret:
        # Write the frame into the
        # file 'filename.avi'
        result.write(frame)
        #print('About to show frame of Video.')
        cv2.imshow("Capturing",frame)
        #print('Running..')
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
