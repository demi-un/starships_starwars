from django.shortcuts import render
import requests


url = "https://swapi.dev/api/starships/"
responce = requests.get(url).json()["results"]

starships_list = responce


def main_page(request):
    return render(
        request, "starships/main_page.html", {"starships_list": starships_list}
    )


def starship(request, id):
    starship = starships_list[id]
    return render(request, "starships/starship.html", {'starship': starship})
