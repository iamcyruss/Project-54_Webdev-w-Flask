from flask import Flask
app = Flask(__name__)


"""
need to install flask in pycharm
pip install Flask didnt work for me. I installed it through pycharm packages
then need to set the environment variable 
$env:FLASK_APP="hello.py"
then run the server
flask run
"""


@app.route('/')
def hello_world():
    return 'Hello, World!'
