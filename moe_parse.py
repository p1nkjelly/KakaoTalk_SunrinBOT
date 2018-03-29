# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import datetime
import re
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sunrint_bot.settings")
import django
django.setup()
from chatbot.models import parsedmenu
def parse_menu():
    data = {}
    driver = webdriver.PhantomJS()
    now = datetime.datetime.now()
    parseset = now + datetime.timedelta(days=4)
    parseDate = parseset.strftime('%Y.%m.%d')
    url = ("https://stu.sen.go.kr/sts_sci_md01_001.do?domainCode=B10&schulCode=B100000658&schulCrseScCode=4&schulKndScCode=04&schMmealScCode=2&schYmd=%s" % (parseDate))
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    for num in range(1,6):
        date = ''
        menu = ''
        element = soup.find_all("tr")
        element = element[0].find_all('th')
        try:
            element = element[num+1]
            element = str(element)
            element = element.replace('<th scope="col">', '')
            element = element.replace('</th>', '')
        except:
            element = ""
        date = element
        for i in range(2,4):
            url2 = ("https://stu.sen.go.kr/sts_sci_md01_001.do?domainCode=B10&schulCode=B100000658&schulCrseScCode=4&schulKndScCode=04&schMmealScCode=%d&schYmd=%s" % (i, parseDate))
            driver.get(url2)
            html2 = driver.page_source
            soup2 = BeautifulSoup(html2, 'html.parser')
            element = soup2.find_all("tr")
            element = element[2].find_all('td')
            try:
                element = element[num]
                element = str(element)
                element = element.replace('[', '')
                element = element.replace(']', '')
                element = element.replace('<td class="textC last">', '')
                element = element.replace('<td class="textC">', '')
                element = element.replace('</td>', '')
                element = element.replace('(h)', '')
                element = element.replace('.', '')
                element = element.replace(' ', '')
                element = re.sub(r"\d", "", element)
                element = element.replace('\n', '')
                element = element.replace('<br/>', '\n')
            except:
                element = ""
            if not element:
                element = "급식이 없습니다.\n"
            if i == 2:
                menu += "[중식]\n"+element+"\n"
            elif i == 3:
                menu += "[석식]\n"+element
        data[date] = menu
    return data
    driver.quit()
if __name__=='__main__':
    menu_data = parse_menu()
    for d, m in menu_data.items():
        parsedmenu(day=d, menu=m).save()