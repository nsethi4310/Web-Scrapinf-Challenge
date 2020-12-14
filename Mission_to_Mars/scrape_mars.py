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

    heading_list=[]
    url_list=[]

    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    results3=soup.find_all('div', class_='description')

    for result in results3:
        heading=result.find('h3').text
        heading_list.append(heading)
        url=result.find('a')['href']
        url_list.append(url)
        new_url=['https://astrogeology.usgs.gov'+ x for x in url_list ]

    full_imgs=[]

    for new in new_url:
        url=new
        browser.visit(url)
        browser.links.find_by_partial_text('Sample').click()
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        results6 = soup.find_all('img', class_='wide-image')
        img_path = results6[0]['src']
        new_img = 'https://astrogeology.usgs.gov/' + img_path
        full_imgs.append(new_img)
    
    heading_url = zip(heading_list, full_imgs)

    hemisphereurl = []

# Iterate through the zipped object
    for x,y in heading_url:
    
        hemi_dict = {}
        
        # Add hemisphere title to dictionary
        hemi_dict['title'] = x
        
        # Add image url to dictionary
        hemi_dict['img_url'] = y
        
        # Append the list with dictionaries
        hemisphereurl.append(hemi_dict)
    


    heading = {}
        
    heading['news_title'] = news_title
        

    heading['news_p'] = news_p
        
    heading['featured_image_url'] = featured_image_url

    heading['hemisphereurls'] = hemisphereurl

    #heading['img_url']= full_imgs


    browser.quit()

#Reading mars facts into html

    url = 'https://space-facts.com/mars/'

    
    tables = pd.read_html(url)
    df = tables[0]
    df.columns = ['Mars Profile', 'Stats']
    tab_html = df.to_html()

    heading['MarsFacts'] = tab_html
    


    return heading

# %%
   
