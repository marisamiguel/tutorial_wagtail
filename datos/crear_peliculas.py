from pelis.models import Pelicula
import json

#lista de películas del json
pelis = json.load(open("listapelis.json"))

for p1 in pelis:
    p = Pelicula()
    p.title = p1["movie_title"]
    p.rating = p1["rating"]
    p.link = "https://www.imdb.com" + p1["link"]
    p.place = p1["place"]
    year = p1["year"]
    if year.isdigit():
        p.year = p1["year"]
    else:
        p.year = 0
    p.imagen = p1["images"][0]
    p.cast = p1['star_cast']
    p.save()
