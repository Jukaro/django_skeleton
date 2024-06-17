from django.urls import path
# from . import views

from members.views.views import *
from members.views.api import RegisterUserView, UserView
from members.views.home import home
from members.views.sign import sign

urlpatterns = [
	path('', home, name='home'),
    path('members/', members, name='members'),
	path('members/details/<int:id>', details, name='details'),
	path('profile/<str:username>', profile, name='profile'),
	path('testing/', testing, name='testing'),
	path('myfirst/', myfirst, name='myfirst'),
	path('jspage/', jspage, name='jspage'),
	path('profile/', rand_profile, name='rand_profile'),
	path('sign/', sign, name='sign'),
    path('api/register/', RegisterUserView.as_view()),
    path('api/user/', UserView.as_view()),
]
