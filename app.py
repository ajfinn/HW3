# test2 project, app.py
# AJ Finn 10/10/2019
from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
