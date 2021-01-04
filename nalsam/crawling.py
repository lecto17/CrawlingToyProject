from selenium import webdriver as wd
import time

driver = wd.Chrome(executable_path="chromedriver.exe")
# url = "https://www.naver.com"
url = "http://www.365qt.com/TodaysQT.asp"

driver.get(url)

#페이지 로딩 시간을 기다린다.
time.sleep(1)

content = ""
#.text를 통해 text를 읽어온다.
#날짜
days = driver.find_element_by_id("qtDayTextG").text
day = ""
for d in days.split("\n"):
    day += d+". "
#제목&본문
prefix = driver.find_element_by_id("qtDayText2").text
#본문 말씀
bible_script = driver.find_element_by_class_name("qtBox").text
#주석
description = driver.find_element_by_class_name("script").text
#길잡이
ending = driver.find_elements_by_class_name("box2Content")[1].text
#질문
question_list = driver.find_element_by_xpath("//*[@id='content']/p[2]").text



f = open('C:/Users/hyunoos/Desktop/QT.txt', 'ab')

# tmp = driver.find_element(with_tag_name("p").below(divTitle))
print("*****날짜******")
print(day, end="\n\n")
content = day+"\n"
print("*****TITLE&본문******")
print("제목: "+prefix.split('\n')[0])
content += prefix.split('\n')[0]+"\n"
print("본문: "+prefix.split('\n')[1], end="\n\n")
content += prefix.split('\n')[1]+"\n\n"
print("*****본문 구절*****")
print(bible_script+"\n")
content += bible_script+"\n\n"
print("*****주석*****")
print(description+"\n")
content += description+"\n\n"
print("*****질문*****")
print(question_list)
content += question_list+"\n\n"

print("*****ENDING******")
print(ending)
content += ending+"\n\n"

f.write(content.encode("utf-8"))
f.close()
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