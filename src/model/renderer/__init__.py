import os
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--start-maximized')

def render_html(url, render_time=5):
    driver = webdriver.Chrome(
        os.getenv("CHROMEDRIVER_PATH"),
        chrome_options=chrome_options)

    driver.get(url)
    time.sleep(render_time)
    html = driver.page_source
    driver.quit()

    return BeautifulSoup(html, features="html.parser")
