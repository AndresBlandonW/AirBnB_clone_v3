#!/usr/bin/python3
"""index file"""
from flask import Flask, jsonify
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def status_route():
    """Return a JSON status"""
    return jsonify({'status': 'OK'})
