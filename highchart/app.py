from flask import Flask
from flask_bootstrap import Bootstrap
from flask import Flask, render_template


app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def show_entries():
    return render_template('example.html')


if __name__ == "__main__":
    app.run()


