import cv2
from datetime import datetime
import time
import sys

#find a better way to do this or rewrite logic
def destroy_window_routine():
    if cv2.waitKey(1) & 0xFF == ord('q'):
                cap.release()
                cv2.destroyAllWindows()
                sys.exit()


while True:
    #print("Before URL")
    cap = cv2.VideoCapture('http://192.168.0.101:8080/')
    #print("After URL")

    # We need to set resolutions.
    # so, convert them from float to integer.
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    size = (frame_width, frame_height)
    
    now = datetime.now()
    current_time = now.strftime("%H-%M-%S") +".avi"
    result = cv2.VideoWriter(current_time, 
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, size)

    start_time_in_secons = time.time()
    time_limit = 3600

    while time.time() - start_time_in_secons < time_limit:
        #print('About to start the Read command')
        ret, frame = cap.read()
        if ret:
            # Write the frame into the
            # file 'filename.avi'
            result.write(frame)
        
            #print('About to show frame of Video.')
            cv2.imshow("Capturing",frame) #comment this if using this in server
            #print('Running..')
            destroy_window_routine()
    #in case we want to terminate the program
    destroy_window_routine()

    cap.release()
    cv2.destroyAllWindows()
