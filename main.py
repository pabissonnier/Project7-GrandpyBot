from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class QuestionForm(FlaskForm):
    question = StringField('Question', validators=[DataRequired(), Length(min=2, max=250)])
