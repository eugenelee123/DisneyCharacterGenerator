import os
from app import app
from flask import render_template, request, url_for, redirect, json, Response, Flask
# from learner import gan_gen



@app.route('/', methods = ['GET'])
def index():
    # img = Image.new('RGB',...)
    # filename = gan_gen(img)
    # return render_template("index.html",img = filename)
    filename = os.path.join(app.config['IMG_FOLDER'], 'img.png')
    return render_template("index.html", img = filename)

@app.route('/display')
def display_image():
    img = Image.new('RGB',...)
    filename = gan_gen(img)
    return render_template("index.html", img = filename)

