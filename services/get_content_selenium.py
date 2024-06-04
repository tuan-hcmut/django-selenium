from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
# from .headers import random_headers
# from .proxies import random_proxies

def get_content_selenium(url, proxy=None):

    # if proxy == None:
    #     proxy = random_proxies()
    # print("proxy IP: ", proxy)

    try:
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-dev-shm-usage")
        # chrome_options.add_argument("--enable-logging")
        # chrome_options.add_argument(f"--user-agent={random_headers['user-agent']}")
        # chrome_options.add_argument(f"--proxy-server={proxy}")
        driver = webdriver.Chrome(options=chrome_options)
        driver.implicitly_wait(1)
        driver.get(url)
        selenium_content = driver.page_source
        soup_selenium = BeautifulSoup(selenium_content, 'html.parser')
        driver.quit()
        return soup_selenium
    except:
        return None