from fastai.vision.all import *

path = Path('data/export.pkl')
learn = load_learner(path)

def get_prediction(img):
    pred_class,pred_idx,outputs = learn.predict(img)
    return str(pred_class), str(pred_idx.item()), str(outputs)


img_pth = 'frames/0-first_frame.jpg'
print(get_prediction(img_pth))