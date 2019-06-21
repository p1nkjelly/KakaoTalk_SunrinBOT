from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
#chrome_options.add_argument("--headless")

driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://sunrint.hs.kr/65129/subMenu.do')

table = driver.find_element_by_xpath("//*[@class='calendar_schedule monthly']")
tr = table.find_element_by_tag_name("tbody").find_elements_by_tag_name("tr")

for r in tr:
    td = r.find_elements_by_tag_name("td")
    for d in td:
        try:
            a = d.find_elements_by_tag_name("a")
        except:
            continue

        for a_ in a:
            a_.click()

            driver.implicitly_wait(1)
            t = driver.find_element_by_xpath("//*[@id='detailFrm']").find_element_by_tag_name("table").find_element_by_tag_name("tbody").find_elements_by_tag_name("tr")

            day = t[1].find_element_by_class_name('ta_l').text
            type = t[2].text.split(" ")[1]
            food = t[3].text.split(" ")[1].replace(",","\n")
            driver.find_element_by_xpath('//*[@id="divLayerMlsvPopup"]/div/div/div/button').click()
            print(type, day, food)

driver.quit()
