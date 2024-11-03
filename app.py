from flask import Flask, render_template, request, jsonify, redirect, url_for,flash
import requests

app = Flask(__name__)
app.secret_key = 'una_clave_secreta_muy_dificil_de_adivinar'

@app.route('/index')
def index():
    flash('Bienvenido a la aplicación!')
    return render_template('index.html')


@app.route('/', methods=[ 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']

        # Hacer una solicitud GET a json-server
        response = requests.get(f'http://localhost:3000/usuarios?usuario={usuario}&password={password}')

        if response.json():
            flash('Inicio de sesión exitoso!')
            return redirect(url_for('/dashboard'))
        else:
            flash('Usuario o contraseña incorrectos.')

    return render_template('index.html')



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

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')



if __name__ == '__main__':
    app.run(debug=True)


if __name__ == '__main__':
    app.run(debug=True)  # Habilitar el modo de depuración
