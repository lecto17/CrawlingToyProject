from selenium import webdriver as wd
import time

driver = wd.Chrome(executable_path="chromedriver.exe")
# url = "https://www.naver.com"
url = "http://www.365qt.com/TodaysQT.asp"

driver.get(url)

#페이지 로딩 시간을 기다린다.
time.sleep(1)

#.text를 통해 text를 읽어온다.
#날짜
day = driver.find_element_by_id("qtDayTextG").text
#제목&본문
prefix = driver.find_element_by_id("qtDayText2").text
#길잡이
ending = driver.find_elements_by_class_name("box2Content")[1].text

# tmp = driver.find_element(with_tag_name("p").below(divTitle))
print("*****날짜******")
print(day, end="\n\n")
print("*****TITLE&본문******")
print("제목: "+prefix.split('\n')[0])
print("본문: "+prefix.split('\n')[1], end="\n\n")

print("*****ENDING******")
print(ending)

# time.sleep(2)

# elem = driver.find_element_by_name("query")
# elem.send_keys("날마다 솟는 샘물")
# elem.submit()

# driver.find_element_by_class_name("source_url").click()
# time.sleep(2)

#xPath로 element 찾기, 클래스 이름으로 찾을 경우 여러 개의 element를 가져올 수 있지만 xPath의 경우 하나의 element 리턴
# driver.find_element_by_xpath("//*[@id=\"mA01\"]/p/a").click()
#driver.find_element_by_css_selector("#textBlackBig")[0].click()

#with_tag_name는 selenium4부터 지원
# qt_div = driver.find_element_by_id("mA01")
# driver.find_element(with_tag_name("a").near(qt_div)).click()

#link 걸어놓은 주소 중 해당하는 element를 반환
#driver.find_element_by_xpath('//a[@href="'++'"]')

driver.close()