# de la biblioteca flask voy a importar flask, ahora importamos, ahora importamos otro metodo llamado render template, ademas agregamos otros métodos  
from flask import Flask, render_template, send_file, request, redirect, url_for

#importamos la libreria para la base de datos al principio porque es una regla no escrita que s eve mal ponerla en medio. 
import sqlite3


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

@app.route('/funciones_avanzadas')
def funciones_avanzadas():
  return render_template ('funciones_avanzadas.html')

#decorador con get y post para que muestre y capte información respectivamente hablando, en este caso nosostros con el post vamos a coger la información y almacenarla en una base de datos.

# la forma de almacenarlos es nombrando una variable igual a request.form que es como un método que de dirigue al formulario que está en esa vista y capta esa información
#cargo una lista nueva para ingresar toda la información
@app.route("/signup/", methods=["GET", "POST"])
def signup():


  #Para crear la base de datos tenemos que tener una tabla que corresponde a dnde vamos a ingresar toda la información, eso lo hacemos con los siguientes códigos que esplicaré como utilizamos.

  #Conectamos la base de datos con un arcgivo de texto para que así quede toda la información allí.

  con = sqlite3.connect('database.db')

  #Vamos a necesitar un cursor que es el que como su nombre lo indica el que le da indicaciones a los datos y a la base como tal, pues nos permite trabajar con la tabla realmente.

  c = con.cursor()

  #Este es uno de los pasos mas importantes que yo me había tragado y por eso no existía la tabla, y como lo acabo de indicar es crear la tabla en donde irán almacenados nuestros datos, 

  #con execute ejecuto el comando que le estoy planteando, en este caso crear la tabla.

  c.execute('CREATE TABLE IF NOT EXISTS users(name TEXT NOT NULL, surname TEXT, email TEXT NOT NULL, password TEXT NOT NULL)')
  
  #con el con.comit lo que hago es realmente es guardar estos cambios y permitir que los datos queden aquí cuando hacen post

  con.commit()

        #EL close pues obviamente termina de ejecutar mi acción y permite que se cierre como tal la ación para que no surgan mas acciones indeseadas.

  c.close()



  if request.method == 'POST':
    #Conexión de la base de datos con un archivo de texto
    con = sqlite3.connect('database.db')
    #ahora vamos a conectar un cursor que va a trabajar no con codigo corrido si no focalizado, y nos permite trabajar con la tabla, creamos tablas, consultar valores en las tablar, menajr los valores de las tablas, etc.
    c = con.cursor()

    name = request.form['name']
    surname = request.form['surname']
    email = request.form['email']
    password = request.form['password']
    #verificaos que no exista una persona con el mismo correo.
    #SELECT FROM es para consultar datos
    data = c.execute('SELECT * fROM users WHERE email = ?', (email,))
    #EL close pues obviamente termina de ejecutar mi acción y permite que se cierre como tal la ación para que no surgan mas acciones indeseadas.
    c.close()
    if data:
      return redirect(url_for('signup'))
    else:
      #donde no exista (else) creo el cursor y la lista que voy a ingresar
      c = con.cursor()
      #A continuación creamos la base de datos donde se va almacenar los datos de usurios, junto a los códigos que permitan crear tablas. 
      #INSERT INTO es para guardar datos, entonces los utilizamos por medio de la tabla creada users y ahí todos los comandos que hagan post se irán a la tabla creada en forma de fila como lo indica los signos de interrogación
      c.execute('INSERT INTO users (name, surname, email, password) VALUES (?,?,?,?)', (name, surname, email, password))
      #con el con commit lo que hago es mandar eso realmente a la base
      con.commit()
      #EL close pues obviamente termina de ejecutar mi acción y permite que se cierre como tal la ación para que no surgan mas acciones indeseadas.
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
    c = con.cursor()
    #capto los datos que quiero utilizar.
    email = request.form['email']
    password = request.form['password']
    c.execute('SELECT = fROM users WHERE email = ?', (email,))
    passw = c.fetchone() [-1] #capto un sólo valor.
    c.close()
    if passw==password:
      return redirect(url_for('funciones_avanzadas'))
    else:
      return redirect(url_for('login'))

  return render_template("login.html")

#así mismo vamos a crear una funcion para cerrrar sesión.
@app.route('/log_out')
def log_out():
  return render_template ('log_out.html')

#creamos una ruta para el script
@app.route('/script')
def script():
  return render_template ('script.js')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
# utilizamos un debug=True  para dcirle que nuestra aplicacion esta en modo de prueba cada vez que escribamos un codigo se reinicia de forma automatica 


#vamos a importar una base de datos desde SQLite 3 esa es la base de datos que va a tener todo lo que es cuentas y contraseñas de las personas que quieran acceder a las opciones avanzadas.
