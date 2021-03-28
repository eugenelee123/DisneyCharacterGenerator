import os
from app import app
from flask import render_template, request, url_for, redirect, json, Response
from learner import gan_gen

@app.route('/', methods = ['GET'])
def index():
    img = gan_gen()
    return render_template("index.html", img = img)

@app.route('/display')
def display_image():
    return 200

