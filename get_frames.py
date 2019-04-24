from imutils.video import VideoStream
import numpy as np
import cv2
import imutils
import time


vs = VideoStream(src=0).start()
# allow the camera or video file to warm up
time.sleep(2.0)

# keep looping
while True:
	# grab the current frame
	frame = vs.read()

	# if we are viewing a video and we did not grab a frame,
	# then we have reached the end of the video
	#if frame is None:
	#	break

	# resize the frame, blur it, and convert it to the HSV
	# color space
	frame = imutils.resize(frame, width=600)
	#blurred = cv2.GaussianBlur(frame, (11, 11), 0)
	#hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

	epoch_time = int(time.time())

	cv2.imwrite('frames/frame_'+str(epoch_time)+'.jpg',frame)
	
	key = cv2.waitKey(1) & 0xFF

	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break
	time.sleep(5.0)

vs.stop()

# close all windows
cv2.destroyAllWindows()