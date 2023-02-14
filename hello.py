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


#below uses <name> from the url as the variable so whatever you pass into the url will be used in the function
@app.route('/username/<name>')
def bye_world(name):
    return f'Hello {name}.'


if __name__ == "__main__":
    app.run(debug=True)
