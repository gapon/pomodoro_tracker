from imutils.video import VideoStream
import numpy as np
import time
import cv2
from fastai.vision import *
defaults.device = torch.device('cpu')

path = Path('data')

learn = load_learner(path)

def get_prediction(img):
    pred_class,pred_idx,outputs = learn.predict(img)
    return str(pred_class), str(pred_idx.item()), str(outputs)

vs = VideoStream(src=0).start()
# warm up the camera
time.sleep(2.0)

log_file = open('log.txt', 'w')

current_state = None
previous_state = None
current_state_time = 0
time_interval = 3

while True:
	# grab the current frame
	frame = vs.read()

	epoch_time = int(time.time())
	img_path = 'frames/frame_'+str(epoch_time)+'.jpg'
	cv2.imwrite(img_path,frame)

	# convert ndarray to fastai Image
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	frame = Image(pil2tensor(frame, dtype=np.float32).div_(255)).resize(224)

	
	current_state, class_idx, tensor = get_prediction(frame)

	if previous_state == None:
		previous_state = current_state

	print(current_state, previous_state)

	if current_state != previous_state:
		log_file.write(previous_state + ' ' + str(current_state_time) + '\n')
		current_state_time = 0

	current_state_time += time_interval
	previous_state = current_state
	time.sleep(time_interval)

vs.stop()
log_file.close()

# close all windows
cv2.destroyAllWindows()