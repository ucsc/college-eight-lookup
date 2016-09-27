from flask_wtf import Form
from wtforms import SelectField
from wtforms.validators import DataRequired


class SubdomainForm(Form):
    subdomain = SelectField(u'Subdomain', validators=[DataRequired()])