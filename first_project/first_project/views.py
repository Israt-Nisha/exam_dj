from django.http import HttpResponse


def home(request):
    return HttpResponse("hello, this is first django page")

def about(request):
    return HttpResponse("hello, this is about page")