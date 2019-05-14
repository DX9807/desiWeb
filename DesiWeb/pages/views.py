from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request,'index.html',{})

def about(request):

    return render(request,'about.html',{})

def help(request):

    return render(request,'help.html',{})

def contact(request):

    return render(request,'contact.html',{})

def pyp(request):

    return render(request,'pyp.html',{})

def discussionforum(request):

    return render(request,'discussionforum.html',{})

def courses(request):

    return render(request,'courses.html',{})

def company(request):
    return render(request,'company.html',{})


def partners(request):
    return render(request,'partners.html',{})


def settings(request):
    return render(request,'settings.html',{})

def offers(request):
    return render(request,'offers.html',{})


def team(request):
    return render(request,'team.html',{})


def quantitativeapti(request):
    return render(request,'subjects/quantitativeapti.html',{})


def reasoning(request):
    return render(request,'subjects/reasoning.html',{})
