from flask import Flask
app = Flask(__name__)


"""
need to install flask in pycharm
pip install Flask didnt work for me. I installed it through pycharm packages
then need to set the environment variable 
$env:FLASK_APP="hello.py"
then run the server
flask run
to get venv to run properly I needed to change something for windows
https://stackoverflow.com/questions/54776324/powershell-bug-execution-of-scripts-is-disabled-on-this-system 
I think I did it just for my user. still risky though...
"""


@app.route('/')
def hello_world():
    return 'Hello, World!'
