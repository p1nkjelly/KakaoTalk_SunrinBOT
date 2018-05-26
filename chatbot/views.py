# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from json import loads
import tools

def index(request):
    return HttpResponse("<h1>Server Is Alive!</h1>")


buttons = ["오늘의 급식", "오늘의 시간표", "내일의 급식", "내일의 시간표", "다음 급식", "학사일정", "학년-반 정보 등록/변경", "도움말"]
classlist = []
for i in range(1, 4):
    for j in range(1, 13):
        classlist.append(str(i)+"-"+str(j))

def keyboard(request):
    return JsonResponse({
        "type": "buttons",
        "buttons": buttons
    })

@csrf_exempt
def message(request):
    json_str = request.body.decode('utf-8')
    received_json = loads(json_str)
    content_name = received_json['content']
    api_userkey = received_json['user_key']

    if content_name == "오늘의 급식":
        return JsonResponse({
            "message": {
                "text": tools.today_menu()
            },
            "keyboard": {
                "type": "buttons",
                "buttons": buttons
            }
        })

    elif content_name == "내일의 급식":
        return JsonResponse({
            "message": {
                "text": tools.tomorrow_menu()
            },
            "keyboard": {
                "type": "buttons",
                "buttons": buttons
            }
        })

    elif content_name == "다음 급식":
        return JsonResponse({
            "message": {
                "text": tools.next_menu()
            },
            "keyboard": {
                "type": "buttons",
                "buttons": buttons
            }
        })

    elif content_name == "오늘의 시간표":
        return JsonResponse({
            "message": {
                "text": tools.userinfo(api_userkey, 0)
            },
            "keyboard": {
                "type": "buttons",
                "buttons": buttons
            }
        })
    elif content_name == "내일의 시간표":
        return JsonResponse({
            "message": {
                "text": tools.userinfo(api_userkey, 1)
            },
            "keyboard": {
                "type": "buttons",
                "buttons": buttons
            }
        })

    elif content_name == "학사일정":
        return JsonResponse({
            "message": {
                "text": tools.school_cal_print()
            },
            "keyboard": {
                "type": "buttons",
                "buttons": buttons
            }
        })

    elif content_name == "학년-반 정보 등록/변경":
        return JsonResponse({
            "message": {
                "text": "자신의 학년-반을 선택하세요."
            },
            "keyboard": {
                "type": "buttons",
                "buttons": classlist
            }
        })

    elif content_name == "도움말":
        return JsonResponse({
            "message": {
                "text": '''오늘급식 : 오늘의 급식을 보여줍니다.
내일급식 : 내일의 급식을 보여줍니다.
다음급식 : 다음 급식이 존재하는 날의 급식을 보여줍니다.
오늘의 시간표 : 반별 오늘의 시간표를 보여줍니다.
내일의 시간표 : 반별 내일의 시간표를 보여줍니다.
학사일정 : 학교에서 시행되는 행사나 일정을 보여줍니다.
학년-반 정보 등록/변경 : 자신의 학년-반 정보를 서버에 등록합니다.
시간표 열람을 위해서 최소 1회 등록이 필요하며 이후에도 이 탭에서 변경 가능합니다.
문의 : 정보통신과 20221 정민우'''
            },
            "keyboard": {
                "type": "buttons",
                "buttons": buttons
            }
        })

    elif content_name in classlist:
        tools.addoredituserkey(api_userkey, content_name)
        return JsonResponse({
            "message": {
                "text": "등록되었습니다."
            },
            "keyboard": {
                "type": "buttons",
                "buttons": buttons
            }
        })

    else:
        return JsonResponse({
            "message": {
                "text": "에러! 관리자에게 문의하세요!"
            },
            "keyboard": {
                "type": "buttons",
                "buttons": buttons
            }
        })

def whouse(request):
    return HttpResponse(tools.who_use())
