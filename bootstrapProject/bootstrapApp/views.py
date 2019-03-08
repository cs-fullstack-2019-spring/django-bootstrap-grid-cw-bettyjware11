from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "bootstrapApp/index.html")


def next(request):
    return render(request, "bootstrapApp/next.html")


def previous(request):
    return render(request, "bootstrapApp/previous.html")


def Page2(request):
    return render(request, "bootstrapApp/Page2.html")

def Page3(request):
    return render(request, "bootstrapApp/Page3.html")


def changeBackgroundColor(request):
    return