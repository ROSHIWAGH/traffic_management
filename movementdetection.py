import cv2

cap=cv2.VideoCapture("vtest.avi")

ret,frame1=cap.read()
ret,frame2=cap.read()

while cap.isOpened():
    diff=cv2.absdiff(frame1,frame2)
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    _,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated=cv2.dilate(thresh,None,iterations=3)
    contours,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    c=0
    for countour in contours:
        (x,y,w,h)=cv2.boundingRect(countour)
        if cv2.contourArea(countour)<700:
            continue
        c=int(c+1)
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
    st="Density: "+str(len(contours))
    s="Density: "+str(c)
    cv2.putText(frame1,s,(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),3)
    #cv2.drawContours(frame1,contour,-1,(0,255,0),2)
    cv2.imshow("feed",frame1)
    frame1=frame2
    ret,frame2=cap.read()
    if cv2.waitKey(40)==27:
        break
cv2.destroyAllWindows()
cap.release()