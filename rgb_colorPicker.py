# import cv2
# img = cv2.imread('C:\\Users\\sudhi\\OneDrive\\Documents\\Projects\\OpenCV\\object\\lena.png')
# cv2.imshow("img",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
import cv2
import numpy as np 
frameWidth = 640
frameheight =  480
cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameheight)
cap.set(10,150)

# myColors = [[5,107,0,19,255,255], #orange
#             [133,56,0,159,156,255], #purple
#             [57,76,0,100,255,255]] #green

# def findColor(img,myColors): #use this function to find all colors 
#     imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV) 
#     for color in myColors:
#         lower = np.array(color[0:3])
#         upper = np.array(color[3:6])
#         mask = cv2.inRange(imgHSV,lower,upper)
        # mask2 = cv2.flip(mask,1)
        # cv2.imshow("img",mask2)
def empty(a):
    pass
cv2.namedWindow("SlasherMix")
cv2.resizeWindow("SlasherMix",640,240)
cv2.createTrackbar("HueMin","SlasherMix",0,179,empty)
cv2.createTrackbar("HueMax","SlasherMix",179,179,empty)
cv2.createTrackbar("SatMin","SlasherMix",0,255,empty)
cv2.createTrackbar("SatMax","SlasherMix",255,255,empty)
cv2.createTrackbar("ValueMin","SlasherMix",0,255,empty)
cv2.createTrackbar("ValueMax","SlasherMix",255,255,empty)        
        
while True: 
    frame,img = cap.read()
    # findColor(img,myColors)
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("HueMin","SlasherMix")
    h_max = cv2.getTrackbarPos("HueMax","SlasherMix")
    s_min = cv2.getTrackbarPos("SatMin","SlasherMix")
    s_max = cv2.getTrackbarPos("SatMax","SlasherMix")
    v_min = cv2.getTrackbarPos("ValueMin","SlasherMix")
    v_max = cv2.getTrackbarPos("ValueMax","SlasherMix")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)
    img2 = cv2.flip(imgResult,1)
    cv2.imshow("mask",cv2.flip(mask,1))
    cv2.imshow("video",img2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows 