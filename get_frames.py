from imutils.video import VideoStream
import numpy as np
import cv2
import imutils
import time


vs = VideoStream(src=0).start()
# warm up the camera
time.sleep(2.0)

while True:
	# grab the current frame
	frame = vs.read()

	# resize the frame, blur it, and convert it to the HSV color space
	frame = imutils.resize(frame, width=600)
	#blurred = cv2.GaussianBlur(frame, (11, 11), 0)
	#hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

	epoch_time = int(time.time())

	cv2.imwrite('frames/frame_'+str(epoch_time)+'.jpg',frame)
	
	key = cv2.waitKey(1) & 0xFF

	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break
	time.sleep(30.0)

vs.stop()

# close all windows
cv2.destroyAllWindows()