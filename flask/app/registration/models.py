from main import db

class RegistrationDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #userAccountID(db.Integer, db.ForeignKey())
    educationalEstablishmentName = (db.String(150))
    registereeStreetAddress = db.Column(db.String(150))
    registereeCity = db.Column(db.String(100))
    registereePostcode = db.Column(db.String(10))
    registereeTelephoneNum = db.Column(db.Integer())
    registereeMobileNum = db.Column(db.Integer())
    courseNumber = db.Column(db.Integer())
    courseTitle = db.Column(db.String(150))
    isPrerequisiteMet = db.Column(db.Boolean, default=False, nullable=False)
    isEnrollmentUndergone = db.Column(db.Boolean, default=False, nullable=False)
    isFinalCoursePriorToGraduation = db.Column(db.Boolean, default=False, nullable=False)
    isFirstCourse = db.Column(db.Boolean, default=False, nullable=False)
    isEligibleForFinance = db.Column(db.Boolean, default=False, nullable=False)
