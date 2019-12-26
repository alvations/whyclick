
import time
import random

from tqdm import tqdm
from bs4 import BeautifulSoup

from whyclick.chrome import open_chrome, remove_popups

def login(username, password):
    whyq_url = 'https://www.whyq.sg'
    driver = open_chrome(whyq_url)
    driver = remove_popups(driver, whyq_url, 'pop_promo')

    # Activate the login popup.
    element = driver.find_elements_by_xpath("//a[@data-target='#login_popup']")[0]
    element.click()
    # Fill in the login.
    driver.find_element_by_xpath("//input[@name='loginUser']").send_keys(username)
    driver.find_element_by_xpath("//input[@name='loginPass']").send_keys(password)
    # Click on submit.
    element = driver.find_elements_by_xpath("//input[@type='submit']")[0]
    element.click()

    time.sleep(1)
    return driver

def download_previous_orders(driver):
    # Paginate through the orders.
    driver.get('https://www.whyq.sg/user/orders')
    time.sleep(1)
    orders = set()
    while True:
        bsoup = BeautifulSoup(driver.page_source, 'lxml')
        links = [a['href'] for a in bsoup.find_all('a') if 'href' in a.attrs
                 and a['href'].startswith('https://www.whyq.sg/user/order_info')]
        orders.update(links)
        try:
            driver.find_elements_by_xpath("//a[@rel='next']")[0].click()
        except:
            break

    # Open all the order urls and download the data.
    orders_json = []
    for url in tqdm(orders):
        driver.get(url)
        bsoup = BeautifulSoup(driver.page_source, 'lxml')

        this_order = {}
        order_details, order_items, *_ = bsoup.find_all('tbody')
        for tr in order_details.find_all('tr'):
            if len(tr.find_all('td')) == 2:
                k, v = tr.find_all('td')
                this_order[k.text.strip()] = v.text.strip()

        for tr in order_items.find_all('tr'):
            if len(tr.find_all('td')) == 2:
                k, v = tr.find_all('td')
                this_order[k.text.strip()] = v.text.strip()
        orders_json.append(this_order)

    return orders_json


def randomly_order(driver):
    days = driver.find_elements_by_xpath("//div[@class='owl-item active']")
    for element_day in days:
        # Select day.
        element_day.click()
        # Find meals.
        meals = [b for b in element_day.find_elements_by_xpath('//button')
                 if b and b.text == "ADD"]
        # Randomly choose one.
        random.choice(meals).click()
        time.sleep(3)
    # Checkout.
    driver.find_element_by_link_text("PLACE ORDER").click()
