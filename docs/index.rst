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

Flask-Validates binds forms to views using the :func:`~flask_validates.validates` decorator, depending on how you use it Flask-Validates can eliminate the need entirely to create explicit form classes. When a view is invoked :func:`~flask_validates.validates` creates a form behind the scenes based on the fields you provide which is then exposed to the view via :data:`~flask_validates.current_form` which works in a similar manner to Flask's :data:`flask.current_app`.

Alongside creating forms :func:`~flask_validates.validates` also sets the appropriate HTTP 400 response code if form validation fails.

The following example demonstrates using :func:`~flask_validates.validates` to validate three form fields:

.. code-block:: python
   :emphasize-lines: 4-8

   from flask_validates import current_form, validates

   @app.route("/register", methods=["GET", "POST"])
   @validates(
       first_name=StringField(validators=[DataRequired()],
       last_name=StringField(validators=[DataRequired()],
       email=StringField(validators=[DataRequired, Email()]
   )
   def register():
       if request.method == "POST" and current_form.validate():
           create_user()
           return redirect(url_for("index"))
       return render_template("register.html.j2")

It's also possible to use existing forms with :func:`~flask_validates.validates` as is happening in the following example:

.. code-block:: python
   :emphasize-lines: 9

   from flask_validates import current_form, validates

   class RegistrationForm(Form):
       first_name = StringField(validators=[DataRequired()]
       last_name = StringField(validators=[DataRequired()]
       email = StringField(validators=[DataRequired, Email()]

   @app.route("/register", methods=["GET", "POST"])
   @validates(RegistrationForm)
   def register():
       if request.method == "POST" and current_form.validate():
           create_user()
           return redirect(url_for("index"))
       return render_template("register.html.j2")

In some cases you might want to add additional fields to a more generic form. The :func:`~flask_validates.validates` decorator supports this by allowing both a form class and fields to be specified at the same time:

.. code-block:: python
   :emphasize-lines: 9

   from flask_validates import current_form, validates

   class SimpleRegistrationForm(Form):
       first_name = StringField(validators=[DataRequired()]
       last_name = StringField(validators=[DataRequired()]
       email = StringField(validators=[DataRequired, Email()]

   @app.route("/register", methods=["GET", "POST"])
   @validates(SimpleRegistrationForm, captcha=Captcha())
   def register():
       if request.method == "POST" and current_form.validate():
           create_user()
           return redirect(url_for("index"))
       return render_template("register.html.j2")

Populating form objects
~~~~~~~~~~~~~~~~~~~~~~~

Quite often you'll want to populate an existing form with your own data, for instance when rendering a form for an edit page. With WTForms this can be done by passing an object to the form constructor. In Flask-Validates the same behaviour can be achieved by calling :meth:`~flask_validates.validates.PopulateMixin.populate` on :data:`~flask_validates.current_form` as is done in the following example:

.. code-block:: python
   :emphasize-lines: 10-11

   from flask_validates import current_form, validates

   @app.route("/items/<id>/edit", methods=["GET", "POST"])
   @validates(ItemForm)
   def edit(id):
       item = get_item(id)
       if request.method == "POST" and current_form.validate():
           update_item()
           return redirect(url_for("index"))
       return render_template("edit_item.html.j2",
                              form=current_form.populate(item))


Usage with Flask-WTF
~~~~~~~~~~~~~~~~~~~~

Flask-WTF is a popular extension that makes working with Flask and WTForms a bit nicer. Flask-Validates can be configured to work with Flask-WTF as follows:

.. code-block:: python
   :emphasize-lines: 5

   from flask_wtf import FlaskForm
   from flask_validates import FlaskValidates

   app = Flask(__name__)
   FlaskValidates(app, FlaskForm)

API
---

.. autoclass:: flask_validates.FlaskValidates
    :members:

.. data:: flask_validates.current_form

   Points to the form created by :func:`~flask_validates.validates`.

.. autofunction:: flask_validates.validates

.. autoclass:: flask_validates.validates.PopulateMixin
    :members:

