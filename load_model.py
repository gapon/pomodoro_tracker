from fastai.vision import *
defaults.device = torch.device('cpu')

path = Path('data')

learn = load_learner(path)

def get_prediction(img):
    pred_class,pred_idx,outputs = learn.predict(img)
    return str(pred_class), str(pred_idx.item()), str(outputs)


img = open_image('frames/second_frame.jpg').resize(224)
print(get_prediction(img))