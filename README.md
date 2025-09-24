# python1

Usuario admin: jhonnyguerrero
clave: utilizar
Una aplicacion en python, un crud, pasos y ramas para aprender la creacion de un crud con python y manejo de ramas
Paso a paso, para ir creando la aplicacion y cada cambio realizar el commit.
1.creamos un entorno virtual
2.creamos djangocrud, el proyecto
probar la aplicacion en la consola: python manage.py runserver

---

1.crearemos la aplicacion task, dentro del proyecto
2.en el archivo view una funcion de hola mundo con httpresponse
3.configuar en djangocrud, setting.py llamar la app task, y urls.py
probrar la aplicacion comando: py manage.py runserver

---

1.crear la carpeta template en taks, y dentro un archivo html
2.editar el archivo views de taks
3.comprobar el funcionamiento.

---

1.Crear un formulario con la biblioteca de django, en el archivo views de taks
2.HAcer el envio del formulario como variable

---

Realizar el envio de los datos por el formulario en el mismo archivo, identificando el metodo post y get

---

VISTAS DE TAREAS, INICIAR SESION Y GUARDAR LA COOKIE
Crear una html tareas
En views, un metodo tasks o tareas, retorne el html
"cuando se registre el usuario que me redirecionea tasks-tareas, importando en la biblioteca redirect de shortcuts
-tambien crear la cookie, por la sesion, importado la biblioteca contrib.auth el login
Utilizar el objeto login pasando el reques y el usuario creado.
-try except, ajustarlo, importar biblioteca django.db integrityError, para corroborar integridad datos.

---

TEMPLATES Y CONDICIONALES
En la base.html condicionar los link-opciones segun la sesion.
En views configuar un metodo para salir, con metodo logout de django importado contrib.auth.
En url configuar la ruta de salir con metodo que creamos.

---

LOGIN
En views crear nuestra funcion para iniciar sesion, retornando un html.
Configurar el arhivo html, y el archivo url las rutas.
Importar authenticationform de contrib.auth.forms y poder crear el form de login.
En views en la funcion iniciar sesion ahora enviar el form de login.
En views validar el verbo Get o Post.
En views validar si los datos enviados, estan en bd, con authenticate importado de contrib.auth
capturar datos con authenticate, y guardarlos en un objeto user, y guarda la sesion.

---

CREAR LA TABLA TAREAS O TASKS, PARA GUARDAR INFORMACION
ORM "Object Relational Mapping"
En la carpeta tasks, archivo models, crear la clase tasks o tareas con su atributos.
Verificar en los atributos, el tipo de dato segun python.
Si hay una relacion utilizar las ayudas correspondientes de python
-Crear la migracion del archivo que acabamos de crear.
Ejecutar la migracion, para que cree la tabla.
Ahora ver la ruta /admin que viene por defecto en django
Crear un superusuario para nuestra aplicacion, por comandos.
En el panel del admin, no esta la opcion de tareas.
Editar en carpeta tasks el archivo admin.py, importar el modelo tareas.
Ya podemos añadir tareas desde el admin
Ver titulo de la tarea, editanto el archivo models la clase tareas, con una funcion **str\_**
Ver fecha de creacion, editar admin.py crear clase y atributo solo lectura, y registrar la clase

---

Hemos agregado tareas desde admin, ahora desde el usuario logueado.
Editar en views la funcion tareas para listar y crear la funcion ver formulario de tareas:
El html tareas ya esta creado, y el formulario utilizaremos librerias de python usando el modelo,

---

La creacion de un form lo separamos en un archivo diferente,
