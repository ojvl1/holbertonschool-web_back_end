#!/usr/bin/env python3
"""
Flask app
"""

from flask import Flask, request, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config():
    """App config"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def home():
    """
    Rendering template
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
