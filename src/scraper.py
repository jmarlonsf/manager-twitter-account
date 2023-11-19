import argparse
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def execute(username="", password=""):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }

    url_login = "https://twitter.com/i/flow/login"
    url_profile = "https://twitter.com/jmarlonsf"
    driver_path = r"D:\\projetos\\manager-twitter-account\\src\\resource\\chromedriver\\chromedriver.exe"

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url_login)
    driver.implicitly_wait(5)
    time.sleep(5)
    elem_user = driver.find_element(By.TAG_NAME, "input")

    elem_user.clear()
    elem_user.send_keys(username)
    elem_user.send_keys(Keys.RETURN)

    elem_pass = driver.find_element(By.NAME, "password")
    elem_pass.send_keys(password)
    elem_pass.send_keys(Keys.RETURN)

    time.sleep(5)

    driver.get(url_profile)
    print()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Args used when using twitter')
    parser.add_argument('--username', type=str, help='twitter (X) username', required=True)
    parser.add_argument('--password', type=str, help='twitter (X) password', required=True)

    args = parser.parse_args()

    execute(args.username, args.password)
