from flask import Flask, render_template, request
from stories import story

app = Flask(__name__)


@app.route('/')
def root():
    prompts = story.prompts
    return render_template("index.html", prompts=prompts)


@app.route('/story', methods=['POST'])
def post_story():
    text = story.generate(request.form)
    return render_template("story.html", text=text)


if __name__ == '__main__':
    app.run()
