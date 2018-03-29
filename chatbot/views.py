# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import datetime
from operator import eq
from .models import parsedmenu
from .models import timetable_mon
from .models import timetable_tue
from .models import timetable_wed
from .models import timetable_thu
from .models import timetable_fri
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
    next = now + datetime.timedelta(days=2)
    nextDate = next.strftime('%Y.%m.%d')
    for result in results:
        if(eq(result.day[:-3], nextDate)):
            nextstr += result.day+'\n'
            nextstr += result.menu
    if not nextstr:
        return isblank(nextDate)
    else:
        return nextstr

def isblank(cheakDate):
    cheakstr = ''
    if not cheakstr:
        cheakstr += cheakDate+'\n'
        cheakstr += "급식이 없습니다."
    return cheakstr

def timetable(c_name):
    timetable_str = ''
    t = ['월', '화', '수', '목', '금', '토', '일']
    r = datetime.datetime.today().weekday()
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


buttons = ["오늘급식","내일급식","다음급식","오늘의 시간표","오늘의 학사일정","도움말"]

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

    if content_name=="오늘급식":
        return JsonResponse({
        "message":{
            "text":today(results)
        },
        "keyboard":{
            "type":"buttons",
            "buttons":buttons
        }
		})

    elif content_name=="내일급식":
        return JsonResponse({
        "message":{
            "text":tomorrow(results)
	 	},
	 	"keyboard":{
			"type":"buttons",
			"buttons":buttons
		}
		})

    elif content_name=="다음급식":
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
			"text":"학년-반을 선택하세요"
	 	},
        "keyboard":{
            "type":"buttons",
            "buttons":classlist
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

    elif content_name=="도움말":
        return JsonResponse({
        "message":{
            "text":'''오늘급식 : 오늘의 급식을 보여줍니다.
내일급식 : 내일의 급식을 보여줍니다.
다음급식 : 2일 후 급식을 보여줍니다.
오늘의 시간표 : 반별 오늘의 시간표를 보여줍니다.
오늘의 학사일정 : 오늘 학교에서 시행되는 행사나 일정을 보여줍니다.
문의 : 정보통신과 20221 정민우'''
        },
        "keyboard":{
            "type":"buttons",
            "buttons":buttons
        }
        })

    elif content_name in classlist:
        return JsonResponse({
            "message": {
                "text":timetable(content_name)
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