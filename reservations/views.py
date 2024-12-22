from django.shortcuts import render

def index_view(request):
    return render(request, "pages/index.html")

def hotels_view(request):
    return render(request, "pages/hotels.html")
