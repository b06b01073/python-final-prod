from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service

import os
import time



    # PROD options(reference: https://www.youtube.com/watch?v=Ven-pqwk3ec)
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument("--no-sandbox")
    # driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

def crawler(urls, names):
    # DEV driver
    driver = webdriver.Chrome('./chromedriver')
    res = {}
    for url, name in zip(urls, names):
        # crawl the page by selenium

        # change url to scientific name
        res.setdefault(url, dict())
        res[url]["threat"] = []
        driver.get(url)

        # sleep for 3 secs to make sure the page is loaded completely
        time.sleep(2)

        html = driver.page_source

        # pass the crawled page to beautifulsoup
        soup = BeautifulSoup(html, "html.parser")

        # select the <div> with id "threats-details"
        result = soup.find("div", {"id": "threats-details"})

        for row in result.tbody.find_all('tr', recursive=False):
            threat = row.find('td').text
            if len(threat) != 0:
                res[url]["threat"].append(threat)

        res[url]["population"] = soup.find("p", {"class": "species-population-panel"}).text


        imageTag = soup.find('a', {"class": "featherlight__gallery__image"})
        res[url]["imageURL"] = imageTag['href'] if imageTag else None
        res[url]["name"] = name

    return res
