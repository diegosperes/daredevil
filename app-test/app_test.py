# -*- coding: utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def default():
    return render_template('web-app-test.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8888)
