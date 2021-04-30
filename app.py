# bibliotecas para la aplicacion, formularios y control de sesiones
from flask import Flask, render_template, url_for, flash, redirect, request
from flask_bootstrap import Bootstrap
from formularios import *
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
# bibliotecas para el descubrimiento de la red
#from module_scan import os, scan_by_interface
#from topologia import Topologia
#from discover import maqueta_conexiones

app = Flask(__name__)
app.config['SECRET_KEY'] = 'EstaCosaDeberiaSerSecreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'inicio_sesion'

# definicion de la base de datos
db = SQLAlchemy(app)

class Usuario(UserMixin, db.Model):
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        usuario = db.Column(db.String(80), unique=True)
        email = db.Column(db.String(15), unique=True)
        nombre = db.Column(db.String(150))
        contrasenia = db.Column(db.String(80))

db.create_all()

# definicion de las rutas de cada pagina y su comportamiento

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inicio_sesion',methods=['GET','POST'])
def inicio_sesion():
    formulario = formulario_inicio_sesion()
    if formulario.validate_on_submit():
        usuario = Usuario.query.filter_by(usuario=formulario.usuario.data).first()
        if usuario:
            if check_password_hash(usuario.contrasenia, formulario.contrasenia.data):
                login_user(usuario, remember=formulario.recuerdame.data)
                return redirect(url_for('panel_control'))
        return "usuario o contraseña invalidos"
    return render_template('inicio_sesion.html', formulario=formulario)

@app.route('/registro', methods=['GET','POST'])
def registro():
    formulario = formulario_registro()
    if formulario.validate_on_submit():
        hash_pass = generate_password_hash(formulario.contrasenia.data, method='sha256') 
        nuevo_usuario = Usuario(
            usuario=formulario.usuario.data,
            email=formulario.email.data,
            nombre=formulario.nombre.data,
            contrasenia=hash_pass
        )
        db.session.add(nuevo_usuario)
        db.session.commit()
        return "Nuevo usuario creado"

    return render_template('registro.html', formulario=formulario)

@app.route('/panel_control', methods=['GET','POST'])
@login_required
def panel_control():
    return render_template('panel_control.html')

@app.route('/configura_router/<string:router_name>', methods=['GET','POST'])
@login_required
def configura_router(router_name):
    return render_template('configura_router.html',router_name=router_name)

@app.route('/cerrar_sesion')
@login_required
def cerrar_sesion():
    logout_user()
    return redirect(url_for('index'))

#def home():
    '''# descubrimiento y visualizacion de topologia
    # Listamos las interfaces de red aqui
    interfaces=os.listdir("/sys/class/net/")
    # Modulo que permite escanear todos los datos
    recibidos, conexiones_pc = scan_by_interface('enp0s3',"admin","admin01","1234")
    maquetado = maqueta_conexiones(recibidos,conexiones_pc)
    print('----------Conexiones encontradas de la siguiente manera-----------------')
    print(maquetado)
    topo = Topologia(maquetado, "templates")
    topo.print_rep_html_flask()'''
    
 #   return render_template('inicio.html')

#@app.route('/info')
#def about():
#    return render_template('info.html')'''


if __name__ == '__main__':
    app.run(debug=True)


# crear base de datos
# sqlite3 app.db
# .tables
# .exit

# from app import db