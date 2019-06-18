from data import get_work , get_all_works
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('/home.html')

@app.route('/portfolio.html')
def portfolio():
    all_works = get_all_works()
    return render_template('/portfolio.html', all_works=all_works)

@app.route('/work/<work_name>.html')
def work(work_name):
    work = get_work(work_name)
    return render_template('/portfolio/work.html', work=work)

@app.route('/career.html')
def career():
    return render_template('/career.html')

@app.route('/skill.html')
def skill():
    return render_template('/skill.html')


@app.route('/paper.html')
def paper():
    return render_template('/paper.html')


@app.route('/contact.html')
def contact():
    return render_template('/contact.html')


@app.route('/resume.html')
def resume():
    return render_template('/resume.html')

if __name__ == "__main__":
    app.run(debug=True)
