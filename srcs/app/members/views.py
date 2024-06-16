from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader
from members.models import Member, User

from django.db.models.functions import Random

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

def rand_profile(request):
    rand_user = User.objects.annotate(random_value=Random()).order_by('random_value').first()
    return profile(request, rand_user.username)

from game.models import Match
from game.serializer import MatchSerializer
import json

def profile(request, username):
    user = User.objects.get(username=username)
    print(f"User: {user.username}")

    matches = list(Match.objects.filter(players__user=user).order_by('-created_at').distinct())

    serializer = MatchSerializer(matches, many=True, context={'target_username': username})
    # print(f"ser: {serializer.data}")
    games = serializer.data
    context = {
        'avatar': user.avatar,
        'username': user.username,

        "cards": [
            {
                "title": "Game wins",
                "value": user.wins,
            },
            {
                "title": "Total games",
                "value": user.games,
            },
            {
                "title": "Winrate",
                "value": f"{round(user.wins * 100 / user.games) if user.wins != 0 else 0}%",
            }
        ],

        "games": serializer.data

        # 'games': [
        #     {
        #         'players': {
        #             'length': "2"
        #         },
        #         'created_at': "Wed Mar 17 19:42:50 2021",
        #         "target_user_info": {
        #             "user": {
        #                 "username": "user1"
        #             },
        #             "score": "12",
        #             "win": "true"
        #         },
        #         "adversaries": [
        #             {
        #                 "user": {
        #                     "username": "user2"
        #                 },
        #                 "score": "6"
        #             }
        #         ],
        #     },
        #     {
        #         "square": "true",
        #         "created_at": "Wed May 17 23:15:50 2024",
        #         "target_user_info": {
        #             "user": {
        #                 "username": "user1"
        #             },
        #             "score": "6",
        #             "win": "false"
        #         },
        #         "adversaries": [
        #             {
        #                 "user": {
        #                     "username": "user2"
        #                 },
        #                 "score": "12",
        #                 "win": "true"
        #             },
        #             {
        #                 "user": {
        #                     "username": "user3"
        #                 },
        #                 "score": "3",
        #                 "win": "false"
        #             },
        #             {
        #                 "user": {
        #                     "username": "user4"
        #                 },
        #                 "score": "4",
        #                 "win": "false"
        #             }
        #         ],
        #     },
        #     {
        #         "team_game": "true",
        #         'created_at': "2020-04-06",
        #         "target_user_info": {
        #             "user": {
        #                 "username": "user1"
        #             },
        #             "score": "12",
        #             "win": "true"
        #         },
        #         "all_players": [
        #             {
        #                 "user": {
        #                     "username": "user1"
        #                 },
        #                 "score": "12",
        #                 "win": "true"
        #             },
        #             {
        #                 "user": {
        #                     "username": "user2"
        #                 },
        #                 "score": "6",
        #                 "win": "false"
        #             },
        #             {
        #                 "user": {
        #                     "username": "user3"
        #                 },
        #                 "score": "12",
        #                 "win": "false"
        #             },
        #             {
        #                 "user": {
        #                     "username": "user4"
        #                 },
        #                 "score": "6",
        #                 "win": "false"
        #             }
        #         ],
        #     },
        #     {
        #         "square": "true",
        #         "created_at": "Wed May 17 23:15:50 2024",
        #         "target_user_info": {
        #             "user": {
        #                 "username": "user1"
        #             },
        #             "score": "12",
        #             "win": "true"
        #         },
        #         "adversaries": [
        #             {
        #                 "user": {
        #                     "username": "user2"
        #                 },
        #                 "score": "6",
        #                 "win": "false"
        #             },
        #             {
        #                 "user": {
        #                     "username": "user3"
        #                 },
        #                 "score": "6",
        #                 "win": "false"
        #             },
        #             {
        #                 "user": {
        #                     "username": "user4"
        #                 },
        #                 "score": "6",
        #                 "win": "false"
        #             }
        #         ],
        #     },
        #     {
        #         'players': {
        #             'length': "2"
        #         },
        #         'created_at': "Wed Mar 17 19:42:50 2021",
        #         "target_user_info": {
        #             "user": {
        #                 "username": "user1"
        #             },
        #             "score": "12"
        #         },
        #         "adversaries": [
        #             {
        #                 "user": {
        #                     "username": "user2"
        #                 },
        #                 "score": "6",
        #                 "win": "false"
        #             }
        #         ],
        #     },
        # ]
    }
    return spa_render(request, 'profile.html', context)
