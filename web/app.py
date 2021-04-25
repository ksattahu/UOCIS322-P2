"""
Kale Satta-Hutton's Flask API.
"""

from flask import Flask, render_template, send_from_directory, abort

app = Flask(__name__)

@app.route("/<path:fpath>")
def request(fpath):
    if "~" in fpath:
        abort(403)
    elif "//" in fpath:
        abort(403)
    elif ".." in fpath:
        abort(403)
    return send_from_directory("pages", fpath)

@app.errorhandler(404)
def not_found(error):
    return send_from_directory("pages", "404.html"), 404

@app.errorhandler(403)
def forbidden(error):
    return send_from_directory("pages", "403.html"), 403


if __name__ == "__main__":
    app.run(debug=True,
            host='0.0.0.0')
