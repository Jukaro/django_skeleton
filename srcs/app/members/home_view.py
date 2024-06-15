from django.http import HttpRequest
from members.views import spa_render

def home(request: HttpRequest):
    return spa_render(request, 'home.html')
