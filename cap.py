import cv2
cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('my.mp4',fourcc,20.0,(640,480))
while True:
    ret,frame=cap.read() #ret to check if frame is available or not
    if ret==True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        out.write(frame)
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',frame)
        k=cv2.waitKey(1)
        if k==ord('q'):
            exit(0)
    else:
        print("Nothing to capture!")
        exit(0)
cap.release()
out.release()
cv2.destroyAllWindows()
#the video captured will be in color mode bcz we are capturing the video before conversion to grayscale