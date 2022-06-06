import cv2
import numpy as np 
import math 



img = cv2.imread("my_test.jpg")
h,w,c = img.shape


def select_my_reg(img,p1,p2,p3,p4,p5,p6):
    reg = [
        (p1,p2),
        (p3,p4),
        (p5,p6)
    ]
    mask = np.zeros_like(img)
    mask_color = (255,) *3
    cv2.fillPoly(mask,np.array([reg],np.int32,),mask_color)
    mask_img = cv2.bitwise_and(img,mask)
    return mask_img


def just(x):
	pass

cv2.namedWindow('param')
cv2.createTrackbar('p1','param',0,w,just)
cv2.createTrackbar('p2','param',0,h,just)
cv2.createTrackbar('p3','param',0,w,just)
cv2.createTrackbar('p4','param',0,h,just)
cv2.createTrackbar('p5','param',0,w,just)
cv2.createTrackbar('p6','param',0,h,just)

while True:
	p1 = cv2.getTrackbarPos('p1','param')
	p2 = cv2.getTrackbarPos('p2','param')
	p3 = cv2.getTrackbarPos('p3','param')
	p4 = cv2.getTrackbarPos('p4','param')
	p5 = cv2.getTrackbarPos('p5','param')
	p6 = cv2.getTrackbarPos('p6','param')

	img = cv2.imread("my_test.jpg")

	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	blur = cv2.GaussianBlur(gray,(5,5),0)

	canny_img = cv2.Canny(blur,110,0)

	canny_view  = select_my_reg(canny_img,235,321,270,209,432,326)

	lines = cv2.HoughLinesP(canny_view,1,np.pi/180, 50,minLineLength=0,maxLineGap=157)
	
	try:
		for line1 in lines:
			x1_1,y1_1,x2_1,y2_1 = line1[0]

			cv2.line(img,(x1_1,y1_1),(x2_1,y2_1),(0,255,0),3 )
	except:
		None


	cv2.imshow("img",img)
	cv2.imshow("canny_view",canny_view)
	cv2.imshow("canny_img",canny_img)


	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()