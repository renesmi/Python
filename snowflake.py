from selenium import webdriver
from bs4 import BeautifulSoup
import re

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
## Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
driver = webdriver.Chrome('C:/Users/sumin/Downloads/chromedriver',chrome_options=options)
driver.implicitly_wait(3)
## url에 접근한다.
driver.get('https://play.blizzard.kr/ko/overwatch/snowshop9')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
notices = soup.select('span.snowflake-cost')
print(notices)

for n in notices:
	ss=str(notices)
	a=ss.split('>')
	a1=a[7].split('<')
	print(a1[0])

    #print(type(notices))
    #print(notices.split('>')[0])


    #print(result)
   
print("끝")
