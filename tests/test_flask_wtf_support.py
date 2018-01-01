from flask import json
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

from flask_validates import FlaskValidates
from tests import FlaskValidatesTestCase


class TestFlaskWtfSupport(FlaskValidatesTestCase):

    def setUp(self):
        self.make_test_app(
            field_one=StringField(validators=[DataRequired()]),
            field_two=StringField(validators=[DataRequired()]))

        self.app.secret_key = "supersecret"
        self.app.config["WTF_CSRF_ENABLED"] = False

        FlaskValidates(self.app, FlaskForm)

    def test_for_invalid_input(self):
        resp = self.client.post("/")
        json_data = json.loads(resp.data)

        self.assertEqual(resp.status_code, 400)
        self.assertIsNone(json_data["field_one"])
        self.assertIsNone(json_data["field_two"])

    def test_for_valid_input(self):
        resp = self.client.post(
            "/",
            data=dict(field_one="foo", field_two="bar"))
        json_data = json.loads(resp.data)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(json_data["field_one"], "foo")
        self.assertEqual(json_data["field_two"], "bar")
