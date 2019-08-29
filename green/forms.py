
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired(), length(min = 2, max = 15)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators= [DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    Username = StringField('Username', validators = [DataRequired(), length(min = 2, max = 15)])
    password = PassWordField('Password', validators = [DataRequired()])
    submit = SubmitField('Login in')


