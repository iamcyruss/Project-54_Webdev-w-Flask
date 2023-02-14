from flask import Flask
app = Flask(__name__)


"""
need to install flask in pycharm
pip install Flask didnt work for me. I installed it through pycharm packages
then need to set the environment variable 
$env:FLASK_APP="stupid.py"
then run the server
flask run
to get venv to run properly I needed to change something for windows
https://stackoverflow.com/questions/54776324/powershell-bug-execution-of-scripts-is-disabled-on-this-system 
I think I did it just for my user. still risky though...
"""


def make_bold(function):
    def bold_function(*args, **kwargs):
        if len(args) > 0:
            return f'<b>{function(args[0])}</b>'
        else:
            return f'<b>{function()}</b>'
    return bold_function


def make_emphasis(function):
    def em_function(*args, **kwargs):
        if len(args) > 0:
            return f'<em>{function(args[0])}</em>'
        else:
            return f'<em>{function()}</em>'
    return em_function


def make_underline(function):
    def under_function(*args, **kwargs):
        if len(args) > 0:
            return f'<u>{function(args[0])}</u>'
        else:
            return f'<u>{function()}</u>'
    return under_function


@app.route('/')
@make_bold
def hello_world():
    return 'Hello, World! 3 what the fuck is actually fucking happening?'


#below uses <name> from the url as the variable so whatever you pass into the url will be used in the function
@app.route('/username/<name>')
@make_underline
@make_bold
@make_emphasis
def bye_world(name):
    return f'Hello {name}.'


if __name__ == "__main__":
    app.run(debug=True)
