# Download driver: https://developer.chrome.com/docs/chromedriver/downloads
from ansible_collections.fortinet.fortios.plugins.modules.fortios_registration_forticare import login
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import  Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os


class WebAutomation:
    def __init__(self):
        # Defind driver. options, and service
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")

        # Create option like download path to save into :)
        download_path = os.getcwd()
        prefs = {'download.default_dictionary': download_path}
        chrome_options.add_experimental_option('prefs', prefs)
        service = Service("chromedriver-linux64/chromedriver")
        self.driver = webdriver.Chrome(options=chrome_options, service=service)

    def login(self, username, password):
        # Load the webpase
        self.driver.get("https://demoqa.com/login")
        # Enter credentials!
        username_filed = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        password_filed = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
        logging_button = self.driver.find_element(By.ID, 'login')
        # Fill credentials anc click login
        username_filed.send_keys('username')
        password_filed.send_keys('password')
        # Some adds may come faster and may click it! So, we find the argument
        self.driver.execute_script("arguments[0].click();", logging_button)

    def fill_form(self, fullname, email, current_address, permanent_address):
        # Locate elements dropbox
        elements = (WebDriverWait(self.driver, 10).
                    until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div'))))
        elements.click()
        text_box = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-0')))
        text_box.click()

        # Locate the form fields and submit burron
        fullname_filed = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        email_filed = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
        current_address_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'currentAddress')))
        permanent_address_filed = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'permanentAddress')))
        submit_button = self.driver.find_element(By.ID, 'submit')

        # Filed in form fields
        fullname_filed.send_keys(fullname)
        email_filed.send_keys(email)
        current_address_field.send_keys(current_address)
        permanent_address_filed.send_keys(permanent_address)
        self.driver.execute_script("arguments[0].click();", submit_button)

    def download(self):
        # Locate Upload/Download section and Download buttom
        upload_download = (WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-7'))))
        upload_download.click()
        # click it:
        download_button = self.driver.find_element(By.ID, 'downloadButton')
        self.driver.execute_script("arguments[0].click();", download_button)

    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    webautomaiton = WebAutomation()
    webautomaiton.login('hamidva','G0admn@demoqa')
    webautomaiton.fill_form("Hamid Vakili", "vakilitestmail@gmail.com",
                            "Berlin,Germany",
                            "Berlin, Germany")
    webautomaiton.download()
    webautomaiton.close()
