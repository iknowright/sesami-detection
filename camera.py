import numpy as np
import cv2

cap = cv2.VideoCapture(2)
i = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        filename = 'shots/image'+str(i)+'.jpg';i+=1
        cv2.imwrite(filename, frame)
        img = cv2.resize(frame, (1920,1080))
        cv2.imshow('frame',img)
        if cv2.waitKey(500) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
