'''
crear songs

ejecctar:

python manage.py shell < datos/crea_canciones.py

Gracias a este archivo python, podemos extraer los eventos del 
json datos_eventos.json
'''

from canciones.models import Cancion
import datetime as dt
import json
import os


# borrar canciones
for c in Cancion.objects.all():
    c.delete()

#lista de canciones del json
if os.path.exists("datos/songs.json"):
    songs = json.load(open("datos/songs.json", encoding="utf-8"))
else:
    songs = json.load(open("songs.json", encoding="utf-8"))

songs = songs['docs'] 
for c1 in songs:
    c = Cancion()
    c.rank = c1["rank"]
    c.title = c1["title"].replace('"', "")
    c.artist = c1["artist"]
    c.peak = c1["peak"]
    c.weeks = c1["weeks"]
   
    c.save()
