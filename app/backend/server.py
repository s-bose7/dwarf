
import re

from typing import Dict, Any
from flask import Flask, request, jsonify, Response, redirect
from . services.dwarf import Dwarf 


app = Flask(__name__)
host = "localhost"
port = 5000


@app.route("/dwarf-home", methods=["GET"])
def dwarf_home()->str:
    return "Welcome to dwarf backend"


def verify_url_pattern(url: str)->bool:
    url_pattern = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return bool(re.match(url_pattern, url))



@app.route("/shorten", methods=["POST"])
def shorten()->Response:
    long_url = request.json["url"]
    valid_url = verify_url_pattern(long_url)
    if not valid_url:
        return jsonify({
            "status_code": 422,
            "message": "Unprocessable Content",
            "long_url": long_url
        })
    
    short_url = Dwarf.shorten(url=long_url) 
    # API response
    response: Dict[str, Any] = {
        "status_code": 200,
        "short_url": short_url, 
        "long_url": long_url,
    }
    return jsonify(response)


@app.route("/<identifier>", methods=["GET"])
def redirect_to_original(identifier: str)->Response:
    original_url: str = Dwarf.decode(identifier)
    if original_url == "":
        return jsonify({
            "status_code": 404,
            "message": "Not Found"
        })
    # Asset found, redirecting...
    return redirect(original_url)