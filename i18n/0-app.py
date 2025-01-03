#!/usr/bin/env python3
"""
Create a basic Flask template
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    """
    Rendering template
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
