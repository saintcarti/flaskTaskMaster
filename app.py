from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Retorna la plantilla directamente

@app.route('/registro')
def registro():
    return render_template('registro.html')




if __name__ == '__main__':
    app.run(debug=True)  # Habilitar el modo de depuración
