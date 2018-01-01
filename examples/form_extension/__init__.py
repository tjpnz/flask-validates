from flask import Flask
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from flask_validates import current_form
from flask_validates import validates
from wtforms import BooleanField
from wtforms import Form
from wtforms import StringField
from wtforms import TextAreaField
from wtforms.validators import DataRequired
from wtforms.validators import Email


class SimpleFeedbackForm(Form):
    email_address = StringField(validators=[DataRequired(), Email()])
    comments = TextAreaField(validators=[DataRequired()])


def create_app():
    app = Flask(__name__)
    app.secret_key = "supersecret"

    @app.route("/", methods=["GET", "POST"])
    @validates(SimpleFeedbackForm, requires_followup=BooleanField())
    def index():
        if request.method == "POST" and current_form.validate():
            flash("Your feedback has been submitted")
            return redirect(url_for("index"))
        return render_template("contact_form.html.j2", form=current_form)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
