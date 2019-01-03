import argparse
import cv2
#import numpy as np
from sesami_detection import SESAMI

import os
import cv2
path = 'images/train'

cv2.waitKey(0)
cv2.destroyAllWindows()


# You can adjust the values here ---------------
reSize=(900,960)
#-----------------------------------------------

objSesami = SESAMI(reSize=reSize, vThresh1=150, vThresh2=250, vErode=1, vDilate=2, debug=True)
 
files = os.listdir(path)
for name in files:
    if name[-4:] == '.jpg':
        image = cv2.imread("%s/%s"%(path,name))
        numSesami, image = objSesami.countSesami(image, minSize=35, maxSize=300)
        filename = "CV2DetectedImages/" + name
        cv2.imwrite(filename, image)
        print("Sesami count for {} : {}".format(name,numSesami))






cv2.waitKey(0)