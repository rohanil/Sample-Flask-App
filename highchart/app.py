from flask import Flask
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)

if __name__ == "__main__":
    app.run()


@app.route('/')
def show_entries():
    return render_template('example.html')