# de la biblioteca flask voy a importar flask, ahora importamos, ahora importamos otro metodo llamado render template  
from flask import Flask, render_template

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

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
# utilizamos un debug=True  para dcirle que nuestra aplicacion esta en modo de prueba cada vez que escribamos un codigo se reinicia de forma automatica 


#vamos a importar una base de datos desde SQLite 3 esa es la base de datos que va a tener todo lo que es cuentas y contraseñas de las personas que quieran acceder a las opciones avanzadas.