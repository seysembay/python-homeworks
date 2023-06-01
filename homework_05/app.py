from flask import Flask
from flask import render_template
from views.about import about_app

app = Flask(__name__)
app.register_blueprint(about_app, url_prefix="/about")


@app.get("/", endpoint="index")
def index():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)
