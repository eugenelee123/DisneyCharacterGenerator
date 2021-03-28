from fastbook import *
from fastai.vision.widgets import *
from fastai.vision.gan import *

gan = load_learner('app/static/export.pkl')

def gan_gen():
    gan.gan_trainer.switch(gen_mode = True)
    img = learn.show_results(figsize(8,8),ds_type = DatasetType.Train, rows = 1)
    img = PILImage.create(img)
    return img