#!/usr/bin/python3
"""Initialize Blueprint views"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/app_server/v1")

from app_server.v1.views.view1 import *
from app_server.v1.views.view2 import *
from app_server.v1.views.view3 import *
