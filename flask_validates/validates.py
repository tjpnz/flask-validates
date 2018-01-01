from functools import wraps

from flask import Response
from flask import current_app
from flask import request
try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack
from werkzeug.datastructures import ImmutableMultiDict
from werkzeug.local import LocalProxy
from wtforms import Form


class FlaskValidates(object):
    def __init__(self, app=None, form_cls=None):
        self.app = app
        if app is not None:
            self.init_app(app, form_cls)

    def init_app(self, app, form_cls=None):
        app.config["FLASK_VALIDATES_FORM_CLASS"] = form_cls


def validates(form_cls=None, **fields):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            ctx = stack.top
            if ctx is not None:
                ctx.current_form = _make_form(form_cls, fields)
            resp = f(*args, **kwargs)
            if isinstance(resp, (Response, str,)) and ctx.current_form.errors:
                return resp, 400,
            else:
                return resp
        return decorated_function
    return decorator


def _make_form(form_cls, fields):
    if form_cls is None:
        form_cls = current_app.config.get("FLASK_VALIDATES_FORM_CLASS", Form)
    form = type("_Form", (form_cls,), fields)
    return form(_get_form_data())


def _get_form_data():
    if request.form:
        return request.form
    if request.get_json():
        return ImmutableMultiDict(request.get_json())


def _current_form():
    ctx = stack.top
    if not hasattr(ctx, "current_form"):
        return None
    else:
        return ctx.current_form


current_form = LocalProxy(_current_form)
