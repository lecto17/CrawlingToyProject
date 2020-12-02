from selenium import webdriver as wd
import time

driver = wd.Chrome(executable_path="chromedriver.exe")
url = "http://www.instagram.com/nessussi"

driver.get(url)

#페이지 로딩 시간을 기다린다.
time.sleep(6)

#로그인을 진행한다.
# href로 1차 시도
# elem = driver.find_element_by_xpath('//a[@href="'+"/accounts/login/?next=%2Fnessussi%2F&amp;source=desktop_nav"+'"]').click()
# class_name 이름으로 2차 시도
# print(driver.find_element_by_class_name("sqdOP")[1].text)
#link_text로 3차 시도
driver.find_element_by_link_text("로그인").click()

SCROLL_PAUSE_SEC = 1

# 스크롤 높이 가져옴
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # 끝까지 스크롤 다운
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 1초 대기
    time.sleep(SCROLL_PAUSE_SEC)

    # 스크롤 다운 후 스크롤 높이 다시 가져옴
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height