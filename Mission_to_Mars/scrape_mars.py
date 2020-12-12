# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Dependencies
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime
import datetime as dt
from bs4 import BeautifulSoup
import requests
import pymongo
from splinter import Browser
#from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


# %%
# Creating executable path
def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)


def scrape():
    browser = init_browser()
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find('ul', class_='item_list')
    results2=results.find('li', class_='slide')
    news_title = results2.find("div", class_="content_title").text
    news_p=results2.find('div', class_='article_teaser_body').text
    
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    browser.links.find_by_partial_text('FULL IMAGE').click()
    browser.links.find_by_partial_text('more info').click()
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find('figure', class_='lede')
    results2=results.a['href']
    featured_image_url= 'https://www.jpl.nasa.gov' + results2
    #heading_data = zip(news_title, news_p, featured_image_url)
    heading = {}
        
    heading['news_title'] = news_title
        

    heading['news_p'] = news_p
        
    heading['featured_image_url'] = featured_image_url
    browser.quit()

    return heading
    

# %%
   
