import requests
from bs4 import BeautifulSoup


req = requests.get('http://www.sunrint.hs.kr/34974/subMenu.do')
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