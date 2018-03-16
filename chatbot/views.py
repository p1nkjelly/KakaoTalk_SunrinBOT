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
		return todaystr.replace(",", "\n")

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
		return tomorrowDate.replace(",", "\n")
		flag = 1

def next(results):
	nextstr = ''
	now = datetime.datetime.now()
	nowDate = now.strftime('%Y.%m.%d')
	tomorrow = now + datetime.timedelta(days=1)
	tomorrowDate = tomorrow.strftime('%Y.%m.%d')
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
		return nextstr.replace(",", "\n")
	
def isblank(cheakDate):
	cheakstr = ''
	if not cheakstr:
		cheakstr += cheakDate+'\n'
		cheakstr += "급식이 없습니다."
	return cheakstr

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
			"buttons":["1-1","1-2","1-3","1-4","1-5","1-6","1-7","1-8","1-9","1-10","1-11","1-12","2-1","2-2","2-3","2-4","2-5","2-6","2-7","2-8","2-9","2-10","2-11","2-12","3-1","3-2","3-3","3-4","3-5","3-6","3-7","3-8","3-9","3-10","3-11","3-12"]
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

