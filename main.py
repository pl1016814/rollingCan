#"Circular Shape Movement Detection" - Constantine Munoz P2, V1.0.5
#Process of code:
#Import libraries -> resize frame to reduce lag -> grayscale + gaussian blur ->
#Run Hough -> Find largest out of circles -> Draw the actual circle -> Show current frame

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True:
  ret, frame = cap.read()
# SETUP
  img = cv.resize(frame, (375, 500), interpolation=cv.INTER_AREA)
  gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
  #gaussian blur as stated in documentation doesn't work for my soda can, idk why
  gray = cv.GaussianBlur(gray, (7, 7), 1.5)

  circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, dp=1.2, minDist=200, param1=160, param2=35, minRadius=100, maxRadius=200)
  #opencv has a list in a list, this takes the circle that has the highest radius
  x, y, r = circles[0][circles[0][:, 2].argmax()]

  #they come back as floats
  cv.circle(img, (int(x), int(y)), int(r), (0, 255, 0), 3)
  cv.circle(img, (int(x), int(y)), 2, (0, 255, 0), 3)

  cv.imshow("Circular Shape Detection", img)
cap.release()
cv.destroyAllWindows()
