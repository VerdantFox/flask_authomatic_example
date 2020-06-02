from flask import Blueprint, render_template


core = Blueprint("core", __name__)


@core.route("/")
def index():
    """This is the home page view"""
    return render_template("core/index.html")
