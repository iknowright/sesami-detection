import cv2
import numpy as numpy

class SESAMI:
    def __init__(self, reSize=(1800,1290), vThresh1=210, vThresh2=120, vErode=2, vDilate=4, debug=False):
        self.resize = reSize
        self.thresh1 = vThresh1
        self.thresh2 = vThresh2
        self.erode = vErode
        self.dilate = vDilate
        self.indexNum = 0
        self.debug = debug

    def countSesami(self, image, minSize=25, maxSize=450):
        self.indexNum += 1
        numSesami = 0

        image = cv2.resize(image, self.resize, interpolation = cv2.INTER_AREA)
        if(self.debug==True and self.indexNum==2):   
            # cv2.imshow("Original #" + str(self.indexNum) , image)
            # cv2.imwrite("original.png", image)
            pass

        gray1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        (T, gray1) = cv2.threshold(gray1, self.thresh1, 255, cv2.THRESH_BINARY)
        gray1 = cv2.erode(gray1, None, iterations=self.erode)
        gray1 = cv2.dilate(gray1, None, iterations=self.dilate)

        lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        (L, A, gray2) = cv2.split(lab)
        (T, gray2) = cv2.threshold(gray2, self.thresh2, 255, cv2.THRESH_BINARY)
        gray2 = cv2.erode(gray2, None, iterations=self.erode)
        gray2 = cv2.dilate(gray2, None, iterations=self.dilate)

        gray = cv2.bitwise_or(gray1, gray2)

        # if(self.debug==True and self.indexNum==2):
        if(self.debug==True):            
            cv2.imshow("GRAY1", gray1)
            cv2.imshow("GRAY2", gray2)
            cv2.imshow("Final GRAY", gray)
            # pass

        (cnts, _) = cv2.findContours(gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        for (i, c) in enumerate(cnts):
            area = cv2.contourArea(c)
            (x, y, w, h) = cv2.boundingRect(c)
            hull = cv2.convexHull(c)
            hullArea = cv2.contourArea(hull)
            solidity = (area / float(hullArea)) if (hullArea>0) else 0

            # if(self.debug==True and self.indexNum==2):
            if(self.debug==True):                
                print ("area:{} , hullArea:{}, solidity:{}".format(area,hullArea,solidity))

            if((area>=minSize and area<=maxSize)):
                if((solidity>=0.7 and solidity<=1)):
                    numSesami += 1
                    ((x, y), radius) = cv2.minEnclosingCircle(c)
                    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)

        # if(self.debug==True and self.indexNum==2):
        if(self.debug==True):
            font = cv2.FONT_HERSHEY_COMPLEX_SMALL
            cv2.putText(image, "Sesami count: " + str(numSesami), (image.shape[1]-500, 40), font, 2, (255, 1, 126), 3)
            # cv2.imwrite("detectSesami.png", image)
            cv2.imshow("Sesami #" + str(self.indexNum) , image)

        return numSesami, image