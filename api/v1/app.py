#!/usr/bin/python3
'''app for registering blueprint and starting flask'''
from flask import Flask, make_response, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
cors = CORS(app, resources={'/*': {'origins': '0.0.0.0'}})
app.register_blueprint(app_views, url_prefix="/api/v1")
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.teardown_appcontext
def tear_down(self):
    """close query after each session"""
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """Returns a JSON-formatted error response"""
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    app.run(host=getenv("HBNB_API_HOST", "0.0.0.0"),
            port=int(getenv("HBNB_API_PORT", "5000")), threaded=True)
