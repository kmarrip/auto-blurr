import cv2 
cap=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
while cap.isOpened():
	ret,frame=cap.read()
	if ret==True:
		gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		faces=face_cascade.detectMultiScale(gray,1.3,5)
		for (x,y,w,h) in faces:
			main=gray[y:y+h,x:x+w]
			main=cv2.blur(main,(31,31))
			gray[y:y+h,x:x+w]=main
			cv2.imshow("blurred",gray)
		if cv2.waitKey(1)==27:
			break
	else:
		break
# hello there this is just a comment for you people to understand thanks 
cap.release()
cv2.destroyAllWindows()