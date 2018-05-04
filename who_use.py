# -*- coding: utf-8 -*-
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sunrint_bot.settings")
import django
django.setup()
from chatbot.models import user_key
counter = 0
total = 0
for i in range(1,4):
    for j in range(1,13):
        for data in user_key.objects.all():
            grade = data.c_data[:1]
            _class = data.c_data[2:]
            if grade == str(i):
                if _class == str(j):
                    counter += 1
        print(str(i)+" - "+str(j)+" : "+str(counter))
        total += counter
        counter = 0
print("total : "+str(total))