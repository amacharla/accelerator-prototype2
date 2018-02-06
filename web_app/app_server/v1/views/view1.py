#!/usr/bin/python3
"""View 1 Routes"""

from flask import Flask, Blueprint, jsonify
from app_server.v1.views import app_views

@app_views.route('/1')
def hello_view_1():
        """placeholder for view 1"""
        return jsonify({"View 1": "OKAY"})
