import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('casecade/data/haarcascade_frontalface_alt2.xml')


while(True):
        #Frame tus buriig avch uzeh
    ret, frame = cap.read()
    gray = cv2.cvt.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_casecade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x, y, w, h) in faces:
        print(x,y,w,h)
        roi_gray = gray[y:y+h, x:x+w]
        img_item = "my-image.png"
        cv2.imwrite(img_item, roi_gray)
        #Recognition

        #Frame-deer zurag gargah
        color = (255, 0, 0) #Blue
        stroke = 3
        width = x + w
        end_cordinate_x = x + w
        end_cordinate_y = y + h
        cv2.rectangle(frame, (x,y), (end_cordinate_x, end_cordinate_y) , color , stroke)

    #Frame-iin ur dun
    cv2.imshow('frame',frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    #Duusgah /*Shell-deer space-deh*/
    cap.release()
    cv2.destroyAllWindows()

