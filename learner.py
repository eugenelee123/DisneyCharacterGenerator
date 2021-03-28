from fastbook import *
from fastai.vision.widgets import *
from fastai.vision.gan import *
from PIL import Image
import random,os
from werkzeug.utils import secure_filename
from flask import Flask, flash, request, redirect, url_for
from app import app

# gan = load_learner('app/static/export.pkl')

# def gan_gen():
#     gan.gan_trainer.switch(gen_mode = True)
#     img = learn.show_results(figsize(8,8),ds_type = DatasetType.Train, rows = 1)
#     img = PILImage.create(img)
#     img_io = BytesIO()
#     img_io.save(img, "JPEG", quality = 70)
#     return send_file(img_io,mimetype = "image'jpeg")
    # full_filename = os.path.join(app.config['IMG_FOLDER'], 'img.jpg')
   
    # return full_filename

