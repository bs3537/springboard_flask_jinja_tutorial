from flask import Flask, request, render_template
#from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample

#includes conditions, loops, and jinja templates, etc. 
app = Flask(__name__)
#app.config['SECRET_KEY'] = "Lexydog"

#debug = DebugToolbarExtension(app)

@app.route('/')
def index():
    return render_template("hello.html")

@app.route('/lucky')
def lucky_number():
    num = randint(1, 10)
    return render_template("lucky.html", lucky_num = num, msg="You are so lucky")

@app.route('/form')
def show_form():
    return render_template("form.html")

@app.route('/form2')
def show_form2():
    return render_template("form2.html")

COMPLIMENTS = ["cool", "clever", "awesome"]
@app.route('/greet')
def get_greeting():
    username = request.args["username"]
    nice_thing = choice(COMPLIMENTS)
    return render_template("greet.html", username=username, compliment = nice_thing)

@app.route('/greet2')
def get_greeting2():
    username = request.args["username"]
    wants  = request.args["wants_compliments"]
    nice_things = sample(COMPLIMENTS, 2)
    return render_template("greet2.html", username=username, wants_compliments = wants, compliments= nice_things)

@app.route('/greet2base')
def get_greeting2_base():
    username = request.args["username"]
    wants  = request.args["wants_compliments"]
    nice_things = sample(COMPLIMENTS, 2)
    return render_template("greet2.html", username=username, wants_compliments = wants, compliments= nice_things)

@app.route('/spell/<word>')
def spell_word(word):
    return render_template("word.html", word=word)

app.run(host='0.0.0.0', port=81)