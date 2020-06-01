"""Globals

Global variables and objects to import into other modules.
Kept separate to avoid inifinite import loops.
"""
import os

from flask_login import LoginManager
from flask_mongoengine import MongoEngine

# Paths
ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

# Database setup
db = MongoEngine()

# Login manager setup
login_manager = LoginManager()
