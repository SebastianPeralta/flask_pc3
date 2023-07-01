from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuración de MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '' # Poner tu password aquí
app.config['MYSQL_DB'] = 'alumnos_PC3'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        details = request.form
        username = details['username']
        clave = details['clave']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM alumnos WHERE username=%s AND clave=%s", (username, clave,))
        user = cur.fetchone()
        if user:
            return 'Inicio de sesión exitoso'
        else:
            return 'Error en el inicio de sesión'
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        details = request.form
        username = details['username']
        nombre = details['nombre']
        apellidos = details['apellidos']
        clave = details['clave']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO alumnos(username, nombre, apellidos, clave) VALUES (%s, %s, %s, %s)", (username, nombre, apellidos, clave,))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('login'))
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True, port=3514)
