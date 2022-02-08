#!/usr/bin/python3
"""index file"""
from flask import Flask, jsonify
from api.v1.views import app_views


@app.route('/status')
def status_route():
    """Return a JSON status"""
    return jsonify({'status': 'OK'})
