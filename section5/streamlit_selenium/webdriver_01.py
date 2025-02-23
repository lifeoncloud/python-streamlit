from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://news.naver.com/section/105")

elem = driver.find_element(By.CLASS_NAME, 'ranking_list _FLICKING_CONTENT')
childs = elem.find_elements(By.CLASS_NAME, 'rl_item _LAZY_LOADING_WRAP')
grandchilds = childs.find_elements(By.CLASS_NAME, 'rl_content')


for grandchild in grandchilds: 
    print(grandchild.text)

# elems = driver.find_element(By.CLASS_NAME, 'article_head')
# childs = elems.find_elements(By.TAG_NAME, 'h1')
# for child in childs:
#     print(child.text)
