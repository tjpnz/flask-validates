# Flask-Validates

[![Build Status](https://travis-ci.org/tjpnz/flask-validates.svg?branch=master)](https://travis-ci.org/tjpnz/flask-validates)

Painless form validation (WTForms or Flask-WTF) using view decorators.

## Quickstart

Most interaction with Flask-Validates is through `validates` for decorating views and `current_form` for getting a reference to the form bound to the given route. The following example demonstrates a simple use of the `validates` decorator which validates a form with two fields:


```python
@app.route("/", methods=["GET", "POST"])
    @validates(
        email_address=StringField("Email", validators=[DataRequired(), Email()]),
        query=TextAreaField("Query", validators=[DataRequired()])
    )
    def index():
        if request.method == "POST" and current_form.validate():
            flash("Your feedback has been submitted")
            return redirect(url_for("index"))
        return render_template("contact_form.html.j2", form=current_form)
```

More examples can be found in the `examples` directory.

### Flask-WTF Support

`Flask-Validates` can be used with `Flask-WTF` (and indeed any WTForms integration) by initializing the `Flask-Validates` extension with the `FlaskForm` form class:

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
