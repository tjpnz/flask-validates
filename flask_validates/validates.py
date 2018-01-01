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
        """Initializes FlaskValidates with given ``app``.

        The default form class used by FlaskValidates can be overridden by
        specifying ``form_cls``.
        """
        app.config["FLASK_VALIDATES_FORM_CLASS"] = form_cls


def validates(form_cls=None, **fields):
    """Adds form validation to a Flask view.

    ``form_cls`` specifies the base class on which validation is performed
    including any fields that might be present. If ``form_cls`` is not
    specified it defaults to :class:`wtforms.Form` or the form class
    passed to :class:`~flask_validates.FlaskValidates` if set.


    ``fields`` specifies the fields that are to be added to ``form_cls``.
    """
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
