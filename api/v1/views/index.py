#!/usr/bin/python3
""" returns json statuses for app_views routes  """
from api.v1.views import app_views
from flask import jsonify
from models import storage

@app_views.route("/status")
def status():
    """return JSON of OK status"""
    return jsonify({'status': 'OK'})
