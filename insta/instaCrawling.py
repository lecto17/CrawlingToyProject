from selenium import webdriver as wd
from personal_Info import ID, PWD
import time

driver = wd.Chrome(executable_path="chromedriver.exe")
targetID = "nessussi"   
url = "http://www.instagram.com/"+targetID
LOADING_TIME = 1
driver.get(url)

print("******페이지로딩******")
#페이지 로딩 시간을 기다린다.
time.sleep(LOADING_TIME)

#로그인 버튼을 눌러 로그인을 진행한다.
# href로 1차 시도
# elem = driver.find_element_by_xpath('//a[@href="'+"/accounts/login/?next=%2Fnessussi%2F&amp;source=desktop_nav"+'"]').click()
# class_name 이름으로 2차 시도
# print(driver.find_element_by_class_name("sqdOP")[1].text)
#link_text로 3차 시도
#driver.find_element_by_link_text("로그인").click()
#css_selector를 통한 로그인 진행
driver.find_elements_by_css_selector(".sqdOP.L3NKy.y3zKF")[1].click()
print("******로그인 버튼 클릭1******")

time.sleep(LOADING_TIME)
#ID와 PWD를 넣고 로그인 버튼을 클릭한다.
#driver.find_element_by_name("username").send_keys("mlmtorMan@gmail.com")
# driver.find_elements_by_css_selector("._2hvTZ.pexuQ.zyHYP").send_keys("mlmtorMan@gmail.com")
# print(driver.find_elements_by_css_selector("._2hvTZ.pexuQ.zyHYP")[0].text)
driver.find_element_by_name("username").send_keys(ID)
driver.find_element_by_name("password").send_keys(PWD)
driver.find_element_by_css_selector(".sqdOP.L3NKy.y3zKF").click()
print("******로그인 버튼 클릭2******")

time.sleep(LOADING_TIME)
#로그인 이후 nessussi 검색을 하고 첫번째 
driver.find_element_by_css_selector(".XTCLo.x3qfX").send_keys(targetID)
print("******키워드 검색 완료******")
time.sleep(LOADING_TIME)
#driver.find_element_by_css_selector(".yCE8d.JvDyy").click()
driver.find_elements_by_class_name("z556c")[0].click()
print("******리스트 중 첫번째 메뉴 클릭******")
# driver.find_element_by_link_text("nessussi").click()


time.sleep(LOADING_TIME)
# 스크롤 높이 가져옴
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # 끝까지 스크롤 다운
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 3초 대기
    time.sleep(LOADING_TIME+1)

    # 스크롤 다운 후 스크롤 높이 다시 가져옴
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height