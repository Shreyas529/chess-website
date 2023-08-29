from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

url = 'https://ratings.fide.com/'
driver.get(url)

driver.implicitly_wait(10)

page_source = driver.page_source

soup = BeautifulSoup(page_source, 'html.parser')

table = soup.find("div", {"id" : "top_rating_div"})
print(table)

driver.quit()