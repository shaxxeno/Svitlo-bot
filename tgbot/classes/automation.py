import time
from tgbot.config import load_config
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

delay = 120


class Automation:

    def __init__(self, address_name, address_number):
        self.driver = None
        self.address_name = address_name
        self.address_number = address_number
        self.get_page_source()

    def get_page_source(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument("--window-size=1920,1080")
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(url=load_config().misc.url)
        if self.driver.find_element(By.XPATH, '//*[@id="modal-attention"]/div/div/div[1]/button'):
            self.driver.find_element(By.XPATH, '//*[@id="modal-attention"]/div/div/div[1]/button').click()
        WebDriverWait(self.driver, delay).until(ec.presence_of_element_located((By.XPATH, '//*[@id="street"]')))
        self.driver.find_element(By.XPATH, '//*[@id="street"]').send_keys(self.address_name)
        self.driver.find_element(By.XPATH, '//*[@id="streetautocomplete-list"]/div').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="house_num"]').send_keys(self.address_number)
        self.driver.find_element(By.XPATH, '//*[@id="house_numautocomplete-list"]/div[1]').click()

    def text(self):
        page_source = self.driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        reply = soup.find('div', {'id': 'showCurOutage'}).find('p').text.strip()
        return reply

    def image(self):
        image = self.driver.find_element(By.XPATH, '//*[@id="tableRenderElem"]').screenshot_as_png
        return image
