from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length

class formulario_inicio_sesion(FlaskForm):
    usuario = StringField('usuario', validators=[InputRequired(),Length(4,15)])
    contrasenia  = PasswordField('contraseña', validators=[InputRequired(),Length(4,80)])
    recuerdame = BooleanField('recuerdame')

class formulario_registro(FlaskForm):
    email = StringField('correo electronico', validators=[InputRequired(), Email(message='correo invalido'),Length(4,80)])
    nombre = StringField('nombre completo', validators=[InputRequired(),Length(4,150)])
    usuario = StringField('usuario', validators=[InputRequired(),Length(4,15)])
    contrasenia  = PasswordField('contraseña', validators=[InputRequired(),Length(4,80)])