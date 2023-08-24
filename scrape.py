from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def extract_players():
    
    options = ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)

    url = 'https://ratings.fide.com/'
    driver.get(url)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "top_rating_div")))

    page_source = driver.page_source

    soup = BeautifulSoup(page_source, 'html.parser')

    table = soup.find("div", {"id" : "top_rating_div"})
    
    for img in soup.find_all("img"):
        img['src'] = url + img['src']
        
    for players in table.find_all("a"):
        players['href'] = url + players['href']
        

    driver.quit()
    
    return str(table)

def extract_tournments():
    
    options = ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)

    url = 'https://calendar.fide.com/'
    driver.get(url)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "section-profile")))

    page_source = driver.page_source

    soup = BeautifulSoup(page_source, 'html.parser')
    
    table = soup.find("section",{"class" : "container section-profile"})
    
    driver.quit()
    
    return str(table)

def extract_news():
    
    options = ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)

    url = 'https://www.chess.com/news'
    driver.get(url)

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "v5-section-content-wide")))
    
    page_source = driver.page_source

    soup = BeautifulSoup(page_source, 'html.parser')
    
    news_container = soup.find("div",{"class" : "v5-section-content-wide"})
    
    for img in soup.find_all("img"):
        if "data-srcset" in img:
            img['src']=img['data-src']
    
    driver.quit()
    
    fh=open("text.txt","w")
    fh.write(str(news_container))
    fh.close()
    
    return str(news_container)
