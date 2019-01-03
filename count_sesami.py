import argparse
import cv2
#import numpy as np
from sesami_detection import SESAMI

# You can adjust the values here ---------------
reSize=(900,960)
#-----------------------------------------------

ap = argparse.ArgumentParser()
ap.add_argument("-n", "--noSesami", required=True, help="Path to the image path with no Sesami")
ap.add_argument("-s", "--Sesami", required=True, help="Path to the image with Sesami")

args = vars(ap.parse_args())

objSesami = SESAMI(reSize=reSize, vThresh1=150, vThresh2=250, vErode=1, vDilate=2, debug=True)

# numNoSesami = objSesami.countSesami(cv2.imread(args["noSesami"]), minSize=35, maxSize=450)
numSesami = objSesami.countSesami(cv2.imread(args["Sesami"]), minSize=35, maxSize=300)
numSesami = objSesami.countSesami(cv2.imread(args["Sesami"]), minSize=35, maxSize=300)
# countSesami = (numSesami-numNoSesami) if (numSesami-numNoSesami>0) else 0

print("Sesami count: {}".format(numSesami))

cv2.waitKey(0)