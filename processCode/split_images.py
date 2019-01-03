import os
import cv2
path = 'images'

ylist = [0, 648, 648*2]
xlist = [0, 648, 648*2, 648*3]
 
files = os.listdir(path)
for name in files:
    if name != 'cropped_images':
        image = cv2.imread("images/{}".format(name))
        i = 1
        for y in ylist:
            for x in xlist:
                namelist = name.split(".")
                name = namelist[0]
                cropped_image = image[y:y+648, x:x+648]
                filename = 'images/cropped_images/' + name + "_" + str(int(i)) + ".jpg";i+=1
                cv2.imwrite(filename, cropped_image)

cv2.waitKey(0)
cv2.destroyAllWindows()