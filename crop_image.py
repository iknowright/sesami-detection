import os
import cv2
path = 'shots'
 
files = os.listdir(path)
for name in files:
    image = cv2.imread("%s/%s"%(path,name))
    cropped_image = image[485:1775, 375:2175]
    filename = 'shot_crop/' + name
    cv2.imwrite(filename, cropped_image)

cv2.waitKey(0)
cv2.destroyAllWindows()