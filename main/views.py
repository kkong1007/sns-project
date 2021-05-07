from django.shortcuts import render

# Create your views here.
def showmain(request):
    return render(request, 'main/mainpage.html')
def show(request):
    return render(request, 'main/show.html')
def bucket(request):
    return render(request, 'main/bucket.html')
def photo(request):
    return render(request, 'main/photo.html')