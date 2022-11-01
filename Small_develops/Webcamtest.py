import cv2 #install opencv and import in cv2
cam=cv2.VideoCapture(0) #here we use the module VideoCapture with default input as 0 because and if you use another external webcam you can give like 1 or 2 
while cam.isOpened(): #camera will open with the isOpened module
    ret, frame = cam.read()
    if cv2.waitKey(2) == ord("q"): #here "q" is key used to quit the open camera and you can change it
        break
    cv2.imshow("NEKE_MAHA",frame) #you can give any name to camera frame
