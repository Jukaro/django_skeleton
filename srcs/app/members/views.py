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
        'username': "jojo",
        'games_nb': "4",
        'wins': "2",
        'winrate': "50",

        "cards": [
            {
                "title": "Game wins",
                "value": "2",
            },
            {
                "title": "Total games",
                "value": "4",
            },
            {
                "title": "Winrate",
                "value": "50%",
            }
        ],

        'games': [
            {
                'players': {
                    'length': "2"
                },
                'created_at': "Wed Mar 17 19:42:50 2021",
                "target_user_info": {
                    "user": {
                        "username": "user1"
                    },
                    "score": "12",
                    "win": "true"
                },
                "adversaries": [
                    {
                        "user": {
                            "username": "user2"
                        },
                        "score": "6"
                    }
                ],
            },
            {
                "square": "true",
                "created_at": "Wed May 17 23:15:50 2024",
                "target_user_info": {
                    "user": {
                        "username": "user1"
                    },
                    "score": "6",
                    "win": "false"
                },
                "adversaries": [
                    {
                        "user": {
                            "username": "user2"
                        },
                        "score": "12",
                        "win": "true"
                    },
                    {
                        "user": {
                            "username": "user3"
                        },
                        "score": "3",
                        "win": "false"
                    },
                    {
                        "user": {
                            "username": "user4"
                        },
                        "score": "4",
                        "win": "false"
                    }
                ],
            },
            {
                "team_game": "true",
                'created_at': "2020-04-06",
                "target_user_info": {
                    "user": {
                        "username": "user1"
                    },
                    "score": "12",
                    "win": "true"
                },
                "all_players": [
                    {
                        "user": {
                            "username": "user1"
                        },
                        "score": "12",
                        "win": "true"
                    },
                    {
                        "user": {
                            "username": "user2"
                        },
                        "score": "6",
                        "win": "false"
                    },
                    {
                        "user": {
                            "username": "user3"
                        },
                        "score": "12",
                        "win": "false"
                    },
                    {
                        "user": {
                            "username": "user4"
                        },
                        "score": "6",
                        "win": "false"
                    }
                ],
            },
            {
                "square": "true",
                "created_at": "Wed May 17 23:15:50 2024",
                "target_user_info": {
                    "user": {
                        "username": "user1"
                    },
                    "score": "12",
                    "win": "true"
                },
                "adversaries": [
                    {
                        "user": {
                            "username": "user2"
                        },
                        "score": "6",
                        "win": "false"
                    },
                    {
                        "user": {
                            "username": "user3"
                        },
                        "score": "6",
                        "win": "false"
                    },
                    {
                        "user": {
                            "username": "user4"
                        },
                        "score": "6",
                        "win": "false"
                    }
                ],
            },
            {
                'players': {
                    'length': "2"
                },
                'created_at': "Wed Mar 17 19:42:50 2021",
                "target_user_info": {
                    "user": {
                        "username": "user1"
                    },
                    "score": "12"
                },
                "adversaries": [
                    {
                        "user": {
                            "username": "user2"
                        },
                        "score": "6",
                        "win": "false"
                    }
                ],
            },
        ]
    }
    return spa_render(request, 'profile.html', context)
