import cv2,datetime
cap=cv2.VideoCapture(0)
cap.set(3,1360)
cap.set(4,768)
while True:
    ret,frame=cap.read() #ret to check if frame is available or not
    if ret==True:
        font=cv2.FONT_HERSHEY_COMPLEX
        text='Width : ' + str(cap.get(3)) + '  Height : ' +  str(cap.get(4)) + "Time:" + str(datetime.datetime.now())
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame=cv2.putText(frame,text,(10,50),font,1,(0,255,255),2,cv2.LINE_AA)
        cv2.imshow('frame', frame)
        k = cv2.waitKey(1)
        if k == ord('q'):
            exit(0)
    else:
        print("Nothing to capture!")
        exit(0)
cap.release()
cv2.destroyAllWindows()