from flask import Flask, render_template, request, jsonify, redirect, url_for,flash,session
import requests
from functools import wraps

app = Flask(__name__)
app.secret_key = 'una_clave_secreta_muy_dificil_de_adivinar'


def loginrequired(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario' not in session:
            flash('Inicia sesión para acceder a la página solicitada.', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/')
def home():
    return render_template('login.html')

@app.route('/index')
def index():
    flash('Bienvenido a la aplicación!')
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']

        # Hacer una solicitud GET a json-server
        response = requests.get(f'http://localhost:3000/usuarios?usuario={usuario}&password={password}')

        if response.ok:
            usuarios = response.json()
            if usuarios:  # Si hay al menos un usuario encontrado
                session['usuario'] = usuario  # Almacena el usuario en la sesión
                flash('Inicio de sesión exitoso!')
                return redirect(url_for('dashboard'))
            else:
                flash('Usuario o contraseña incorrectos.')
        else:
            flash('Error en la conexión con el servidor.')

    return render_template('login.html')




@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']

        # Hacer una solicitud POST a json-server
        response = requests.post('http://localhost:3000/usuarios', json={'usuario': usuario, 'password': password})

        if response.status_code == 201:
            flash('Usuario registrado exitosamente!')
            return redirect(url_for('index'))
        else:
            flash('Error al registrar el usuario.')

    return render_template('registro.html')

@loginrequired
@app.route('/dashboard')
def dashboard():

    return render_template('dashboard.html')



@app.route('/logout')
def logout():
    session.pop('usuario', None)  # Elimina el usuario de la sesión
    flash('Has cerrado sesión exitosamente.')
    return redirect(url_for('login'))



if __name__ == '__main__':
    app.run(debug=True)


if __name__ == '__main__':
    app.run(debug=True)  # Habilitar el modo de depuración
