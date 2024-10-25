#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    web_title = 'Welcome to Holberton'
    head1 = 'Hello world'
    return render_template('0-index.html',
                            web_title=web_title, head1=head1)

app.run(port=5000)
