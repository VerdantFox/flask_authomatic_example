"""A file for testing oauth setup"""
from authomatic.adapters import WerkzeugAdapter
from flask import Flask, make_response, request

from oauth_config import authomatic

app = Flask(__name__)


@app.route("/")
def index():
    """Landing page for our oauth test with hyperlinks to each oauth test"""
    return """
    <p><a href="/users/facebook_oauth">Go to Facebook</a></p>
    <p><a href="/users/google_oauth">Go to Google</a></p>
    <p><a href="/users/github_oauth">Go to GitHub</a></p>
    """


@app.route("/users/facebook_oauth")
def facebook_oauth():
    """Ask for Facebook Oauth data"""
    return oauth_generalized("Facebook")


@app.route("/users/google_oauth")
def google_oauth():
    """Ask for Google Oauth data"""
    return oauth_generalized("Google")


@app.route("/users/github_oauth")
def github_oauth():
    """Ask for GitHub Oauth data"""
    return oauth_generalized("GitHub")


def oauth_generalized(oauth_client):
    """Generalized oauth data retrieval"""
    # Get response object for the WerkzeugAdapter.
    response = make_response()
    # Log the user in, pass it the adapter and the provider name.
    result = authomatic.login(WerkzeugAdapter(request, response), oauth_client)
    # If there is no LoginResult object, the login procedure is still pending.
    if not result:
        return response
    # If there is no result.user something went wrong
    if not result.user:
        return "Failed to retrieve oauth user"

    # Update user to retrieve data
    result.user.update()

    # Return a dictionary containing the user data
    # Flask automatically converts the dictionary to JSON
    return result.user.data


if __name__ == "__main__":
    # Initiate app
    app.run()
