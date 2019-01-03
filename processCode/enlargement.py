import os
import cv2
path = 'images/cropped_images'

ylist = [0, 648, 648*2]
xlist = [0, 648, 648*2, 648*3]
 
files = os.listdir(path)
for name in files:
    image = cv2.imread("%s/%s" % (path,name))
    # print(image)
    height , width = image.shape[:2]
    enlarged_image = cv2.resize(image,(2000, 2000), interpolation = cv2.INTER_NEAREST)
    filename = 'images/enlarged_images/' + name + "_enlarged.jpg"
    cv2.imshow('show', enlarged_image)
    cv2.imwrite(filename, enlarged_image)

cv2.waitKey(0)
cv2.destroyAllWindows()