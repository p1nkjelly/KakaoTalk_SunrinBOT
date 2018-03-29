# -*- coding: utf-8 -*-
import csv
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sunrint_bot.settings")
import django
django.setup()
from chatbot.models import timetable_mon
from chatbot.models import timetable_tue
from chatbot.models import timetable_wed
from chatbot.models import timetable_thu
from chatbot.models import timetable_fri
def mon():
    data = {}
    f = open('sunrin-mon.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)
    for line in rdr:
        tmp = ''
        for i in range(1,8):
            tmp += str(i)+"교시 : "+line[i]+"\n"
        data[line[0]] = tmp
    return data
    f.close()
def tue():
    data = {}
    f = open('sunrin-tue.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)
    for line in rdr:
        tmp = ''
        for i in range(1,8):
            tmp += str(i)+"교시 : "+line[i]+"\n"
        data[line[0]] = tmp
    return data
    f.close()
def wed():
    data = {}
    f = open('sunrin-wed.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)
    for line in rdr:
        tmp = ''
        for i in range(1,8):
            tmp += str(i)+"교시 : "+line[i]+"\n"
        data[line[0]] = tmp
    return data
    f.close()
def thu():
    data = {}
    f = open('sunrin-thu.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)
    for line in rdr:
        tmp = ''
        for i in range(1,8):
            tmp += str(i)+"교시 : "+line[i]+"\n"
        data[line[0]] = tmp
    return data
    f.close()
def fri():
    data = {}
    f = open('sunrin-fri.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)
    for line in rdr:
        tmp = ''
        for i in range(1,7):
            tmp += str(i)+"교시 : "+line[i]+"\n"
        data[line[0]] = tmp
    return data
    f.close()
if __name__=='__main__':
    time_data_mon = mon()
    timetable_mon.objects.all().delete()
    for c, t in time_data_mon.items():
        timetable_mon(c_name=c, t_table=t).save()

    time_data_tue = tue()
    timetable_tue.objects.all().delete()
    for c, t in time_data_tue.items():
        timetable_tue(c_name=c, t_table=t).save()

    time_data_wed = wed()
    timetable_wed.objects.all().delete()
    for c, t in time_data_wed.items():
        timetable_wed(c_name=c, t_table=t).save()

    time_data_thu = thu()
    timetable_thu.objects.all().delete()
    for c, t in time_data_thu.items():
        timetable_thu(c_name=c, t_table=t).save()

    time_data_fri = fri()
    timetable_fri.objects.all().delete()
    for c, t in time_data_fri.items():
        timetable_fri(c_name=c, t_table=t).save()