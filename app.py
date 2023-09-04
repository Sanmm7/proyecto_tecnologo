from flask_sqlalchemy import SQLAlchemy
from flask import Flask, flash, render_template, request, redirect, session, url_for
from flask_migrate import Migrate
from database import db
from models import Usuario
app = Flask(__name__)
app.config['SECRET_KEY'] = '1034516961Sa'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3306/proyectoweb'
db.init_app(app)

migrate = Migrate(app,db)

# Define los modelos de datos aquí
# class Usuario(db.Model):
#     ...

@app.route('/')
def index():
    # Ejemplo de vista para la página principal
    return render_template('index.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        edad = request.form['edad']
        tel = request.form['tel']
        n_documento = request.form['n_documento']
        t_documento = request.form['t_documento']
        email = request.form['email']
        dirrecion = request.form['dirrecion']
        contra = request.form['contra']

        nuevo_usuario = Usuario(nombre=nombre, apellidos=apellidos, edad=edad, tel=tel, n_documento=n_documento, t_Documento=t_documento, email=email, dirrecion=dirrecion, contra=contra)
        db.session.add(nuevo_usuario)
        db.session.commit()

        # Redireccionar a la página de inicio después de registrar el usuario
        return render_template('indexalert.html')
    
    # Si la solicitud es GET, simplemente renderiza el formulario de registro
    return render_template('formregistro.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['username']
        contra = request.form['password']
        user = Usuario.query.filter_by(email=email, contra=contra).first()
        if user:
            session['user_id'] = user.id_u
            session['tipo_usuario'] = user.rol
            flash('Inicio de sesión exitoso!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Nombre de usuario o contraseña incorrectos', 'danger')
    return render_template('contramal.html')

@app.route('/dashboard')
def dashboard():
    
    user_id = session.get('user_id')
    tipo_usuario = session.get('tipo_usuario')
    if user_id:
        user = Usuario.query.get(user_id),Usuario.query.get(tipo_usuario)
        if tipo_usuario=='admin':
        
          return render_template('PrincipalAdmin.html', user=user)
        elif tipo_usuario=='pac':
             return render_template('PrincipalResidente.html', user=user)
        elif tipo_usuario=='doctor':
            return render_template('PrincipalVigilante.html',user=user)
    else:
     flash('Debes iniciar sesión para acceder al dashboard', 'warning')
     return render_template('index.html')
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Has cerrado sesión exitosamente', 'info')
    return render_template('secion.html')
       

if __name__ == '__main__':
    app.run(debug=True)
