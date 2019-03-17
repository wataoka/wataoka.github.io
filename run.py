from data import get_work_data , get_work_list
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('/home.html')

@app.route('/portfolio.html')
def portfolio():
    work_list = get_work_list()
    return render_template('/portfolio.html', work_list=work_list)

@app.route('/work/<work_name>.html')
def work(work_name):

    work_data = get_work_data(work_name)

    return render_template('/portfolio/work.html', work_data=work_data)

@app.route('/career.html')
def career():
    return render_template('/career.html')

@app.route('/contact.html')
def contact():
    return render_template('/contact.html')

if __name__ == "__main__":
    app.run(debug=True)
