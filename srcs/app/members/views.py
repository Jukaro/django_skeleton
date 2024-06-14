from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader
from members.models import Member

def spa_render(request, path, context=None):
    if request.headers.get('X-Source') == "SPA":
        return render(request, path, context=context)
    return render(request, 'master.html')

# Create your views here.
def members(request):
    mymembers = Member.objects.all().values()
    context = {
        'mymembers': mymembers,
    }
    return spa_render(request, 'all_members.html', context)

def details(request, id):
    mymember = Member.objects.get(id=id)
    context = {
        'mymember': mymember,
    }
    return spa_render(request, 'details.html', context)

def home(request: HttpRequest):
    return spa_render(request, 'home.html')

def testing(request):
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry']
    }
    return spa_render(request, 'template.html', context)

def myfirst(request):
    return spa_render(request, 'myfirst.html')

def jspage(request):
    return spa_render(request, 'jspage.html')

def profile(request):
    context = {
        'avatar': "/static/img/pp.png",
        'username': "jojo"
    }
    return spa_render(request, 'profile.html', context)
