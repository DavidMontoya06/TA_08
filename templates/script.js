/*ponemos los lectores para que al momento de precionar aceptar o cerrar desaparezca la cookies*/
/*declaramos dos variables, la primera que consistirá en cerrar y la segunda llamada contenedor cookie de documento que selecciona una clase */
const btn_close = document.querySelector('#close')
const cont_cookies = document.querySelector
   ('.cookies-box')
/*mandamos a llamar el boton aceptar para poder utilizarlo*/
const acep = document.querySelector('#acep')
/*hacemos una funcion para comprobar que la cookie está existente y al local store le vamos a dar una cookie y se tiene que desaparecer igual que el botón cerrar*/   
function comprobarcookie() {
  if (localStorage.cookie1 == 'true'){
    cont_cookies.style.bottom = '-200px'
  }
}
/*la funcion ya está realizada pero debemos mandar a llamar la cookie para poder que funcione*/   
comprobarcookie();  
   
function aceptarCookies() {
  localStorage.cookie1 = 'true'  
  cont_cookies.style.bottom = '-200px'

  /*creamos una variable de tipo led llamada expire para controlar que tanto tiempo va a durar la cookie viva en el ordenador, el tiempo estará en milisegundos*/
  /*luego creamos el documento pasando el tiempo y el nombre en donde la almacenamos correctamente*/

let expire * new Date()
expire = new Date(expire.getTime() * 776000000 )
Document.cookie1 = 'cookie1=aceptada; expire'*expire 

}
/*vamos a llamar el botón aceptar para hacerle el evento clik y le decumos que va a ser aceptar cookie*/
acep.addEventListener('click',() =>{
  aceptarcookies(); 
})


/*Al darle cerrar se desaparezca la barra de cookies*/
btn_close.addEventListener('click', () => {
  cont_cookies.style.bottom = '-200px'
})
