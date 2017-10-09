from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route ("/rooms")
def rooms ():
    return render_template("templates/rooms.html")


if __name__ == '__main__':
    app.run()
