from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import STORIES

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get('/questions')
def questions():  # ask_questions
    """display the form which prompts for values """
    story_id = request.args["story"]
    prompts = STORIES[story_id].prompts  # list a of strings (words)
    return render_template("questions.html", prompts=prompts, story_id=story_id)


@app.get('/results')
def results():  # show_result
    """Turns the values to story and displays it"""
    # request.args is a already dict like obj
    answers = {key: request.args[key] for key in request.args if key != "story_id"}
    story_id = request.args["story_id"]
    story = STORIES[story_id].get_result_text(answers)
    return render_template("results.html", story=story)

@app.get('/')
def show_homepage():
    # story = {story_id: story_object}
    # story_id_to_name = {story: STORIES[story].name for story in STORIES}
    story_id_to_names = [(story_id, story.name) for (story_id, story) in STORIES.items()]
    # story_id_to_name = {story_tuple[0]: story_tuple[1].name for story_tuple in STORIES.items()}
    return render_template("index.html", story_id_to_names=story_id_to_names)