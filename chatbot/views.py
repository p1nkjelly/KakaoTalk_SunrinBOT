# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import datetime
from operator import eq
from .models import parsedmenu

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
	tmp = 9999
	now = datetime.datetime.now()
	tomorrow = now + datetime.timedelta(days=1)
	tomorrowDate = tomorrow.strftime('%Y.%m.%d')
	for result in results:
		if (eq(result.day[:-3], tomorrowDate)):
			nextstr += result.day + '\n'
			nextstr += result.menu
	if not nextstr:
		for result in results:
			if tmp > int(result.day[8:-3]):
				nextstr = ''
				tmp = int(result.day[8:-3])
				nextstr += result.day + '\n'
				nextstr += result.menu
		if not nextstr:
			return isblank("DataBase에 저장된")
		else:
			return nextstr
	else:
		return nextstr

	
def isblank(cheakDate):
	cheakstr = ''
	if not cheakstr:
		cheakstr += cheakDate+'\n'
		cheakstr += "급식이 없습니다."
	return cheakstr

classlist = []
for i in range(1,4):	
	for j in range(1,13):
		classlist.append(str(i)+"-"+str(j))


buttons = ["오늘급식","내일급식","다음급식","시간표","오늘의 학사일정","도움말"]

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
		return JsonResponse(
		{
	 	"message":{
			"text":today(results)
	 	},
	 	"keyboard":{
			"type":"buttons",
			"buttons":buttons
		 }
		}
		)

	elif content_name=="내일급식":
		return JsonResponse(
		{
	 	"message":{
			"text":tomorrow(results)
	 	},
	 	"keyboard":{
			"type":"buttons",
			"buttons":buttons
		 }
		}
		)

	elif content_name=="다음급식":
		return JsonResponse(
		{
	 	"message":{
			"text":next(results)
	 	},
	 	"keyboard":{
			"type":"buttons",
			"buttons":buttons
		 }
		}
		)

	elif content_name=="시간표":
		return JsonResponse(
		{
	 	"message":{
			"text":"반-학년을 선택하세요"
	 	},
	 	"keyboard":{
			"type":"buttons",
			"buttons":classlist
		 }
		}
		)

	elif content_name=="오늘의 학사일정":
		return JsonResponse(
		{
	 	"message":{
			"text":"오늘의 학사일정입니다."
	 	},
	 	"keyboard":{
			"type":"buttons",
			"buttons":buttons
		 }
		}
		)

	elif content_name=="도움말":
		return JsonResponse(
		{
		"message":{
			"text":'''오늘급식 : 오늘의 급식을 보여줍니다.
내일급식 : 내일의 급식을 보여줍니다.
다음급식 : 오늘과 내일 급식이 모두 없을 때 그 다음의 급식을 보여줍니다. 내일 급식이 존재한다면 내일 급식을 보여줍니다.
시간표 : 반별 오늘의 시간표를 보여줍니다.
오늘의 학사일정 : 오늘 학교에서 시행되는 행사나 일정을 보여줍니다.
문의 : 정보통신과 20221 정민우'''
		 },
		"keyboard":{
			"type":"buttons",
			"buttons":buttons
	 	 }
		}
		)

	else :
		return JsonResponse(
		{
	 	"message":{
			"text":"노동중..."
	 	},
	 	"keyboard":{
			"type":"buttons",
			"buttons":buttons
		 }
		}
		)
