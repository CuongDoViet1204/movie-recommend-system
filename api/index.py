import pandas as pd

import mysql.connector

import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import pickle

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name')
    if name:
        return jsonify({"message": f"Hello world, {name}"})
    else:
        return jsonify({"error": "Please specify a name in the 'name' query parameter. "}), 400
