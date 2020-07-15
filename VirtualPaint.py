# import cv2
# img = cv2.imread('C:\\Users\\sudhi\\OneDrive\\Documents\\Projects\\OpenCV\\object\\lena.png')
# cv2.imshow("img",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# import cv2
# import numpy as np 
# frameWidth = 640
# frameheight =  480
# cap = cv2.VideoCapture(0)
# cap.set(3,frameWidth)
# cap.set(4,frameheight)
# cap.set(10,150)

# myColors = [[5,114,0,19,255,255], #orange
#             [133,56,0,159,156,255], #purple
#             [57,76,0,100,255,255], #green
#             [161,93,148,176,171,255]] #pink 
#             # [25,0,228,103,117,255]] #jugnu 
# myColorValues = [[51,153,255],   #BGR
#                  [255,0,255],
#                  [0,255,0],
#                  [222,0,255]]            

# myPoints = [] ## [x,y,colorID]
# def findColor(img,myColors,myColorValues): #use this function to find all colors 
#     imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV) 
#     count=0
#     newPoints =[]
#     for color in myColors:
#         lower = np.array(color[0:3])
#         upper = np.array(color[3:6])
#         mask = cv2.inRange(imgHSV,lower,upper)
#         mask2 = cv2.flip(mask,1)
#         x,y = getContours(mask2)
#         cv2.circle(imgResult1,(x,y),15,myColorValues[count],cv2.FILLED)
#         if x != 0 and y != 0:
#             newPoints.append([x,y,count])
#         count+=1
#         # cv2.imshow(str(color[0]),mask2)
#     return newPoints    

# def getContours(img):
#     contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
#     x,y,w,h = 0,0,0,0 #if area is not greater tha 500 so something has to e return
#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         # print(area)
#         if area>500:
#             # cv2.drawContours(imgResult1, cnt, -1, (255, 0, 0), 3)
#             peri = cv2.arcLength(cnt,True)
#             #print(peri)
#             approx = cv2.approxPolyDP(cnt,0.02*peri,True)
#             # print(len(approx))
#             # objCor = len(approx)
#             x, y, w, h = cv2.boundingRect(approx)
#     return x+y//2,y        
# def drawCanvas(myPoint,myColorValues):
#     for point in myPoint:
#         cv2.circle(imgResult1,(point[0],point[1]),10,myColorValues[point[2]],cv2.FILLED)
# while True: 
#     success,img = cap.read()
#     img2 = cv2.flip(img,1)
#     imgResult1 = img2.copy() #everything is changeble in here draw anything in image
#     newPoints = findColor(img,myColors,myColorValues)
#     if len(newPoints)!=0:
#         for newP in newPoints:
#             myPoints.append(newP)
#     if len(myPoints)!=0:
#         drawCanvas(myPoints,myColorValues)        
#     cv2.imshow("video",imgResult1)
#     # cv2.imshow("img",mask2)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows 




"""updated version"""
import cv2
import numpy as np
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)
 
# myColors = [[5,107,0,19,255,255],
#             [133,56,0,159,156,255],
#             [57,76,0,100,255,255],
#             [90,48,0,118,255,255]]
# myColorValues = [[51,153,255],          ## BGR
#                  [255,0,255],
#                  [0,255,0],
#                  [255,0,0]]
 
myColors = [[5,114,0,19,255,255], #orange
            [133,56,0,159,156,255], #purple
            [57,76,0,100,255,255], #green
            [161,93,148,176,171,255]] #pink 
            # [25,0,228,103,117,255]] #jugnu 
myColorValues = [[51,153,255],   #BGR
                 [255,0,255],
                 [0,255,0],
                 [222,0,255]]            

myPoints =  []  ## [x , y , colorId ]
 
def findColor(img,myColors,myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints=[]
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask0 = cv2.inRange(imgHSV,lower,upper)
        mask = cv2.flip(mask0,1)
        x,y=getContours(mask)
        cv2.circle(imgResult,(x,y),15,myColorValues[count],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count +=1
        #cv2.imshow(str(color[0]),mask)
    return newPoints
 
def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            #cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2,y
 
def drawOnCanvas(myPoints,myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)
 
 
while True:
    success,img = cap.read()
    img2 = cv2.flip(img,1)
    imgResult = img2.copy()

    newPoints = findColor(img, myColors,myColorValues)
    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints,myColorValues)
 
 
    cv2.imshow("Result", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows