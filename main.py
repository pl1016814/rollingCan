#"Circular Shape Movement Detection" - Constantine Munoz P2, V1.0.6
#Process of code:
#Import libraries -> resize frame to reduce lag -> grayscale + gaussian blur ->
#Run Hough -> Find largest out of circles based on previous circle -> Draw the actual circle ->
# Get current frame -> Add frame to final video -> This process takes like 15-30 seconds

import cv2 as cv
import numpy as np

#VIDEO SETUP
video = "rollingCan.mp4"
cap = cv.VideoCapture(video)
fps = cap.get(cv.CAP_PROP_FPS)
fourccCodec = cv.VideoWriter_fourcc(*"mp4v")
finalVideoPath = "finalCan.mp4"
finalVideo = cv.VideoWriter(finalVideoPath, fourccCodec, fps, (432, 768))
frameCount = 0

curRadiusMid = 125
while True:
  ret, frame = cap.read()
  if not ret or frame is None:
    break
  # SETUP
  img = cv.resize(frame, (432, 768), interpolation=cv.INTER_AREA)
  gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
  #gaussian blur as stated in documentation doesn't work for my soda can, idk why
  gray = cv.GaussianBlur(gray, (7, 7), 1.5)

  circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, dp=1.2, minDist=200, param1=160, param2=35, minRadius= int(curRadiusMid - 3), maxRadius= int(curRadiusMid + 2))
  #opencv has a list in a list, this takes the circle that has the lowest radius given parameters
  x, y, r = circles[0][circles[0][:, 2].argmax()]
  curRadiusMid = r

  #they come back as floats
  cv.circle(img, (int(x), int(y)), int(r+4), (0, 255, 0), 3)
  cv.circle(img, (int(x), int(y)), 2, (0, 255, 0), 3)

  finalVideo.write(img)
  frameCount += 1
cap.release()
cv.destroyAllWindows()
