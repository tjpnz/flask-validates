from flask import json


def test_flask_wtf_based_form_validation(app_with_flask_wtf_based_form, client):
    resp = client.post("/")
    assert resp.status_code == 400
    assert json.loads(resp.data) == dict(field_one=None, field_two=None)

    resp = client.post("/", data=dict(field_one="foo", field_two="bar"))
    assert resp.status_code == 200
    assert json.loads(resp.data) == dict(field_one="foo", field_two="bar")
