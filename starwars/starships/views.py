from django.shortcuts import render
import requests


url = "https://swapi.dev/api/starships/"
responce = requests.get(url).json()["results"]

starships_list = responce

starship_images = {
    "CR90 corvette": "starships/img/CR90 corvette.jpg",
    "Star Destroyer": "starships/img/star destroyer.jpeg",
    "Sentinel-class landing craft": "starships/img/sentinel class landing craft.jpg",
    "Death Star": "starships/img/death star.jpeg",
    "Millennium Falcon": "starships/img/millenium falcon.jpg",
    "Y-wing": "starships/img/Y wing.jpeg",
    "X-wing": "starships/img/X wing.jpg",
    "TIE Advanced x1": "starships/img/tie advanced x1.jpg",
    "Executor": "starships/img/executor.jpeg",
    "Rebel transport": "starships/img/rebel transport.jpeg",
}


def main_page(request):
    return render(
        request, "starships/main_page.html", {"starships_list": starships_list}
    )


def starship(request, id):
    starship = starships_list[id]
    starship['logo'] = starship_images[starship['name']]
    return render(
        request,
        "starships/starship.html",
        {"starship": starship, "images": starship_images},
    )
