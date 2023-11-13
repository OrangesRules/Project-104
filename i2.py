import cv2

img =  cv2.imread("solar-system.jpg")

cv2.putText(img,"Sun",(20,220),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.7,color=(255,255,255))
cv2.putText(img,"Mercury",(120,180),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Venus",(190,260),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.7,color=(255,255,255))
cv2.putText(img,"Earth",(280,160),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.7,color=(255,255,255))
cv2.putText(img,"Mars",(380,260),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.7,color=(255,255,255))
cv2.putText(img,"Jupiter",(550,30),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.7,color=(255,255,255))
cv2.putText(img,"Saturn",(760,320),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.7,color=(255,255,255))
cv2.putText(img,"Uranus",(960,120),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.7,color=(255,255,255))
cv2.putText(img,"Neptune",(1110,300),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.7,color=(255,255,255))





cv2.imshow("orange", img)
cv2.waitKey(0)


