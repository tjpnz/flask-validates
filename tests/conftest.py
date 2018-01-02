import pytest
from flask import Flask, jsonify
from flask_wtf import FlaskForm
from wtforms import Form
from wtforms import StringField
from wtforms.validators import DataRequired

from flask_validates.validates import build_form_class, current_form, validates, FlaskValidates


@pytest.fixture
def form():
    class TestForm(Form):
        field_one = StringField()
        field_two = StringField()

    form_cls = build_form_class(TestForm)
    return form_cls()


@pytest.fixture
def app():
    return Flask(__name__)


@pytest.fixture
def app_with_form_cls_form(app):
    class FormCls(Form):
        field_one = StringField(validators=[DataRequired()])
        field_two = StringField(validators=[DataRequired()])

    @app.route("/", methods=["POST"])
    @validates(FormCls)
    def index():
        current_form.validate()
        return jsonify(current_form.data)

    return app


@pytest.fixture
def app_with_kwargs_form(app):
    @app.route("/", methods=["POST"])
    @validates(field_one=StringField(validators=[DataRequired()]),
               field_two=StringField(validators=[DataRequired()]))
    def index():
        current_form.validate()
        return jsonify(current_form.data)

    return app


@pytest.fixture
def app_with_composite_form(app):
    class FormCls(Form):
        field_one = StringField(validators=[DataRequired()])

    @app.route("/", methods=["POST"])
    @validates(FormCls, field_two=StringField(validators=[DataRequired()]))
    def index():
        current_form.validate()
        return jsonify(current_form.data)

    return app


@pytest.fixture
def app_with_flask_wtf_based_form(app_with_kwargs_form):
    app_with_kwargs_form.secret_key = "supersecret"
    app_with_kwargs_form.config["WTF_CSRF_ENABLED"] = False
    FlaskValidates(app_with_kwargs_form, FlaskForm)
    return app_with_kwargs_form


@pytest.fixture
def client(app):
    return app.test_client()
