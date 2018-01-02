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


class PopulateMixin(object):
    def populate(self, obj=None, data=None, **kwargs):
        """Populates form with the given values and returns the form instance.

        If ``obj`` is provided it is checked for attributes matching form field
        names, which will be used for form field values.

        ``data`` accepts a dictionary of data and is only used if ``obj`` is not
        present.

        ``**kwargs`` accepts arbitrary values for attributes not found on ``obj``.
        """
        return self.process(obj=obj, data=data, **kwargs)


def build_form_class(form_cls, **fields):
    return type("_Form", (form_cls, PopulateMixin,), fields)


def get_form_data():
    if request.form:
        return request.form
    if request.get_json():
        return ImmutableMultiDict(request.get_json())


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
            nonlocal form_cls

            ctx = stack.top
            if ctx is None:
                return f(*args, **kwargs)

            # Determine the default form class if not provided
            if form_cls is None:
                form_cls = current_app.config.get("FLASK_VALIDATES_FORM_CLASS", Form)

            cls = build_form_class(form_cls, **fields)
            ctx.current_form = cls(get_form_data())

            resp = f(*args, **kwargs)
            if isinstance(resp, (Response, str,)) and ctx.current_form.errors:
                return resp, 400,
            else:
                return resp

        return decorated_function
    return decorator


current_form = LocalProxy(lambda: getattr(stack.top, "current_form", None))
