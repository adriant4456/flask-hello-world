from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from app.update import update_folder_list


class ValidName(object):
    def __init__(self, message = None):
        if message is None:
            message = "Folder name can only contain alphanumeric calendars"
        self.message = message
        
    def __call__(self, form, field):
            for i in field.data:
                if ord(i) > 64 and ord(i) < 91:
                    continue
                if ord(i) > 96 and ord(i) < 123:
                    continue
                if ord(i) > 47 and ord(i) < 58:
                    continue
                if ord(i) == 95 or ord(i) == 32:
                    continue
                else:
                    raise ValidationError(self.message)


class SapForm(FlaskForm):
    material = StringField('Material',validators=[DataRequired()])
    plotstruc = SubmitField('Plot/Doc Structure')
    mbom = SubmitField('Material BOM')


class IWForm(FlaskForm):
    project = StringField('Project', validators = [DataRequired(), ValidName()])
    machine = StringField('Machine', validators = [DataRequired(), ValidName()])
    new = SubmitField('Make')

class IWFolderListForm(FlaskForm):
    placeholder  = StringField('placeholder')


