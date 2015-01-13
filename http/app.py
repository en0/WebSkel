#!/usr/bin/env python

from flask import Flask, render_template, abort
from jinja2.exceptions import TemplateNotFound

from flask.ext.restful import Api, Resource

app = Flask(__name__)
api = Api(app)

@app.route('/')
@app.route('/<path:path>')
def webclient(path="index.html"):
    """ Default route.

    This is a catch all. It is locked to the /templates directory.

    Arguments:
        path - The path to the file relative to the /templates directory

    Returns:
        Response Object
    """
    try:
        return render_template(path)
    except TemplateNotFound:
        abort(404)


class ExampleAPI(Resource):
    """ Example of an API request handler. """
    def get(self):
        return {
            "Message": "Example API",
        }

api.add_resource(ExampleAPI, "/api/test")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
