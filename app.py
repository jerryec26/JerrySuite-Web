from flask import Flask, render_template, request, redirect
from registro import registrar_datos

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        presupuesto = request.form['presupuesto']
        cliente = request.form['cliente']
        lugar = request.form['lugar']
        fecha = request.form['fecha']
        version = request.form['version']
        tc = request.form['tc']

        if presupuesto and cliente and lugar and fecha and version and tc:
            registrar_datos(presupuesto, cliente, lugar, fecha, version, tc)
            return redirect('/')
        else:
            return "Por favor completa todos los campos."

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
