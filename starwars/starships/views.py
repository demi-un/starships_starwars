from django.shortcuts import render


def main_page(request):
    return render(request, 'starships/main_page.html')

def starship(request):
    return render(request, 'starships/starship.html')
