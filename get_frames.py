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


while True:
	# grab the current frame
	frame = vs.read()

	epoch_time = int(time.time())
	img_path = 'frames/frame_'+str(epoch_time)+'.jpg'
	cv2.imwrite(img_path,frame)

	# convert ndarray to fastai Image
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	frame = Image(pil2tensor(frame, dtype=np.float32).div_(255)).resize(224)


	print(get_prediction(frame))


	time.sleep(3.0)

vs.stop()

# close all windows
cv2.destroyAllWindows()