from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Class 4
# Task 1
# driver = webdriver.Chrome(executable_path="C:\\Users\\Itay Zrihan\\Desktop\\ChromeDriver.exe")
# driver.get("http://walla.co.il")
# driver = webdriver.Firefox(executable_path="C:\\Users\\Itay Zrihan\\Desktop\\FirefoxDriver.exe")
# driver.get("http://ynet.co.il")
# Task 2
# driver = webdriver.Chrome(executable_path="C:\\Users\\Itay Zrihan\\Desktop\\ChromeDriver.exe")
# driver.get("http://walla.co.il")
# driver.current_url
# driver.find_element_by_name("וואלה! NEWS")
# driver.refresh()
# walla2 = driver.find_element_by_class_name("main-logo")
# walla = driver.title
# if walla == walla2:
#     print("compare")
# Task 3
# driver = webdriver.Chrome(executable_path="C:\\Users\\Itay Zrihan\\Desktop\\ChromeDriver.exe")
# driver.get("http://walla.co.il")
# driver.find_element_by_class_name("css-kcnid8")
# driver.find_element_by_id("main-footer")
# לא אלמנטים משתנים לפי פעולות שמתבצעות באתר

# Task 4
# driver = webdriver.Chrome(executable_path="C:\\Users\\Itay Zrihan\\Desktop\\ChromeDriver.exe")
# driver.get("https://translate.google.com/")
# driver.find_element_by_class_name("er8xn").send_keys("שיר חופשי")

# Task 5
driver = webdriver.Chrome(executable_path="C:\\Users\\Itay Zrihan\\Desktop\\ChromeDriver.exe")
driver.get("https://www.youtube.com/")
driver.find_element_by_id("search").send_keys("אייל גולן")
driver.find_element_by_id("search-icon-legacy").click()

# Task 6
# driver = webdriver.Chrome(executable_path="C:\\Users\\Itay Zrihan\\Desktop\\ChromeDriver.exe")
# driver.get("https://translate.google.com/")
# webelement = driver.find_element_by_class_name("er8xn").send_keys("hey")
# driver.find_element_by_xpath("//span/span/div/textarea")
# driver.find_element_by_xpath("/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea")
# print(webelement)
# אני יודע שהתכוונת שנשתמש בelemensts אבל פשוט לא מצאתי

# Task 7
# driver = webdriver.Chrome(executable_path="C:\\Users\\Itay Zrihan\\Desktop\\ChromeDriver.exe")
# driver.get("https://www.themarker.com/")
# david = driver.page_source
# print(len(david))


# print(news)


# CHALLENGES :)
# Task 8
# driver = webdriver.Chrome(executable_path="C:\\Users\\Itay Zrihan\\Desktop\\ChromeDriver.exe")
# driver.get("http://walla.co.il")
# cookies = driver.delete_all_cookies()
# print(cookies)
# driver.quit()

# task 9

# driver = webdriver.Chrome(executable_path="C:\\Users\\Itay Zrihan\\Desktop\\ChromeDriver.exe")
# driver.get("https://github.com/")
# driver.find_element_by_class_name("form-control input-sm header-search-wrapper p-0 js-chromeless-input-container header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center").send_keys("Selenium", Keys.ENTER)


# import requests
#
# res = requests.post('http://127.0.0.1:5000/data/123', json={"user_name": "henov"})
# if res.ok:
#     print(res.json())

