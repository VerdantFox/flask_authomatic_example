from authomatic.adapters import WerkzeugAdapter
from flask import (
    Blueprint,
    Markup,
    abort,
    flash,
    make_response,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import generate_password_hash

# from root.users.forms import (
#     LoginForm,
#     RegistrationForm,
#     UserSettingsForm,
# )
from root.users.models import User
from root.users.oauth_config import authomatic

users = Blueprint("users", __name__)


@users.route("/register", methods=["GET", "POST"])
def register():
    """Registers the user in 'flask' database, 'users' collection"""
    pass


@users.route("/login", methods=["GET", "POST"])
def login():
    """Logs the user in"""
    pass


@users.route("/logout")
@login_required
def logout():
    pass


@users.route("/profile/<username>", methods=["GET", "POST"])
@login_required
def profile(username):
    pass


@users.route("/settings", methods=["GET", "POST"])
@login_required
def settings():
    pass

@users.route("/delete_account", methods=["GET", "POST"])
def delete_account():
    """Delete current user's account"""
    pass


@users.route("/facebook_oauth", methods=["GET", "POST"])
def facebook_oauth():
    return oauth_generalized("Facebook")


@users.route("/google_oauth", methods=["GET", "POST"])
def google_oauth():
    return oauth_generalized("Google")


@users.route("/github_oauth", methods=["GET", "POST"])
def github_oauth():
    """Perform github oauth register, login, or account association"""
    return oauth_generalized("GitHub")


@users.route("/facebook_oauth_disconnect", methods=["GET", "POST"])
def facebook_oauth_disconnect():
    return oauth_disconnect("Facebook")


@users.route("/google_oauth_disconnect", methods=["GET", "POST"])
def google_oauth_disconnect():
    return oauth_disconnect("Google")


@users.route("/github_oauth_disconnect", methods=["GET", "POST"])
def github_oauth_disconnect():
    return oauth_disconnect("GitHub")


# ----------------------------------------------------------------------------
# HELPER METHODS
# ----------------------------------------------------------------------------
def oauth_disconnect(oauth_client):
    """Generalized oauth disconnect"""
    pass


def oauth_generalized(oauth_client):
    """Generalized oauth login, register, and account association"""
    pass


def login_and_redirect(user):
    """Logs in user and redirects to 'next' in session, or index otherwise"""
    pass
