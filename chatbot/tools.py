# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from operator import eq
from .models import *
import datetime

def today():
    todaystr = ''
    now = datetime.datetime.now()
    nowDate = now.strftime('%Y.%m.%d')
    for result in parsedmenu.objects.filter(day__startswith=nowDate):
        if eq(result.day[:-3], nowDate):
            todaystr += result.day+'\n'
            todaystr += result.menu
    if not todaystr:
        return isblank(nowDate)
    else:
        return todaystr

def tomorrow():
    tomorrowstr = ''
    now = datetime.datetime.now()
    tomorrow = now + datetime.timedelta(days=1)
    tomorrowDate = tomorrow.strftime('%Y.%m.%d')
    for result in parsedmenu.objects.filter(day__startswith=tomorrowDate):
        if eq(result.day[:-3], tomorrowDate):
            tomorrowstr += result.day+'\n'
            tomorrowstr += result.menu
    if not tomorrowstr:
        return isblank(tomorrowDate)
    else:
        return tomorrowstr

def next():
    nextstr = ''
    now = datetime.datetime.now()
    i = 2
    while not nextstr and i < 8:
        next = now + datetime.timedelta(days=i)
        nextDate = next.strftime('%Y.%m.%d')
        for result in parsedmenu.objects.filter(day__startswith=nextDate):
            if eq(result.day[:-3], nextDate):
                if "급식이 없습니다." in result.menu:
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
        if eq(userdata.key, userkey):
            return timetable(userdata.c_data, daynum)
    return "먼저 학년-반 정보를 등록해주세요."

def timetable(c_name, daynum):
    timetable_str = ''
    t = ['월', '화', '수', '목', '금', '토', '일']
    r = datetime.datetime.today().weekday() + daynum
    if r == 7:
        r = 0
    if t[r] == '월':
        for timetable in timetable_mon.objects.filter(c_name=c_name):
            if eq(c_name, timetable.c_name):
                timetable_str += timetable.c_name+'반 '+t[r]+'요일 시간표\n\n'
                timetable_str += timetable.t_table
    elif t[r] == '화':
        for timetable in timetable_tue.objects.filter(c_name=c_name):
            if eq(c_name, timetable.c_name):
                timetable_str += timetable.c_name+'반 '+t[r]+'요일 시간표\n\n'
                timetable_str += timetable.t_table
    elif t[r] == '수':
        for timetable in timetable_wed.objects.filter(c_name=c_name):
            if eq(c_name, timetable.c_name):
                timetable_str += timetable.c_name+'반 '+t[r]+'요일 시간표\n\n'
                timetable_str += timetable.t_table
    elif t[r] == '목':
        for timetable in timetable_thu.objects.filter(c_name=c_name):
            if eq(c_name, timetable.c_name):
                timetable_str += timetable.c_name+'반 '+t[r]+'요일 시간표\n\n'
                timetable_str += timetable.t_table
    elif t[r] == '금':
        for timetable in timetable_fri.objects.filter(c_name=c_name):
            if eq(c_name, timetable.c_name):
                timetable_str += timetable.c_name+'반 '+t[r]+'요일 시간표\n\n'
                timetable_str += timetable.t_table
    else:
        timetable_str += "즐거운 주말 보내세요~"
    return timetable_str
