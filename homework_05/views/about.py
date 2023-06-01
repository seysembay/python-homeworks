from flask import Blueprint
from flask import render_template

about_app = Blueprint(
    "about_app",
    __name__,
    url_prefix="/about",
)


@about_app.get("/", endpoint="main")
def about_index():
    return render_template("about.html")
