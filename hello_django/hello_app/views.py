from django.shortcuts import render
from django.shortcuts import render
# Create your views here.
def print_hello(request):
    movies = {
        "movies": [
            {"name": "godha", "year": 2017, "summary": "its movie is tovino thomaus movie and good love story and inspration type movie ", "success": True},
            {"name": "King of Kotha", "year": 2023, "summary": "its movie is tovino thomaus movie and good love story and inspration type movie ", "success": False},
            {"name": "Jailer", "year": 2023, "summary": "its movie is tovino thomaus movie and good love story and inspration type movie ", "success": True},
            {"name": "vettam", "year": 2000, "summary": "its movie is tovino thomaus movie and good love story and inspration type movie ", "success": True},
            {"name": "chenai expres", "year": 2017, "summary": "its movie is tovino thomaus movie and good love story and inspration type movie ", "success": False},
            {"name": "iratta", "year": 2022, "summary": "its movie is tovino thomaus movie and good love story and inspration type movie ", "success": True},
        ]
    }
    return render(request, 'hello.html', movies)
