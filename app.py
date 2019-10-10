# test2 project, app.py
# AJ Finn 10/10/2019
from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html', pageTitle='My Calculator')

@app.route('/calc', methods=['GET','POST'])
def calc():
    if request.method == 'POST':
        form = request.form
        loanAmount = int(form['numOne'])
        payments = int(form['numTwo'])
        rate = int(form['numThree'])
        calc = loanAmount / ((((1 + rate)^payments)-1) / (rate(1+rate)^payments))
        return render_template('index.html', display=calc, pageTitle='My Calculator')
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
