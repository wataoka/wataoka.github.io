from data.work import works_dataset
from data.career import careers_dataset
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('/home.html')

@app.route('/portfolio.html')
def portfolio():
    works_dict = works_dataset.get_data_dict()
    return render_template('/portfolio.html', works_dict=works_dict)

@app.route('/work/<work_id>.html')
def work(work_id):
    work = works_dataset.get_data(work_id)
    return render_template('/portfolio/work.html', work=work)

@app.route('/career.html')
def career():
    careers_dict = careers_dataset.get_data_dict() 
    return render_template('/career.html', careers_dict=careers_dict)

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
