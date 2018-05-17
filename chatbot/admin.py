# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import parsedmenu
from .models import timetable_mon
from .models import timetable_tue
from .models import timetable_wed
from .models import timetable_thu
from .models import timetable_fri
from .models import school_cal
from .models import user_key

admin.site.register(parsedmenu)
admin.site.register(timetable_mon)
admin.site.register(timetable_tue)
admin.site.register(timetable_wed)
admin.site.register(timetable_thu)
admin.site.register(timetable_fri)
admin.site.register(school_cal)
admin.site.register(user_key)
