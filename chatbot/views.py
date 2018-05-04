# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import datetime
from operator import eq
from .models import *

results = parsedmenu.objects.all()

def today(results):
    todaystr = ''
    now = datetime.datetime.now()
    nowDate = now.strftime('%Y.%m.%d')
    for result in results:
        if(eq(result.day[:-3], nowDate)):
            todaystr += result.day+'\n'
            todaystr += result.menu
    if not todaystr:
        return isblank(nowDate)
    else:
        return todaystr

def tomorrow(results):
    tomorrowstr = ''
    now = datetime.datetime.now()
    tomorrow = now + datetime.timedelta(days=1)
    tomorrowDate = tomorrow.strftime('%Y.%m.%d')
    for result in results:
        if(eq(result.day[:-3], tomorrowDate)):
            tomorrowstr += result.day+'\n'
            tomorrowstr += result.menu
    if not tomorrowstr:
        return isblank(tomorrowDate)
    else:
        return tomorrowstr

def next(results):
    nextstr = ''
    now = datetime.datetime.now()
    i = 2
    while(not nextstr and i<8):
        for result in results:
            next = now + datetime.timedelta(days=i)
            nextDate = next.strftime('%Y.%m.%d')
            if(eq(result.day[:-3], nextDate)):
                if("급식이 없습니다." in  result.menu):
                    nextstr = ''
                else:
                    nextstr += result.day+'\n'
                    nextstr += result.menu
        i += 1

    if not nextstr:
        return isblank("이번주에 다음")
    else:
        return nextstr

def isblank(cheakDate):
    cheakstr = ''
    if not cheakstr:
        cheakstr += cheakDate+'\n'
        cheakstr += "급식이 없습니다."
    return cheakstr

def addoredituserkey(userkey_add, classdata):
    try:
        user_key.objects.filter(key=userkey_add).delete()
        user_key(key=userkey_add, c_data=classdata).save()
    except:
        user_key(key=userkey_add, c_data=classdata).save()

def userinfo(userkey, daynum):
    for userdata in user_key.objects.filter(key=userkey):
        if(eq(userdata.key, userkey)):
            return timetable(userdata.c_data, daynum)
    return "먼저 학년-반 정보를 등록해주세요."

def timetable(c_name, daynum):
    timetable_str = ''
    t = ['월', '화', '수', '목', '금', '토', '일']
    r = datetime.datetime.today().weekday() + daynum
    if t[r] == '월':
        for timetable in timetable_mon.objects.all():
            if(eq(c_name, timetable.c_name)):
                timetable_str += timetable.c_name+'반 '+t[r]+'요일 시간표\n\n'
                timetable_str += timetable.t_table
    elif t[r] == '화':
        for timetable in timetable_tue.objects.all():
            if(eq(c_name, timetable.c_name)):
                timetable_str += timetable.c_name+'반 '+t[r]+'요일 시간표\n\n'
                timetable_str += timetable.t_table
    elif t[r] == '수':
        for timetable in timetable_wed.objects.all():
            if(eq(c_name, timetable.c_name)):
                timetable_str += timetable.c_name+'반 '+t[r]+'요일 시간표\n\n'
                timetable_str += timetable.t_table
    elif t[r] == '목':
        for timetable in timetable_thu.objects.all():
            if(eq(c_name, timetable.c_name)):
                timetable_str += timetable.c_name+'반 '+t[r]+'요일 시간표\n\n'
                timetable_str += timetable.t_table
    elif t[r] == '금':
        for timetable in timetable_fri.objects.all():
            if(eq(c_name, timetable.c_name)):
                timetable_str += timetable.c_name+'반 '+t[r]+'요일 시간표\n\n'
                timetable_str += timetable.t_table
    else:
        timetable_str += "즐거운 주말 보내세요~"
    return timetable_str

classlist = []
for i in range(1,4):	
    for j in range(1,13):
        classlist.append(str(i)+"-"+str(j))


buttons = ["오늘의 급식","오늘의 시간표","내일의 급식","내일의 시간표","다음 급식","오늘의 학사일정","학년-반 정보 등록/변경","도움말"]

def keyboard(request):
    return JsonResponse({
        "type":"buttons",
        "buttons":buttons
    })

@csrf_exempt
def message(request):
    json_str = (request.body).decode('utf-8')
    received_json = json.loads(json_str)
    content_name = received_json['content']
    api_userkey = received_json['user_key']

    if content_name=="오늘의 급식":
        return JsonResponse({
        "message":{
            "text":today(results)
        },
        "keyboard":{
            "type":"buttons",
            "buttons":buttons
        }
		})

    elif content_name=="내일의 급식":
        return JsonResponse({
        "message":{
            "text":tomorrow(results)
	 	},
	 	"keyboard":{
			"type":"buttons",
			"buttons":buttons
		}
		})

    elif content_name=="다음 급식":
        return JsonResponse({
        "message":{
            "text":next(results)
        },
        "keyboard":{
            "type":"buttons",
            "buttons":buttons
		}
		})

    elif content_name=="오늘의 시간표":
        return JsonResponse({
        "message":{
			"text":userinfo(api_userkey, 0)
	 	},
        "keyboard":{
            "type":"buttons",
            "buttons":buttons
		}
        })
    elif content_name == "내일의 시간표":
        return JsonResponse({
            "message": {
                "text": userinfo(api_userkey, 1)
            },
            "keyboard": {
                "type": "buttons",
                "buttons": buttons
            }
        })

    elif content_name=="오늘의 학사일정":
        return JsonResponse({
        "message":{
            "text":"학사일정 작업중..."
        },
        "keyboard":{
            "type":"buttons",
            "buttons":buttons
        }
	    })

    elif content_name == "학년-반 정보 등록/변경":
        return JsonResponse({
            "message": {
                "text": "자신의 학년-반을 선택하세요."
            },
            "keyboard":{
            "type":"buttons",
            "buttons":classlist
		    }
        })

    elif content_name=="도움말":
        return JsonResponse({
        "message":{
            "text":'''오늘급식 : 오늘의 급식을 보여줍니다.
내일급식 : 내일의 급식을 보여줍니다.
다음급식 : 다음 급식이 존재하는 날의 급식을 보여줍니다.
오늘의 시간표 : 반별 오늘의 시간표를 보여줍니다.
내일의 시간표 : 반별 내일의 시간표를 보여줍니다.
오늘의 학사일정 : 오늘 학교에서 시행되는 행사나 일정을 보여줍니다.
학년-반 정보 등록/변경 : 자신의 학년-반 정보를 서버에 등록합니다.
시간표 열람을 위해서 최소 1회 등록이 필요하며 이후에도 이 탭에서 변경 가능합니다.
문의 : 정보통신과 20221 정민우'''
        },
        "keyboard":{
            "type":"buttons",
            "buttons":buttons
        }
        })

    elif content_name in classlist:
        addoredituserkey(api_userkey, content_name)
        return JsonResponse({
            "message": {
                "text":"등록되었습니다."
            },
            "keyboard": {
                "type": "buttons",
                "buttons": buttons
            }
        })

    else :
        return JsonResponse({
        "message":{
            "text":"에러! 관리자에게 문의하세요!"
        },
        "keyboard":{
            "type":"buttons",
            "buttons":buttons
		}
		})