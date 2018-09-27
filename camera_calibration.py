import numpy as np
import cv2
import glob
import matplotlib.pyplot as plt

# set corners inside squares
corner_x_size = 8 # 8 for rear and wide, 7 for test
corner_y_size = 6 # 6 for rear and wide, 5 for test

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((corner_y_size*corner_x_size,3), np.float32)
objp[:,:2] = np.mgrid[0:corner_x_size, 0:corner_y_size].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d points in real world space
imgpoints = [] # 2d points in image plane.

# Make a list of calibration images
# images = glob.glob('calibration_wide/GO*.jpg')
images = glob.glob('calibration_rear/*.png') # rear bag
# images = glob.glob('calibration_test/*.png') # test bag

# Step through the list and search for chessboard corners
for idx, fname in enumerate(images):
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Find the chessboard corners
    ret, corners = cv2.findChessboardCorners(gray, (corner_x_size,corner_y_size), None) # wide&rear
    # ret, corners = cv2.findChessboardCorners(gray, (7,5), None) # test bag


    # If found, add object points, image points
    if ret == True:
        objpoints.append(objp)
        imgpoints.append(corners)
        print objp
        print corners

        # Draw and display the corners
        cv2.drawChessboardCorners(img, (corner_x_size,corner_y_size), corners, ret) #wide and rear
        # cv2.drawChessboardCorners(img, (7, 5), corners, ret)# test bag
        #write_name = 'corners_found'+str(idx)+'.jpg'
        #cv2.imwrite(write_name, img)
        cv2.imshow('img', img)
        cv2.waitKey(0) #500
    else:
        print fname + " is not detected."

cv2.destroyAllWindows()