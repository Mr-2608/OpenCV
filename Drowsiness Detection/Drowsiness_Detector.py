import cv2 as cv
import winsound as ws 

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

vid_cap = cv.VideoCapture(0)
font = cv.FONT_HERSHEY_SIMPLEX
no_frames = 0

while (vid_cap.isOpened()):
    
    frame = vid_cap.read()[1]
    gray_frame = cv.cvtColor(frame , cv.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray_frame,1.1,4)
    
    for (x,y,w,h) in faces:
        face_gray = gray_frame[y:y+h,x:x+w]
        face_BGR = frame[y:y+h,x:x+w]
        
        eyes = eye_cascade.detectMultiScale(face_gray)
        
        if eyes ==():
            no_frames += 1
            if no_frames>=20:
                cv.putText(frame , "Drowsiness Aleart!" , (100,100),font ,1,(0,0,255),1,cv.LINE_AA)
                ws.Beep(1000,500)
        else:
            no_loops = 0
        
        for (x1,y1,w1,h1) in eyes:
            cv.rectangle(face_BGR ,(x1,y1),(x1+w1,y1+h1),(0,0,255),2)
            
    cv.imshow("cap",frame)
    
    if cv.waitKey(1)==27:
        break
    
vid_cap.release() 
cv.destroyAllWindows()
