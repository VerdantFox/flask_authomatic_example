"""app.py

This is the main file called to run the flask application
"""
from root.factory import create_app

if __name__ == "__main__":

    app = create_app()
    app.run()
