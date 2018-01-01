Flask-Validates
===============

Painless form validation using view decorators.

Installation
------------

Using pip:

.. code-block:: sh

   pip install Flask-Validates

Usage
-----

Flask-Validates binds forms to views using the :func:`~validates` decorator, depending on how you use it Flask-Validates can eliminate the need entirely to create explicit form classes. When a view is invoked :func:`~validates` creates a form behind the scenes based on the fields you provide which is then exposed to the view via :data:`current_form` which works in a similar manner to Flask's :data:`flask.current_app`.

Alongside creating forms :func:`~validates` also sets the appropriate HTTP 400 response code if form validation fails.

.. code-block:: python

   from flask_validates import current_form, validates

   @validates(
       first_name=StringField(validators=[DataRequired()],
       last_name=StringField(validators=[DataRequired()],
       email=StringField(validators=[DataRequired, Email()]
   )
   @app.route("/register", methods=["GET", "POST"])
   def register():
       if request.method == "POST" and current_form.validate():
           create_user()
           return redirect(url_for("index"))
       return render_template("register.html.j2")

It's also possible to use existing forms with :func:`~validates` as is happening in the following example:

.. code-block:: python

   from flask_validates import current_form, validates

   class RegistrationForm(Form):
       first_name = StringField(validators=[DataRequired()]
       last_name = StringField(validators=[DataRequired()]
       email = StringField(validators=[DataRequired, Email()]

   @validates(RegistrationForm)
   @app.route("/register", methods=["GET", "POST"])
   def register():
       if request.method == "POST" and current_form.validate():
           create_user()
           return redirect(url_for("index"))
       return render_template("register.html.j2")

In some cases you might want to add additional fields to a more generic form. The :func:`~validates` decorator supports this by allowing both a form class and fields to be specified at the same time:

.. code-block:: python

   from flask_validates import current_form, validates

   class SimpleRegistrationForm(Form):
       first_name = StringField(validators=[DataRequired()]
       last_name = StringField(validators=[DataRequired()]
       email = StringField(validators=[DataRequired, Email()]


   @validates(SimpleRegistrationForm, captcha=Captcha())
   @app.route("/register", methods=["GET", "POST"])
   def register():
       if request.method == "POST" and current_form.validate():
           create_user()
           return redirect(url_for("index"))
       return render_template("register.html.j2")

Usage with Flask-WTF
~~~~~~~~~~~~~~~~~~~~

Flask-WTF is a popular extension that makes working with Flask and WTForms a bit nicer. Flask-Validates can be configured to work with Flask-WTF as follows:

.. code-block:: python

   from flask_wtf import FlaskForm
   from flask_validates import FlaskValidates

   app = Flask(__name__)
   FlaskValidates(app, FlaskForm)

API
===

.. module:: flask_validates

.. autoclass:: FlaskValidates
    :members:

.. data:: current_form

   Points to the form created by :func:`~validates`.

.. autofunction:: validates