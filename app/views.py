import os
from app import app
from flask import render_template, request, url_for, redirect, json, Response

@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')


