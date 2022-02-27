from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

# users first and last names must be between 2 and 15 characters
# forms will make sure all fields are filled out, and remind the user if not
class NewUserForm(FlaskForm):
    firstName = StringField('First Name', validators=[DataRequired(), Length(min=2, max=15)])
    lastName = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=15)])
    idNum = StringField('ID', validators=[DataRequired()])
    points = StringField('Points', validators=[DataRequired()])

    submit = SubmitField('Add User')

class UpdateUserForm(FlaskForm):
    firstName = StringField('First Name', validators=[Length(min=2, max=15)])
    lastName = StringField('Last Name', validators=[Length(min=2, max=15)])
    points = StringField('Points')

    submit = SubmitField('Update User')