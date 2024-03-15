from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

# Define prompts for the story
prompts = ["noun", "verb", "adjective"]

@app.route("/")
def ask_questions():
    return render_template("jinja.html", prompts=prompts)

@app.route("/story")
def show_story():
    text = generate_story(request.args)
    return render_template("story.html", text=text)

def generate_story(answers):
    template = "Once upon a time, there was a {adjective} {noun} who loved to {verb}!"
    story = template.format(adjective=answers["adjective"], noun=answers["noun"], verb=answers["verb"])
    return story

if __name__ == "__main__":
    app.run(debug=True)
