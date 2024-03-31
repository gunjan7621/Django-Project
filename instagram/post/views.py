from django.shortcuts import render


# Create your views here.
def index(request):
    data= {"title": "Instagram"}
    return render(request, "index.html",data)
def search(request):
    data= {"title": "post"}
    return render(request, "Search.html",data)

