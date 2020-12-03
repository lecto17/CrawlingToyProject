from urllib.request import urlopen
from urllib.parse import quote_plus # 아스키 코드로 변환시켜준다.
from bs4 import BeautifulSoup
from selenium import webdriver as wd
from personal_Info import ID, PWD
import time


def scrollDown():
    # 스크롤 높이 가져옴
    f = open("C:/Users/hyunoos/Desktop/img_list.txt", "w")
    last_height = driver.execute_script("return document.body.scrollHeight")
    # n = 1
    origin_path = ""

    
    while True:
        # 끝까지 스크롤 다운
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        html = driver.page_source
        soup = BeautifulSoup(html)

        # select는 페이지에 있는 정보를 다 가져 온다.
        # 클래스가 여러 개면 기존 클래스의 공백을 없애고 .으로 연결시켜 주어야 한다.
        insta = soup.select('.v1Nh3.kIKUG._bz0w')
        print("len: "+ str(len(insta)))
        n = 1

        # 이미지 하나만 가져올 게 아니라 여러 개를 가져올 것이므로 반복문을 쓴다.
        for i in insta:
            # 인스타 주소에 i번 째의 a태그의 href 속성을 더하여 출력한다.
            origin_path = 'https://www.instagram.com' + i.a['href']
            f.write(origin_path+"\n")
            # print(origin_path)
            # 인스타 페이지 소스에서 이미지에 해당하는 클래스의 이미지 태그의 src 속성을 imgUrl에 저장한다.
            imgUrl = i.select_one('.KL4Bh').img['src']
            # with urlopen(imgUrl) as f:
            #     # img라는 폴더 안에 programmer(n).jpg 파일을 저장한다.
            #     # 텍스트 파일이 아니기 때문에 w(write)만 쓰면 안되고 binary 모드를 추가시켜야 한다.
            #     with open(path+'/img/' + targetID + str(n) + '.jpg', "wb") as h:
            #         # f를 읽고 img에 저장한다.
            #         img = f.read()
            #         # h에 위 내용을 쓴다.
            #         h.write(img)
            # print(n)
            f.write(str(n)+"\n")
            # 계속 programmer 1에 덮어쓰지 않도록 1을 증가시켜 준다
            n += 1     
            # print(imgUrl)
            f.write(imgUrl+"\n\n")
            # 출력한 걸 보았을 때 구분하기 좋도록 빈 줄을 추가시킨다.
            # print()

        # 3초 대기
        time.sleep(5)

        # 스크롤 다운 후 스크롤 높이 다시 가져옴
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:            
            break
        last_height = new_height

driver = wd.Chrome(executable_path="chromedriver.exe")
targetID = "nessussi"   
url = "http://www.instagram.com/"+targetID
path = "C:/Users/hyunoos/Desktop/CrawlingToyProject/insta"
LOADING_TIME = 2
print("url: "+ url)
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
'''
갑자기 이 부분이 사라짐. 원래 url('https://www.instagram.com/nessussi')로 접근하면 개인 페이지가 떠야 되는데
지금은 자동으로 ID / PWD 작성하는 곳으로 redirection 되고 있음
갑자기 왜 그러는건지..

# driver.find_elements_by_css_selector(".sqdOP.L3NKy.y3zKF")[1].click()
# print("******로그인 버튼 클릭1******")

# time.sleep(LOADING_TIME)
'''
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
scrollDown()

# pictures = driver.find_elements_by_class_name("_9AhH0")
# driver.find_elements_by_class_name("_9AhH0")[0].click()
# time.sleep(LOADING_TIME)
# print(driver.find_elements_by_css_selector("._9AhH0")[0].get_attribute("src"))
# print("length: "+ str(len(pictures)))


#사진 저장하기
# img_url = "https://betanews.com/wp-content/uploads/2017/09/firefox-logo.jpg"
# img_name = os.path.basename(img_url)
# urllib.request.urlretrieve(img_url,img_name)

