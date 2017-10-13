from wtforms import Form, StringField, TextAreaField, PasswordField, BooleanField, validators

class RegisterForm(Form):
    # name = StringField('Name', [validators.Length(min=1, max=50)])
    # username = StringField('Username', [validators.Length(min=4, max=25)])
    # email = StringField('Email', [validators.Length(min=6, max=50)])
    # password = PasswordField('Password', [
    #     validators.DataRequired(),
    #     validators.EqualTo('confirm', message="Passwords do not match")
    # ])
    # confirm = PasswordField('Confirm Password')
    educationalEstablishmentName = StringField('Establishment Name: ', [validators.Length(min=5, max=150)])
    registereeStreetAddress= StringField('Registeree\'s Street Address: ', [validators.Length(min=5, max=150)])
    registereeCity = StringField('Registeree\'s City: ', [validators.Length(min=5, max=100)])
    registereePostcode = StringField('Registeree\'s Post Code: ', [validators.Length(min=5, max=10)])
    registereeTelephoneNum = StringField('Registeree\'s Telephone Number: ', [validators.Length(min=9, max=12)])
    registereeMobileNum = StringField('Registeree\'s Mobile Number: ', [validators.Length(min=9, max=12)])
    courseNumber = StringField('Course Number: ', [validators.Length(min=5, max=6)])
    courseTitle = StringField('Course Title: ', [validators.Length(min=5, max=150)])
    # isPrerequisiteMet = RadioField('Are course prerequisites met?: ', choices=[('True', 'Yes'), ('False', 'No')])
    # isEnrollmentUndergone = RadioField('Have you undergone enrollment?: ', choices=[('True', 'Yes'), ('False', 'No')])
    # isFinalCoursePriorToGraduation = RadioField('Is this your final year prior to graduating?: ', choices=[('True', 'Yes'), ('False', 'No')])
    # isFirstCourse = RadioField('Is this your first course with us?: ', choices=[('True', 'Yes'), ('False', 'No')])
    # isEligibleForFinance = RadioField('Are you eligible for financial aid?: ', choices=[('True', 'Yes'), ('False', 'No')])
    isPrerequisiteMet = BooleanField(
        label='Are course prerequisites met?: ',
        validators=[],
        default=False,
        description='prerequisites'
        )
    isEnrollmentUndergone = BooleanField(
        label='Have you undergone enrollment?: ',
        validators=[],
        default=False,
        description='enrollment'
        )
    isFinalCoursePriorToGraduation = BooleanField(
        label='Is this your final year prior to graduating?: ',
        validators=[],
        default=False,
        description='prior to graduating'
        )
    isFirstCourse = BooleanField(
        label='Is this your first course with us?: ',
        validators=[],
        default=False,
        description='first course with establishment'
    )
    isEligibleForFinance = BooleanField(
        label='Are you eligible for financial aid?: ',
        validators=[],
        default=False,
        description='first course with establishment'
    )
