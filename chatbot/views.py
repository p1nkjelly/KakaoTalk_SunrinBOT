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
flag = 0
classlist = []

def today(results):
	todaystr = ''
	now = datetime.datetime.now()
	nowDate = now.strftime('%Y.%m.%d')
	for result in results:
		if(eq(result.day, nowDate)):
			todaystr += result.day+'\n'
			todaystr += result.menu
	if not todaystr:
		return isblank(nowDate)
	else:
		return todaystr.replace(",", "\n")[:-11]+"\n"+todaystr[-11:]

def tomorrow(results):
	tomorrowstr = ''
	now = datetime.datetime.now()
	tomorrow = now + datetime.timedelta(days=1)
	tomorrowDate = tomorrow.strftime('%Y.%m.%d')
	for result in results:
		if(eq(result.day, tomorrowDate)):
			tomorrowstr += result.day+'\n'
			tomorrowstr += result.menu
	if not tomorrowstr:
		return isblank(tomorrowDate)
		flag = 0
	else:
		return tomorrowstr.replace(",", "\n")[:-11]+"\n"+tomorrowstr[-11:]
		flag = 1

def next(results):
	nextstr = ''
	tmp = 9999
	if flag:
		return tomorrow(results)
	for result in results:
		if tmp>int(result.day[-2:]):
			nextstr = ''
			tmp = int(result.day[-2:])
			nextstr += result.day+'\n'
			nextstr += result.menu+'\n'
	if not nextstr:
		return isblank()
	else:
		return nextstr.replace(",", "\n")[:-11]+"\n"+nextstr[-11:]
	
def isblank(cheakDate):
	cheakstr = ''
	if not cheakstr:
		cheakstr += cheakDate+'\n'
		cheakstr += "급식이 없습니다."
	return cheakstr

for i in range(1,4):	
	for j in range(1,13):
		classlist.append(str(i)+"-"+str(j))

def keyboard(request):
	return JsonResponse({
		"type":"buttons",
		"buttons":["오늘급식","내일급식","다음급식","시간표","오늘의 학사일정"]
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
			"buttons":["오늘급식","내일급식","다음급식","시간표","오늘의 학사일정"]
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
			"buttons":["오늘급식","내일급식","다음급식","시간표","오늘의 학사일정"]
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
			"buttons":["오늘급식","내일급식","다음급식","시간표","오늘의 학사일정"]
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
			"buttons":["오늘급식","내일급식","다음급식","시간표","오늘의 학사일정"]
		 }
		}
		)

	else :
		return JsonResponse(
		{
	 	"message":{
			"text":"ERROR"
	 	},
	 	"keyboard":{
			"type":"buttons",
			"buttons":["오늘급식","내일급식","다음급식","시간표","오늘의 학사일정"]
		 }
		}
		)
