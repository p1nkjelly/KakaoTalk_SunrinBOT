import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sunrint_bot.settings")
import django
django.setup()

from chatbot.models import parsedmenu

def parse_menu():
	req = requests.get('http://www.sunrint.hs.kr/index.do')
	html = req.text
	soup = BeautifulSoup(html, 'html.parser')
	i = 0
	menus = soup.select(
		'p.menu'
		)
	dates = soup.select(
		'dd > p.date'
		)
	data = {}
	for date in dates:
		i += 1
		j = 0
		data[date.text[:-2]] = 0
		for menu in menus:
			data[date.text[:-2]] = menu.text[166:-163]
			j += 1
			if i == j:
				break	
	return data
if __name__=='__main__':
	menu_data = parse_menu()
	parsedmenu.objects.all().delete()
	for d, m in menu_data.items():
		parsedmenu(day=d, menu=m).save()
