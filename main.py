# de la biblioteca flask voy a importar flask, ahora importamos, ahora importamos otro metodo llamado render template, ademas agregamos otros métodos  
from flask import Flask, render_template, send_file, request, redirect, url_for

#Importo desde la librería flas_email a Message, para poder así coge la información que recolecte en un html en particular y poder enviarla como un mensaje de email.

#from flask_mail import Mail, Message

#importamos la libreria para la base de datos al principio porque es una regla no escrita que s eve mal ponerla en medio. 
import sqlite3


# confirmo que estoy en el archivo principal y guardo lo que me envia flask en una variable que se llama app
app = Flask(__name__)

try:
  #Para crear la base de datos tenemos que tener una tabla que corresponde a dnde vamos a ingresar toda la información, eso lo hacemos con los siguientes códigos que esplicaré como utilizamos.

  #Conectamos la base de datos con un arcgivo de texto para que así quede toda la información allí.

  con = sqlite3.connect('database.db')

  #Vamos a necesitar un cursor que es el que como su nombre lo indica el que le da indicaciones a los datos y a la base como tal, pues nos permite trabajar con la tabla realmente.

  c = con.cursor()

  #Este es uno de los pasos mas importantes que yo me había tragado y por eso no existía la tabla, y como lo acabo de indicar es crear la tabla en donde irán almacenados nuestros datos, 

  #con execute ejecuto el comando que le estoy planteando, en este caso crear la tabla.

  c.execute('CREATE TABLE IF NOT EXISTS users(name TEXT NOT NULL, surname TEXT, email TEXT NOT NULL, password TEXT NOT NULL)')

  c.execute('CREATE TABLE IF NOT EXISTS curiosidades(enumerado TEXT NOT NULL, especie TEXT NOT NULL, dato1 TEXT, dato2 TEXT, dato3 TEXT, image BLOB NOT NULL)')

  c.execute('CREATE TABLE IF NOT EXISTS comentarios(nombre TEXT NOT NULL, email TEXT, comentario TEXT NOT NULL)')

  
  #con el con.comit lo que hago es realmente es guardar estos cambios y permitir que los datos queden aquí cuando hacen post

  con.commit()

  #EL close pues obviamente termina de ejecutar mi acción y permite que se cierre como tal la ación para que no surgan mas acciones indeseadas.

  c.close()

  #llamamos o requerimos al método post para así hacer que cuando ingrese datos a los comandos pues los datos se tomen y sean procesados a la base de datos

except error:
  print(error)
finally:

  con.close()






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
# Esta función me retornara algo al navegador, en este caso es solo un texto llamado "abaut page", esto hace unas semanas, ahora me retorna la información de ¿quienes somos?  ahora importamos render template el archivo UMB.html  
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

@app.route('/datos_curiosos', methods=('GET', 'POST'))
def datos_curiosos():

  if request.method == 'POST':

    con = sqlite3.connect('database.db')

    c = con.cursor()

    enumerado = request.form.get('enumerado')
    especie = request.form.get('especie')
    dato1 = request.form.get('dato1')
    dato2 = request.form.get('dato2')
    dato3 = request.form.get('dato3')
    image = request.form.get('image')

    #corregir y comentar de buena manera el data

    data = c.execute('SELECT * fROM curiosidades WHERE especie = ?', (especie,))

    c.close()

    if data==especie:

      return redirect(url_for('datos_curiosos'))
    
    else:

      c = con.cursor()

      #Creamos la funcion convertir_a_binario como una función auxiliar, tendriamos dentro de ella la image

      def convertir_a_binario(image):

        #realizamos la apertura invocando open (abrir) sobre el manejador de contexto (with), luego ahí estaría la ruta de la image e indicamos que va a hacer de modo de trabajo lectura en modo binario (rb) y llamamos a una variable f como el manejador del archivo.

        with open(image, 'rb') as f:

          #leemos los datos del archivo blob con la función efe y la acción leer (read)
          blob = f.read()

        #por ultimo retornamos el contenido de blob y ese contenido quedará en la variable image_binario
        return blob
        
        #tambien debo crear la función que lleve de binario a imagen

        #necesitamos obtener la versión en binario de la foto que vamos a insertar, entonces escribimos foto_binario como nombre de variable e invocamos una funcion que llamamos convertir_a_binario y pasamos como argumento el archivo que se va a convertir es una dupla con 6 elementos el último elemento, el que está en el índice -1 es la image, vamos a crear la función convertir_a_binario como una funcioón auxiliar

        image_binario = convertir_a_binario(curiosidades[-1])

        #recreamos la dupla "curiosidades" de la siguiente manera: llamamos todos sus índices y el último es donde tendriamos la imagen en binario antes de la orden de inser into

        curiosidades = (curiosidades[0], curiosidades[1], curiosidades[2], curiosidades[3], curiosidades[4], curiosidades[5], image_binario)



      c.execute('INSERT INTO curiosidades(enumerado, especie, dato1, dato2, dato3, image) VALUES (?,?,?,?,?,?)', (enumerado, especie, dato1, dato2, dato3, image))


      con.commit()

      c.close()

      return redirect(url_for('funciones_avanzadas'))


  return render_template ('datos_curiosos.html')






@app.route('/tipo_especie')
def tipo_especie():
  return render_template ('tipo_especie.html')

@app.route('/bibliografia')
def bibliografia():
  return render_template ('bibliografia.html')

#le digo a python qye voy a utilizar los dos métodos (get y post)

@app.route('/contacto', methods=('GET', 'POST'))

#Creo la función

def contacto():

  #Cuando el Usuario intente enviarme datos utilizo el método post en este caso.

  if request.method == 'POST':

    con = sqlite3.connect('database.db')

    c = con.cursor()

    nombre = request.form.get('nombre')
    email = request.form.get('email')
    comentario = request.form.get('comentario')

    c.execute('INSERT INTO comentarios(nombre, email, comentario) VALUES (?,?,?)', (nombre, email, comentario))

    con.commit()

    c.close()

    return redirect(url_for('UMB'))

  return render_template ('contacto.html')




    

  






@app.route('/funciones_avanzadas')
def funciones_avanzadas():
  return render_template ('funciones_avanzadas.html')






#decorador con get y post para que muestre y capte información respectivamente hablando, en este caso nosostros con el post vamos a coger la información y almacenarla en una base de datos.

# la forma de almacenarlos es nombrando una variable igual a request.form que es como un método que de dirigue al formulario que está en esa vista y capta esa información
#cargo una lista nueva para ingresar toda la información

@app.route('/signup/', methods=('GET', 'POST'))

def signup():

  if request.method == 'POST':

    #Conexión de la base de datos con un archivo de texto

    con = sqlite3.connect('database.db')

    #ahora vamos a conectar un cursor que va a trabajar no con codigo corrido si no focalizado, y nos permite trabajar con la tabla, creamos tablas, consultar valores en las tablar, menajr los valores de las tablas, etc.

    c = con.cursor()

    #llamamos todas las variables que nombremos en el método post y en las que las personas en este caso van a ingresar sus datos para registrarse.

    name = request.form.get('name')
    surname = request.form.get('surname')
    email = request.form.get('email')
    password = request.form.get('password')

    #verificaos que no exista una persona con el mismo correo.
    #SELECT FROM es para consultar datos y por medio del user que se encuentra en la creación de la tabla vamos a llamar a la variable email para verificar su unicidad.

    data = c.execute('SELECT * fROM users WHERE email = ?', (email,))

    #EL close pues obviamente termina de ejecutar mi acción y permite que se cierre como tal la ación para que no surgan mas acciones indeseadas.

    c.close()

    #En caso que no se cumpla la unicidad del email no me dejará avanazar

    if data==email:

      #No me dejará avanzar del signup, es decir de la pestaña de registro

      return redirect(url_for('signup'))

      #En caso contrario avanzará con la introducción de los datos a la base de datos.

    else:

      #donde no exista (else) creo el cursor y la lista que voy a ingresar

      c = con.cursor()

      #A continuación creamos la base de datos donde se va almacenar los datos de usurios, junto a los códigos que permitan crear tablas. 
      #INSERT INTO es para guardar datos, entonces los utilizamos por medio de la tabla creada users y ahí todos los comandos que hagan post se irán a la tabla creada en forma de fila como lo indica los signos de interrogación

      c.execute('INSERT INTO users(name, surname, email, password) VALUES (?,?,?,?)', (name, surname, email, password))

      #con el con commit lo que hago es mandar eso realmente a la base

      con.commit()

      #EL close pues obviamente termina de ejecutar mi acción y permite que se cierre como tal la ación para que no surgan mas acciones indeseadas.

      c.close()

      #con este último return redirect me quiere decir que cuando yo lo termine él me enviará una página en específico.

      return redirect(url_for('UMB'))

  return render_template("signup_form.html")

#Cuando tenemos ya la tabla construida pasamos a la parte del login o acceso y es el mismo proceso.

@app.route("/login", methods=("GET", "POST"))
def login():
  if request.method == 'POST':
    #Conexión de la base de datos con un archivo de texto
    con = sqlite3.connect('database.db')
    #Vamos a crear el cursor.
    c = con.cursor()
    #capto los datos que quiero utilizar para la onsulta.
    email = request.form.get('email')
    password = request.form.get('password')
    #utilizo el comando para obtener un email de la tabla seleccionandolo.
    c.execute('SELECT * fROM users WHERE email = ?', (email,))

    #capto un sólo valor con fetchone, ya que es un sólo usuario el que está entrando y no varios.

    try:

      passw = c.fetchone()[-1]

      c.close()


      if passw==password:
        return redirect(url_for('funciones_avanzadas'))
      else:
        return redirect(url_for('login'))

    except TypeError:

      return redirect(url_for('signup'))
    

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
