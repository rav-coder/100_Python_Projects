from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def html_wrap():
        return f'<b> {function()} </b>'

    return html_wrap


@app.route("/")
@make_bold
def hello_world():
    return "<p style='text-align: center'>Hello, World!</p>" \
           "<img src='https://media.giphy.com/media/Hq4yMpaMwNElJChQt0/giphy.gif'>"


@app.route("/bye")
def say_bye():
    return "Bye!"


@app.route("/users/<username>/<int:number>")
def greet(username, number):
    return f"Hello {username}, number: {number}! How are you?"


if __name__ == "__main__":
    app.run(debug=True)
