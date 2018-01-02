from wtforms import Form
from wtforms import StringField

from flask_validates.validates import build_form_class
from tests import FlaskValidatesTestCase


class TestPopulate(FlaskValidatesTestCase):
    def test_populate(self):
        class TestForm(Form):
            field_one = StringField()
            field_two = StringField()

        class TestObject(object):
            field_one = "foo"
            field_two = "bar"

        form_cls = build_form_class(TestForm)
        form = form_cls()
        form.populate(obj=TestObject())

        self.assertEqual(form.field_one.data, "foo")
        self.assertEqual(form.field_two.data, "bar")
