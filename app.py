from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get('/questions')
def questions():
    prompts = silly_story.prompts # list a of strings (words)
    return render_template("questions.html", prompts=prompts)

@app.get('/results')
def results():
    return render_template("results.html")