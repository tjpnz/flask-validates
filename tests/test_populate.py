from unittest.mock import Mock


def test_populate(form):
    form = form.populate(Mock(field_one="foo", field_two="bar"))
    assert form.field_one.data == "foo"
    assert form.field_two.data == "bar"
