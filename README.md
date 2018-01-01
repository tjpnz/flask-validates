# Flask-Validates

[![Build Status](https://travis-ci.org/tjpnz/flask-validates.svg?branch=master)](https://travis-ci.org/tjpnz/flask-validates)

Painless form validation ([WTForms](https://github.com/wtforms/wtforms) or [Flask-WTF](https://github.com/lepture/flask-wtf)) using view decorators.

## Quickstart

Most interaction with Flask-Validates is through `validates` for decorating views and `current_form` for getting a reference to the form bound to the given route. The following example demonstrates a simple use of the `validates` decorator which validates a form with two fields:

```python
@app.route("/", methods=["GET", "POST"])
@validates(
    email=StringField(validators=[DataRequired(), Email()]),
    comments=TextAreaField(validators=[DataRequired()])
)
def index():
    if request.method == "POST" and current_form.validate():
        flash("Your feedback has been submitted")
        return redirect(url_for("index"))
    return render_template("contact_form.html.j2", form=current_form)
```

You can also validate existing forms:

```python
@app.route("/", methods=["GET", "POST"])
@validates(ExistingForm)
def index():
    if request.method == "POST" and current_form.validate():
        flash("Your feedback has been submitted")
        return redirect(url_for("index"))
    return render_template("contact_form.html.j2", form=current_form)
```

If validation fails Flask-Validates appends a `400` status code to the response.

See [examples](examples) for more comprehensive examples of usage.

### Flask-WTF Support

Flask-Validates can be used with [Flask-WTF](https://github.com/lepture/flask-wtf) (and should be compatible with any other WTForms based integration) by initializing the Flask-Validates extension with the FlaskForm class:

```python
FlaskValidates(app, FlaskForm)
```

### Installing

Using pip:

```
pip install Flask-Validates
```

## Running the tests

```
python setup.py test
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
