# -*- coding: utf-8 -*-

import sys
import warnings
import time

from tqdm import tqdm
from bs4 import BeautifulSoup

import pyderman

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

def open_chrome(headless=True):
    path = pyderman.install(browser=pyderman.chrome)

    options = Options()
    options.add_argument("--enable-javascript")
    options.headless = headless

    driver = webdriver.Chrome(path, options=options)

    # Sanity checks.
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    return driver


def remove_popups(driver, url, pop_name):
    driver.get(url)
    # Remove all pop-up nonsense...
    element = driver.find_element_by_class_name(pop_name)
    driver.execute_script("""
    var element = arguments[0];
    element.parentNode.removeChild(element);
    """, element)
    driver.get(url)
    return driver
