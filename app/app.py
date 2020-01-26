# install required packages
import dash
import dash_html_components as html

from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()