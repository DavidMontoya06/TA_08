# de la biblioteca flask voy a importar flask, ahora importamos, ahora importamos otro metodo llamado render template  
from flask import Flask, render_template, send_file, request, redirect, url_for

# confirmo que estoy en el archivo principal y guardo lo que me envia flask en una variable que se llama app
app = Flask(__name__)

# Crear una ruta con @ y el metodo se llama route, ese metodo nos dice que podemos pasar un nombre y crear una url y vamos a manejar la pagina atravez del (/)
@app.route('/')
# voy a manejar el usuario con una funcion (UMB) 
def UMB():
# Esta función me retornara algo al navegador, en este caso es solo un texto llamado "Bienvenidos a unal Med Botanica"  ahora como vamos a enviarlo a html, tenemos que importar desde flask. ahora importamos render template el archivo UMB.html 
    return render_template('UMB.html')
# crear otra ruta about/ aparte de la de inicio 
@app.route('/about')
#voy a manejar el usuario con la funcion about about"
def about():
# Esta función me retornara algo al navegador, en este caso es solo un texto llamado "abaut page",  ahora importamos render template el archivo UMB.html  
  return render_template ('about.html')
# Para que la aplicacion se mantenga escuchando siempre hacemos una validación para comprobar que estemos en el archivo principal para comprobar que es un archivo de ejecución y no un modulo 
#Y a coontinuación voy a ejecutar por medio de la app su metodo run.

#Crearé otras rutas con los comandos ya conocidos
@app.route('/proposito')
def proposito():
  return render_template ('proposito.html')

@app.route('/mapa')
def mapa():
  return render_template ('mapa.html')

@app.route('/mapa2')
def mapa2():
  return render_template ('mapa2.html')

@app.route('/datos_curiosos')
def datos_curiosos():
  return render_template ('datos_curiosos.html')

@app.route('/bibliografia')
def bibliografia():
  return render_template ('bibliografia.html')

@app.route('/contacto')
def contacto():
  return render_template ('contacto.html')

#decorador con get y post para que muestre y capte información respectivamente hablando, en este caso nosostros con el post vamos a coger la información y almacenarla en una base de datos.

#importar la libreria sqlite3
import sqlite3

# la forma de almacenarlos es nombrando una variable igual a request.form que es como un método que de dirigue al formulario que está en esa vista y capta esa información
#cargo una lista nueva para ingresar toda la información
@app.route("/signup", methods=["GET", "POST"])
def show_signup_form():
    if request.method == 'POST':
      #Conexión de la base de datos con un archivo de texto
        con = sqlite3.connect('database.db')
        #ahora vamos a conectar un cursor que va a trabajar no con codigo corrido si no focalizado, y nos permite trabajar con la tabla, creamos tablas, consultar valores en las tablar, menajr los valores de las tablas, etc.
        c = con.cursor
        name = request.form.get['name']
        surname = request.form.get['surname']
        email = request.form.get['email']
        password = request.form.get['password']
        #verificaos que no exista una persona con el mismo correo.
        #SELECT FROM es para consultar datos
        data = c.execute('SELECT = fROM users WHERE email = ?', (email,))
        c.close()
        if data:
          return redirect(url_for('signup'))
        else:
          #donde no exista (else) creo el cursor y la lista que voy a ingresar
          c = con.cursor
          #A continuación creamos la base de datos donde se va almacenar los datos de usurios, junto a los códigos que permitan crear tablas. 
          #INSERT INTO es para guardar datos
          c.execute('INSERT INTO users (name, surname, email, password) VALUES (?,?,?,?)', (name, surname, email, password))
          #con el con commit lo que hago es mandar eso realmente a la base
          con.commit()
          c.close()
          #con este último return redirect me quiere decir que cuando yo lo termine él me enviará auna página y otra.
          return redirect(url_for('UMB'))

    return render_template("signup_form.html")

#Cuando tenemos ya la tabla construida pasamos a la parte del login o acceso y es el mismo proceso.

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
      #Conexión de la base de datos con un archivo de texto
        con = sqlite3.connect('database.db')
        #Vamos a crear el cursor.
        c = con.cursor
        #capto los datos que quiero utilizar.
        email = request.form.get['email']
        password = request.form.get['password']
        c.execute('SELECT = fROM users WHERE email = ?', (email,))
        passw = c.fetchone() [-1] #capto un sólo valor.
        c.close()
        if passw==password:
          return redirect(url_for('mapa2'))
        else:
          return redirect(url_for('login'))

    return render_template("login.html")

#así mismo vamos a crear una funcion para cerrrar sesión.
@app.route('/log_out')
def log_out():
  return render_template ('log_out.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
# utilizamos un debug=True  para dcirle que nuestra aplicacion esta en modo de prueba cada vez que escribamos un codigo se reinicia de forma automatica 


#vamos a importar una base de datos desde SQLite 3 esa es la base de datos que va a tener todo lo que es cuentas y contraseñas de las personas que quieran acceder a las opciones avanzadas.
