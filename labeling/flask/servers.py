# # -*- coding: utf-8 -*-

import random
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/show_error")
def show_results():
    results = [dict(index=i, line='test', status=random.choice(['ok', 'warning', 'error'])) for i in range(10)]
    return render_template('show_result.html', results=results)


if __name__ == "__main__":
    app.run()
