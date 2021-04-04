"""
Auther : Daeseong Lee
Last Modification : 2021.04.04
bhban@kakao.com
https://github.com/mbc8949/pixabay_crawling_1
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def crawling(keyword, numImages, result_dir):
    # 웹드라이버 실행
    options = Options()
    options.add_argument("--windows-size=1024, 768")
    #options.add_argument("headless")
    driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=options)

    # 이미지 검색 url
    url = 'https://pixabay.com/images/search/'

    # 이미지 검색하기
    driver.get(url + keyword)

    # 이미지 검색 영역의 xpath
    xpath = '//*[@id="content"]/div/div[3]/div'
    #// *[ @ id = "content"] / div / div[3]

    # 100장 이하 이미지를 요구받은 경우
    if numImages <= 100:
        image_area = driver.find_element_by_xpath(xpath)
        image_elements = image_area.find_elements_by_tag_name("img")
        for i in range(numImages):
            image_elements[i].screenshot(result_dir + "/" + str(time.time()) + ".png")
    # 100장 이상을 요구받은 경우
    else:
        while numImages > 0:
            image_area = driver.find_element_by_xpath(xpath)
            image_elements = image_area.find_elements_by_tag_name("img")
            for i in range(len(image_elements)):
                image_elements[i].screenshot(result_dir + "/" + str(time.time()) + ".png")
                numImages -= 1
                if i == len(image_elements) - 1:
                    next_button = driver.find_element_by_partial_link_text("Next page")
                    next_button.click()
                    time.sleep(5)





