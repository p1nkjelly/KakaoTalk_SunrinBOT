# -*- coding: utf-8 -*-
import csv
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sunrint_bot.settings")
import django
django.setup()
from chatbot.models import school_cal

def save():
    data = {}
    f = open('school_cal.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)
    j = 1
    for line in rdr:
        for i in range(1,13):
            if i+2 <= 12:
                data[str(i + 2).zfill(2)+"-"+str(j).zfill(2)] = line[i]
            else:
                data[str(i - 10).zfill(2) + "-" + str(j).zfill(2)] = line[i]
        j += 1
    return data
    f.close()

if __name__=='__main__':
    school_cal_data = save()
    school_cal.objects.all().delete()
    for date, data in school_cal_data.items():
        school_cal(date=date, data=data).save()
