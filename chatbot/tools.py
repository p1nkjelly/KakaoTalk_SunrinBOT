# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from operator import eq
from .models import *
import datetime


def str_date_return(day, str_type):
    now = datetime.datetime.now()
    dayinfo = now + datetime.timedelta(days=day)
    if str_type == 1:
        DateStr = dayinfo.strftime('%Y.%m.%d')
    elif str_type == 2:
        DateStr = dayinfo.strftime('%m-%d')
    else:
        DateStr = "error"
    return DateStr


def day_name_return(shift):
    day_name = ['월', '화', '수', '목', '금', '토', '일']
    day_num = datetime.datetime.today().weekday() + shift
    if day_num >= 7:
        while day_num >= 7:
            day_num -= 7
        return day_name[day_num]
    else:
        return day_name[day_num]


def today_menu():
    todaystr = ''
    nowDate = str_date_return(0, 1)
    for result in parsedmenu.objects.filter(day__startswith=nowDate):
        if eq(result.day[:-3], nowDate):
            todaystr += result.day+'\n'+result.menu
    if not todaystr:
        return isblank(nowDate+"("+day_name_return(0)+")")
    else:
        return todaystr


def tomorrow_menu():
    tomorrowstr = ''
    tomorrowDate = str_date_return(1, 1)
    for result in parsedmenu.objects.filter(day__startswith=tomorrowDate):
        if eq(result.day[:-3], tomorrowDate):
            tomorrowstr += result.day+'\n'+result.menu
    if not tomorrowstr:
        return isblank(tomorrowDate+"("+day_name_return(1)+")")
    else:
        return tomorrowstr


def next_menu():
    nextstr = ''
    i = 2
    while not nextstr and i < 8:
        nextDate = str_date_return(i, 1)
        for result in parsedmenu.objects.filter(day__startswith=nextDate):
            if eq(result.day[:-3], nextDate):
                if "[중식]\n급식이 없습니다.\n\n[석식]\n급식이 없습니다." in result.menu:
                    nextstr = ''
                else:
                    nextstr += result.day+'\n'+result.menu
        i += 1
    if not nextstr:
        return isblank("이번주에 다음")
    else:
        return nextstr


def isblank(cheakdate):
    cheakstr = ''
    if not cheakstr:
        cheakstr += cheakdate+'\n'+"급식이 없습니다."
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
    requested_day_name = day_name_return(daynum)
    if requested_day_name == '월':
        for data_timetable_mon in timetable_mon.objects.filter(c_name=c_name):
            if eq(c_name, data_timetable_mon.c_name):
                timetable_str += \
                    data_timetable_mon.c_name + '반 ' + requested_day_name + '요일 시간표\n\n' + data_timetable_mon.t_table
    elif requested_day_name == '화':
        for data_timetable_tue in timetable_tue.objects.filter(c_name=c_name):
            if eq(c_name, data_timetable_tue.c_name):
                timetable_str += \
                    data_timetable_tue.c_name + '반 ' + requested_day_name + '요일 시간표\n\n' + data_timetable_tue.t_table
    elif requested_day_name == '수':
        for data_timetable_wed in timetable_wed.objects.filter(c_name=c_name):
            if eq(c_name, data_timetable_wed.c_name):
                timetable_str += \
                    data_timetable_wed.c_name + '반 ' + requested_day_name + '요일 시간표\n\n' + data_timetable_wed.t_table
    elif requested_day_name == '목':
        for data_timetable_thu in timetable_thu.objects.filter(c_name=c_name):
            if eq(c_name, data_timetable_thu.c_name):
                timetable_str += \
                    data_timetable_thu.c_name + '반 ' + requested_day_name + '요일 시간표\n\n' + data_timetable_thu.t_table
    elif requested_day_name == '금':
        for data_timetable_fri in timetable_fri.objects.filter(c_name=c_name):
            if eq(c_name, data_timetable_fri.c_name):
                timetable_str += \
                    data_timetable_fri.c_name + '반 ' + requested_day_name + '요일 시간표\n\n' + data_timetable_fri.t_table
    else:
        timetable_str += "즐거운 주말 보내세요~"
    return timetable_str


def school_cal_print():
    school_cal_str = ''
    print_cnt = 0
    while_cnt = 0
    max_date = datetime.datetime(2019, 2, 14) - datetime.datetime.now()
    max_date = max_date.days
    while print_cnt < 10:
        Date = str_date_return(while_cnt, 2)
        for cal_data in school_cal.objects.filter(date=Date):
            if eq(cal_data.date, Date):
                if not cal_data.data:
                    school_cal_str += ''
                else:
                    school_cal_str += Date[:2]+"월 "+Date[3:]+"일 (" + day_name_return(while_cnt) + ")\n" + cal_data.data + "\n\n"
                    print_cnt += 1
        if while_cnt >= max_date+1:
            break
        else:
            while_cnt += 1
    if not school_cal_str:
        return "DB에 학사일정이 없습니다."
    else:
        return school_cal_str[:-2]


def who_use():
    counter = 0
    total = 0
    returnstr = ''
    for i in range(1, 4):
        for j in range(1, 13):
            for data in user_key.objects.all():
                grade = data.c_data[:1]
                _class = data.c_data[2:]
                if grade == str(i):
                    if _class == str(j):
                        counter += 1
            returnstr += (str(i) + " - " + str(j) + " : " + str(counter) + "<br>")
            total += counter
            counter = 0
    returnstr += ("total : " + str(total))
    return returnstr
