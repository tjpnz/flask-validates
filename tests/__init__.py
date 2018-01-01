import unittest

from flask import Flask
from flask import jsonify

from flask_validates import current_form
from flask_validates import validates


class FlaskValidatesTestCase(unittest.TestCase):

    def make_test_app(self, form_cls, **fields):
        app = Flask(__name__)

        @app.route("/", methods=["POST"])
        @validates(form_cls, **fields)
        def index():
            current_form.validate()
            return jsonify(current_form.data)

        return app
