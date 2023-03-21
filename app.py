from flask import Flask, request, render_template

from stories import story, Story
app = Flask(__name__)


@app.route('/home')
def hom():
    return render_template("home.html", words = story.prompts)

@app.route('/story')
def result():
    arr = {}
    for word in story.prompts:
        arr.update({word: request.args.get(word)})
    newStory = story.generate(arr)

    return render_template("story.html", text = newStory)
