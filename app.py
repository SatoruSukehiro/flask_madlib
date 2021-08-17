from flask import Flask , request
from flask import render_template
from stories import Story
app = Flask(__name__)


@app.route("/")
def home():
    form_data = story.prompts
    
    return render_template('/form.html',form_data=form_data)


@app.route("/story")
def get_story():
    your_story = story.generate(request.args)
    print(request.args)
    return render_template('/story.html',your_story=your_story)



"""
I attempted to change the text color of only the adjective but had no such luck. I also tried to create a dropdown menu to change the template for the story I return but I dont understand fully what the activity is actually telling me to do. 
"""


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)
