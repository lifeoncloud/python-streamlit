from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://www.naver.com')

search = input('검색어를 입력: ')

elem = driver.find_element(By.NAME, 'query')
elem.send_keys(search)
elem.send_keys(Keys.RETURN)

# VIEW element가 강의 내용과 달라서 찾아야 할 듯.
# view = driver.find_element(By.NAME, '블로그')
view = driver.find_element(By.CLASS_NAME, 'spnew2 ico_nav_blog')
view.click()

ul = driver.find_element(By.CLASS_NAME, 'lst_view _fe_view_infinite_scroll_append_target')
posts = ul.find_elements(By.XPATH, './li')

for post in posts:
    title_tag = post.find_element(By.CLASS_NAME, 'title_link')
    print(title_tag.text)
