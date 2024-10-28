#!/usr/bin/env python3
"""
Flask app
"""

from flask import Flask, request, render_template
from flask_babel import Babel


app = Flask(__name__)


class Config(object):
    ''' App config '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def home():
    """
    Rendering template
    """
    return render_template('0-index.html')


@babel.init_app
def get_locale():
    ''' return best languages '''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(debug=True)
