from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class MaterialForm(FlaskForm):
    material = StringField('Material', validators=[DataRequired()])
    go = SubmitField('Go!')
