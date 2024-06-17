from django.http import HttpRequest
from members.views.views import spa_render

def sign(request: HttpRequest):
    return spa_render(request, 'sign.html')
