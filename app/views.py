from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404

def hello(request):
    return HttpResponse("<h1>hello</h1>")

def say_hi(request):
    return render_to_response("say_hi.html")


