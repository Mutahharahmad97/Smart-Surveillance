import cv2

frame = cv2.imread('C:/Users/SHAKH/Pictures/Ghulam.jpg')

image = frame.copy()

frame = 255 - frame

cv2.imshow("Frame",image)

cv2.waitKey(0)