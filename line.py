import numpy as np 
import cv2
import cv2 as cv
import glob



all_img = glob.glob("camera/*.*")

########################### Camera Calibration #############################################

# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((7*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:7].T.reshape(-1,2)
# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

for fname in all_img:
    img = cv.imread(fname)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, (7,7), None)
    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners)
        # Draw and display the corners
#        cv.drawChessboardCorners(img, (7,6), corners2, ret)
#        cv.imshow('img', img)
#        cv.waitKey(500)
#cv.destroyAllWindows()

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints,imgpoints,gray.shape[::-1],None,None)


#################################### Get main undisorted image
base = cv2.imread("test.jpg")

my_img =  cv2.undistort(base,mtx,dist,None,mtx)


### birds eyes view

pts1 = np.float32([[0, 540], [1184, 540],[479, 404], [688, 404]])
pts2 = np.float32([[0, 0], [400, 0],[0, 640], [400, 640]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)

result = cv2.warpPerspective(my_img, matrix, (500, 600))

cv2.imshow("result",result)
cv2.imshow("my_img",my_img)
cv2.waitKey(0)


