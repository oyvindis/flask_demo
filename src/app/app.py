from flask import Flask, jsonify
app = Flask(__name__)
@app.route("/")
def index():
    return jsonify(
        {'company': 'CGI',
         'email': 'mail@cgi.com'
         }
    )