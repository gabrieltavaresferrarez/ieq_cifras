from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

from ieq_cifras.models import User

class NewBandForm(FlaskForm):
    name = StringField(
        'Band Name',
        validators=[
            DataRequired(),
            Length(min=2, max=30)
        ]
    )

    submit = SubmitField('Create Band')

