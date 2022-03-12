#tutorial_wagtail_final

¿ Que es Wagtail ? Wagtail es un CMS de código abierto escrito en Python y creado en el marco web de Django .



##Descripción
Web de datos realizada con Wagtail. En ella podemos ver el listado de las 250 mejores películas (extraidas de la web de IMDb: https://www.imdb.com/chart/top/).En ella podemos ver el listado de las 250 mejores películas según IMDb,viajes, hoteles y noticias en general.

###Nombre del admin: johanna / contraseña : johanna

#¿Cómo lo instalo y hago funcionar?
Instalar y ejecutar Wagtail
Instalar dependencias Wagtail es compatible con Python 3.7, 3.8, 3.9 y 3.10. 

Para verificar si tiene una versión apropiada de Python 3:
python3 --version.

##Windows
1. (ATENCIÓN) Deberemos tener en nuestro ordenador la aplicación "GitBash" u otra del estilo y Python, para que el cmd reconozca los comandos correspondientes.

1. posicionamos donde queramos tener la capeta en el cmd (con cd).
1. Copiamos el enlace del repositorio git donde está el trabajo.
1. En el cmd escribimos: git clone https://github.com/johannague/tutorial_wagtail_final
1. Nos posicionamos dentro del proyecto
1. Creamos el entorno virtual (py -m venv env)
1. Activamos el entorno virtual (env\Scripts\activate.bat)
1. Instalamos los requisitos (pip install -r requirements.txt).
1. Dentro del entorno: py manage.py runserver
1. En google buscamos: http://localhost:8000/ (número indicado al ejecutar el runserver (Starting development server at http://127.0.0.1:8000/) ese es el 8000)
Cuando queramos pararlo: Ctrl + c (en el cmd).

##Linux/Mac
1. (ATENCIÓN) Deberemos tener en nuestro ordenador la aplicación "GitBash" u otra del estilo y Python, para que el cmd reconozca los comandos correspondientes.

1. Nos posicionamos donde queramos tener la capeta en el cmd (con cd).
Copiamos el enlace del repositorio git donde está el trabajo
1. En el cmd escribimos: git clone https://github.com/johannague/tutorial_wagtail_final
1. Nos posicionamos dentro del proyecto
1. Creamos el entorno virtual (python3 -m venv env)
1. Activamos el entorno virtual (source tutorial-env/bin/activate)
1. Instalamos los requisitos (pip install -r requirements.txt).
1. Dentro del entorno: py manage.py runserver
1. En google buscamos: http://localhost:8000/ (número indicado al ejecutar el runserver (Starting development server at http://127.0.0.1:8000/) ese es el 8000)
Cuando queramos pararlo: Ctrl + c (en el cmd).

##Enlace donde podréis encontrar más información del CMS DE WAGTAIL
[Wagtail](https://wagtail.org/)

