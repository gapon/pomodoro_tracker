from imutils.video import VideoStream
import numpy as np
import cv2
import imutils
import time


vs = VideoStream(src=0).start()
# warm up the camera
time.sleep(2.0)

# initialize the first frame
first_frame = None

while True:
	# grab the current frame
	frame = vs.read()

	frame = imutils.resize(frame, width=600)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (21, 21), 0)

	#epoch_time = int(time.time())

	#cv2.imwrite('frames/frame_'+str(epoch_time)+'.jpg',frame)
	
	if first_frame is None:
		first_frame = gray
		continue


	frame_delta = cv2.absdiff(first_frame, gray)
	thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]


	cv2.putText(frame, "Delta: {}".format(text), (10, 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
	cv2.imshow("Security Feed", frame)

	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break


	time.sleep(5.0)

vs.stop()

# close all windows
cv2.destroyAllWindows()