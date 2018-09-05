from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SapForm(FlaskForm):
    material = StringField('Material',validators=[DataRequired()])
    plotstruc = SubmitField('Plot/Doc Structure')
    mbom = SubmitField('Material BOM')

class IWForm(FlaskForm)
    project = StringField('Project', validators = [DataRequired()})
