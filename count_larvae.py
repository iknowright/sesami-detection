import argparse
import cv2
#import numpy as np
from larvae_detection import SESAMI

# You can adjust the values here ---------------
reSize=(2744,1678)
#-----------------------------------------------

ap = argparse.ArgumentParser()
ap.add_argument("-n", "--noSesami", required=True, help="Path to the image path with no Sesami")
ap.add_argument("-s", "--Sesami", required=True, help="Path to the image with Sesami")

args = vars(ap.parse_args())

objSesami = SESAMI(reSize=reSize, vThresh1=100, vThresh2=150, vErode=1, vDilate=2, debug=True)

# numNoSesami = objSesami.countSesami(cv2.imread(args["noSesami"]), minSize=35, maxSize=450)
numSesami, image = objSesami.countSesami(cv2.imread(args["Sesami"]), minSize=20, maxSize=300)
# countSesami = (numSesami-numNoSesami) if (numSesami-numNoSesami>0) else 0

print("Sesami count: {}".format(numSesami))

cv2.waitKey(0)