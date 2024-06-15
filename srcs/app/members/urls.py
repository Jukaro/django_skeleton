from django.urls import path
from . import views

from members.home_view import home

urlpatterns = [
	path('', home, name='home'),
    path('members/', views.members, name='members'),
	path('members/details/<int:id>', views.details, name='details'),
	path('testing/', views.testing, name='testing'),
	path('myfirst/', views.myfirst, name='myfirst'),
	path('jspage/', views.jspage, name='jspage'),
	path('profile/', views.profile, name='profile'),
]
