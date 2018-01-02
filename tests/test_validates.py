from flask import json


def test_form_cls_form_validation(app_with_form_cls_form, client):
    resp = client.post("/")
    assert resp.status_code == 400
    assert json.loads(resp.data) == dict(field_one=None, field_two=None)

    resp = client.post("/", data=dict(field_one="foo", field_two="bar"))
    assert resp.status_code == 200
    assert json.loads(resp.data) == dict(field_one="foo", field_two="bar")


def test_kwargs_form_validation(app_with_kwargs_form, client):
    resp = client.post("/")
    assert resp.status_code == 400
    assert json.loads(resp.data) == dict(field_one=None, field_two=None)

    resp = client.post("/", data=dict(field_one="foo", field_two="bar"))
    assert resp.status_code == 200
    assert json.loads(resp.data) == dict(field_one="foo", field_two="bar")


def test_composite_form_validation(app_with_composite_form, client):
    resp = client.post("/")
    assert resp.status_code == 400
    assert json.loads(resp.data) == dict(field_one=None, field_two=None)

    resp = client.post("/", data=dict(field_one="foo", field_two="bar"))
    assert resp.status_code == 200
    assert json.loads(resp.data) == dict(field_one="foo", field_two="bar")


def test_form_validation_with_json_data(app_with_kwargs_form, client):
    resp = client.post("/",
                       data=json.dumps(dict(field_one="foo", field_two="bar")),
                       content_type="application/json")
    assert resp.status_code == 200
    assert json.loads(resp.data) == dict(field_one="foo", field_two="bar")
