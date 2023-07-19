from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get('/questions')
def questions():  # ask_questions
    """display the form which prompts for values """

    prompts = silly_story.prompts  # list a of strings (words)
    return render_template("questions.html", prompts=prompts)


@app.get('/results')
def results():  # show_result
    """Turns the values to story and displays it"""
    # request.args is a already dict like obj
    answers = {key: request.args[key] for key in request.args}
    story = silly_story.get_result_text(answers)
    return render_template("results.html", story=story)
