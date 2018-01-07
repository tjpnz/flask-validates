def test_populate(form):
    class Mock(object):
        field_one = "foo"
        field_two = "bar"

    form = form.populate(Mock())
    assert form.field_one.data == "foo"
    assert form.field_two.data == "bar"
