from src.model.parser.base import ParserBase
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--no-sandbox')

class ParserSumut(ParserBase):
    WEB_URL = "http://covid19.sumutprov.go.id/"
    DATA_URL = "http://covid19.sumutprov.go.id/"

    def __init__(self, render=None):
        super(ParserSumut, self).__init__(render)

    def parse(self, source):

        driver = webdriver.Chrome(
            ChromeDriverManager().install(),
            chrome_options=chrome_options
        )
        driver.get("http://covid19.sumutprov.go.id/")
        timeout = 10

        # Wait for JS load
        try:
            element_present = EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="content"]/section[4]/div/div/div[2]/'
                    'div/center/div/div[1]/span'
                )
            )
            WebDriverWait(driver, timeout).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")

        positive = driver.find_element_by_xpath(
            '//*[@id="content"]/section[4]/div/div/div[2]/'
            'div/center/div/div[1]/span'
        ).text

        recover = driver.find_element_by_xpath(
            '//*[@id="content"]/section[4]/div/div/div[4]/'
            'div/center/span[2]'
        ).text

        dead = driver.find_element_by_xpath(
            '//*[@id="content"]/section[4]/div/div/div[3]/'
            'div/center/span[2]'
        ).text

        return {
            "positif": int(positive),
            "sembuh": int(recover),
            "meninggal": int(dead)
        }
