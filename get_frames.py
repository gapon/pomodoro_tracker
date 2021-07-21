# USAGE
# python get_frames.py -a True -d True -l log42
# python get_frames.py
from imutils.video import VideoStream
import argparse
import serial
import numpy as np
import time
import cv2
from fastai.vision.all import *
import os
ARDUINO_PORT = os.getenv('ARDUINO_PORT')

ap = argparse.ArgumentParser()
ap.add_argument('-a', '--arduino', type=bool, default=False, help='arduino connection')
ap.add_argument('-d', '--debug', type=bool, default=False, help='debug mode, save frames')
ap.add_argument('-l','--log', type=str, default='log', help='log file name')
args = vars(ap.parse_args())

if args['arduino']:
    arduino = serial.Serial(ARDUINO_PORT, 9600)

path = Path('data/export.pkl')
learn = load_learner(path)

def get_prediction(img):
    pred_class,pred_idx,outputs = learn.predict(img)
    return str(pred_class), str(pred_idx.item()), str(outputs)

vs = VideoStream(src=0).start()
# warm up the camera
time.sleep(2.0)

log_file = open('logs/'+args['log'], 'w')

current_state = None
previous_state = None
current_state_time = 0
time_interval = 5


try:
	while True:
		# grab the current frame
		frame = vs.read()

		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

		current_state, class_idx, tensor = get_prediction(frame)

		if args['debug']:
			frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
			epoch_time = int(time.time())
			img_path = 'frames/' + str(epoch_time) + current_state +'.jpg'
			cv2.imwrite(img_path,frame)

		if args['arduino']:
			if current_state == 'face':
				arduino.write(b'F')
			else:
				arduino.write(b'N')

		if previous_state == None:
			previous_state = current_state

		print(current_state, previous_state)

		if current_state != previous_state:
			log_file.write(previous_state + ' ' + str(current_state_time) + '\n')
			current_state_time = 0

		current_state_time += time_interval
		previous_state = current_state
		time.sleep(time_interval)
except KeyboardInterrupt:
	if args['arduino']:
		arduino.close()
		print('Arduino Serial Closed')

	log_file.close()
	print('File Closed')
	vs.stop()
	print('Video Strem Closed')

print('FINISHED')
