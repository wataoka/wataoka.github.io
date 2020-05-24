import os
import json
import argparse

from flask import Flask, render_template, url_for

app = Flask(__name__, static_url_path='/static')
works_json_path = os.path.join(app.static_folder, 'json/works.json')
careers_json_path = os.path.join(app.static_folder, 'json/careers.json')
skills_json_path = os.path.join(app.static_folder, 'json/skills.json')
studies_json_path = os.path.join(app.static_folder, 'json/studies.json')

@app.route('/')
def home():
    return render_template('/index.html')

@app.route('/portfolio.html')
def portfolio():
    with open(works_json_path) as works_json_file:
        works_list = json.load(works_json_file)
    return render_template('/portfolio.html', works_list=works_list)

@app.route('/work/<work_id>.html')
def work(work_id):
    with open(works_json_path) as works_json_file:
        works_list = json.load(works_json_file)
    work = works_list[int(work_id)]
    return render_template('/portfolio/work.html', work=work)

@app.route('/career.html')
def career():
    with open(careers_json_path) as careers_json_file:
        careers_list = json.load(careers_json_file) 
    return render_template('/career.html', careers_list=careers_list)

@app.route('/study.html')
def study():
    with open(studies_json_path) as studies_json_file:
        studies_list = json.load(studies_json_file) 
    return render_template('/study.html', studies_list=studies_list)

@app.route('/skill.html')
def skill():
    language_dict = {}
    framework_dict = {}
    machine_learning_dict = {}
    other_dict = {}
    with open(skills_json_path) as skills_json_file:
        skills_list = json.load(skills_json_file) 
    for id, skill in enumerate(skills_list):
        if skill['label'] == "language":
            language_dict[id] = skill
        elif skill['label'] == "framework":
            framework_dict[id] = skill
        elif skill['label'] == "machine_learning":
            machine_learning_dict[id] = skill
        elif skill['label'] == "other":
            other_dict[id] = skill
        else:
            print(skill.label + "は無効なラベルです。")
            exit(1)

    return render_template('/skill.html', language_dict=language_dict, framework_dict=framework_dict, machine_learning_dict=machine_learning_dict, other_dict=other_dict)

@app.route('/paper.html')
def paper():
    return render_template('/paper.html')

@app.route('/contact.html')
def contact():
    return render_template('/contact.html')

@app.route('/resume.html')
def resume():
    return render_template('/resume.html')

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', type=str, default='False')
    args = parser.parse_args()
    args.debug = (args.debug == 'True')
    return args

if __name__ == "__main__":
    args = parse_args()
    app.run(debug=args.debug)