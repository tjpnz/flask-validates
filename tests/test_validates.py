from flask import json
from wtforms import StringField, Form
from wtforms.validators import DataRequired

from flask_validates import FlaskValidates
from tests import FlaskValidatesTestCase


class TestValidatesSimpleForms(FlaskValidatesTestCase):

    def setUp(self):
        self.app = self.make_test_app(
            None,
            field_one=StringField(validators=[DataRequired()]),
            field_two=StringField(validators=[DataRequired()]))

    def test_for_invalid_input(self):
        with self.app.test_client() as client:
            resp = client.post("/")
            json_data = json.loads(resp.data)

            self.assertEqual(resp.status_code, 400)
            self.assertIsNone(json_data["field_one"])
            self.assertIsNone(json_data["field_two"])

    def test_for_valid_input(self):
        with self.app.test_client() as client:
            resp = client.post("/", data=dict(
                field_one="foo",
                field_two="bar"))
            json_data = json.loads(resp.data)

            self.assertEqual(resp.status_code, 200)
            self.assertEqual(json_data["field_one"], "foo")
            self.assertEqual(json_data["field_two"], "bar")


class TestValidatesCompositeForms(FlaskValidatesTestCase):

    def setUp(self):
        class TestForm(Form):
            field_one = StringField(validators=[DataRequired()])
            field_two = StringField(validators=[DataRequired()])

        self.app = self.make_test_app(
            TestForm,
            additional_field=StringField(validators=[DataRequired()]))

    def test_for_invalid_input(self):
        with self.app.test_client() as client:
            resp = client.post("/")
            json_data = json.loads(resp.data)

            self.assertEqual(resp.status_code, 400)
            self.assertIsNone(json_data["field_one"])
            self.assertIsNone(json_data["field_two"])
            self.assertIsNone(json_data["additional_field"])

    def test_for_valid_input(self):
        with self.app.test_client() as client:
            resp = client.post("/", data=dict(
                field_one="foo",
                field_two="bar",
                additional_field="baz"))
            json_data = json.loads(resp.data)

            self.assertEqual(resp.status_code, 200)
            self.assertEqual(json_data["field_one"], "foo")
            self.assertEqual(json_data["field_two"], "bar")
            self.assertEqual(json_data["additional_field"], "baz")


class TestValidatesCustomFormClass(FlaskValidatesTestCase):

    def setUp(self):
        self.app = self.make_test_app(
            None,
            field_one=StringField(validators=[DataRequired()]),
            field_two=StringField(validators=[DataRequired()]))

        class CustomFormClass(Form):
            required_field = StringField(validators=[DataRequired()])

        FlaskValidates(self.app, CustomFormClass)

    def test_for_invalid_input(self):
        with self.app.test_client() as client:
            resp = client.post("/")
            json_data = json.loads(resp.data)

            self.assertEqual(resp.status_code, 400)
            self.assertIsNone(json_data["field_one"])
            self.assertIsNone(json_data["field_two"])
            self.assertIsNone(json_data["required_field"])

    def test_for_valid_input(self):
        with self.app.test_client() as client:
            resp = client.post("/", data=dict(
                required_field="foo",
                field_one="bar",
                field_two="baz"))
            json_data = json.loads(resp.data)

            self.assertEqual(resp.status_code, 200)
            self.assertEqual(json_data["required_field"], "foo")
            self.assertEqual(json_data["field_one"], "bar")
            self.assertEqual(json_data["field_two"], "baz")
