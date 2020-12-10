{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Dependencies\n",
    "import pandas as pd\n",
    "from sqlalchemy import create_engine\n",
    "from datetime import datetime\n",
    "import datetime as dt\n",
    "from bs4 import BeautifulSoup\n",
    "import requests\n",
    "import pymongo\n",
    "from splinter import Browser\n",
    "#from bs4 import BeautifulSoup\n",
    "from webdriver_manager.chrome import ChromeDriverManager"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[WDM] - Current google-chrome version is 87.0.4280\n",
      "[WDM] - Get LATEST driver version for 87.0.4280\n",
      "[WDM] - Driver [C:\\Users\\sethi\\.wdm\\drivers\\chromedriver\\win32\\87.0.4280.88\\chromedriver.exe] found in cache\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " \n"
     ]
    }
   ],
   "source": [
    "# Creating executable path\n",
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "#1 Reading Mars information from NASA\n",
    "url = 'https://mars.nasa.gov/news/'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "html = browser.html\n",
    "soup = BeautifulSoup(html, 'html.parser')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"5 Hidden Gems Are Riding Aboard NASA's Perseverance Rover\""
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#2 Reading title\n",
    "results = soup.find('ul', class_='item_list')\n",
    "results2=results.find('li', class_='slide')\n",
    "news_title = results2.find(\"div\", class_=\"content_title\").text\n",
    "\n",
    "news_title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"The symbols, mottos, and small objects added to the agency's newest Mars rover serve a variety of purposes, from functional to decorative.\""
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Scraping new teaser\n",
    "news_p=results2.find('div', class_='article_teaser_body').text\n",
    "news_p"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[WDM] - Current google-chrome version is 87.0.4280\n",
      "[WDM] - Get LATEST driver version for 87.0.4280\n",
      "[WDM] - Driver [C:\\Users\\sethi\\.wdm\\drivers\\chromedriver\\win32\\87.0.4280.88\\chromedriver.exe] found in cache\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " \n"
     ]
    }
   ],
   "source": [
    "# Creating executable path\n",
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "#Getting the image url\n",
    "url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.links.find_by_partial_text('FULL IMAGE').click()\n",
    "browser.links.find_by_partial_text('more info').click()\n",
    "html = browser.html\n",
    "soup = BeautifulSoup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "results = soup.find('figure', class_='lede')\n",
    "results2=results.a['href']\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'/spaceimages/images/largesize/PIA16028_hires.jpg'"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "results2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "featured_image_url= 'https://www.jpl.nasa.gov' + results2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16028_hires.jpg'"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "featured_image_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "scrolled": false
   },
   "outputs": [],
   "source": [
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[WDM] - Current google-chrome version is 87.0.4280\n",
      "[WDM] - Get LATEST driver version for 87.0.4280\n",
      "[WDM] - Driver [C:\\Users\\sethi\\.wdm\\drivers\\chromedriver\\win32\\87.0.4280.88\\chromedriver.exe] found in cache\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " \n"
     ]
    }
   ],
   "source": [
    "# Creating executable path\n",
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "#Getting hemisphere picture and information\n",
    "url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "html = browser.html\n",
    "soup = BeautifulSoup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<div class=\"description\"><a class=\"itemLink product-item\" href=\"/search/map/Mars/Viking/cerberus_enhanced\"><h3>Cerberus Hemisphere Enhanced</h3></a><span class=\"subtitle\" style=\"float:left\">image/tiff 21 MB</span><span class=\"pubDate\" style=\"float:right\"></span><br/><p>Mosaic of the Cerberus hemisphere of Mars projected into point perspective, a view similar to that which one would see from a spacecraft. This mosaic is composed of 104 Viking Orbiter images acquired…</p></div>,\n",
       " <div class=\"description\"><a class=\"itemLink product-item\" href=\"/search/map/Mars/Viking/schiaparelli_enhanced\"><h3>Schiaparelli Hemisphere Enhanced</h3></a><span class=\"subtitle\" style=\"float:left\">image/tiff 35 MB</span><span class=\"pubDate\" style=\"float:right\"></span><br/><p>Mosaic of the Schiaparelli hemisphere of Mars projected into point perspective, a view similar to that which one would see from a spacecraft. The images were acquired in 1980 during early northern…</p></div>,\n",
       " <div class=\"description\"><a class=\"itemLink product-item\" href=\"/search/map/Mars/Viking/syrtis_major_enhanced\"><h3>Syrtis Major Hemisphere Enhanced</h3></a><span class=\"subtitle\" style=\"float:left\">image/tiff 25 MB</span><span class=\"pubDate\" style=\"float:right\"></span><br/><p>Mosaic of the Syrtis Major hemisphere of Mars projected into point perspective, a view similar to that which one would see from a spacecraft. This mosaic is composed of about 100 red and violet…</p></div>,\n",
       " <div class=\"description\"><a class=\"itemLink product-item\" href=\"/search/map/Mars/Viking/valles_marineris_enhanced\"><h3>Valles Marineris Hemisphere Enhanced</h3></a><span class=\"subtitle\" style=\"float:left\">image/tiff 27 MB</span><span class=\"pubDate\" style=\"float:right\"></span><br/><p>Mosaic of the Valles Marineris hemisphere of Mars projected into point perspective, a view similar to that which one would see from a spacecraft. The distance is 2500 kilometers from the surface of…</p></div>]"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "results3=soup.find_all('div', class_='description')\n",
    "results3\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced',\n",
       " 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced',\n",
       " 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced',\n",
       " 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced']"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Getting heading new and image url\n",
    "heading_list=[]\n",
    "url_list=[]\n",
    "\n",
    "for result in results3:\n",
    "    heading=result.find('h3').text\n",
    "    heading_list.append(heading)\n",
    "    url=result.find('a')['href']\n",
    "    url_list.append(url)\n",
    "    new_url=['https://astrogeology.usgs.gov'+ x for x in url_list ]\n",
    "\n",
    "\n",
    "new_url\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Cerberus Hemisphere Enhanced',\n",
       " 'Schiaparelli Hemisphere Enhanced',\n",
       " 'Syrtis Major Hemisphere Enhanced',\n",
       " 'Valles Marineris Hemisphere Enhanced']"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "heading_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "\n",
    "full_imgs=[]\n",
    "\n",
    "for new in new_url:\n",
    "    url=new\n",
    "    browser.visit(url)\n",
    "    browser.links.find_by_partial_text('Sample').click()\n",
    "    html = browser.html\n",
    "    soup = BeautifulSoup(html, 'html.parser')\n",
    "    results6 = soup.find_all('img', class_='wide-image')\n",
    "    img_path = results6[0]['src']\n",
    "    new_img = 'https://astrogeology.usgs.gov/' + img_path\n",
    "    \n",
    "# full image links to a list\n",
    "    full_imgs.append(new_img)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<img class=\"wide-image\" src=\"/cache/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg\"/>]"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "results6\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'/cache/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg'"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "img_path"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['https://astrogeology.usgs.gov//cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg',\n",
       " 'https://astrogeology.usgs.gov//cache/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg',\n",
       " 'https://astrogeology.usgs.gov//cache/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg',\n",
       " 'https://astrogeology.usgs.gov//cache/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg']"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "full_imgs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Cerberus Hemisphere Enhanced',\n",
       " 'Schiaparelli Hemisphere Enhanced',\n",
       " 'Syrtis Major Hemisphere Enhanced',\n",
       " 'Valles Marineris Hemisphere Enhanced']"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "heading_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'title': 'Cerberus Hemisphere Enhanced',\n",
       "  'img_url': 'https://astrogeology.usgs.gov//cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg'},\n",
       " {'title': 'Schiaparelli Hemisphere Enhanced',\n",
       "  'img_url': 'https://astrogeology.usgs.gov//cache/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg'},\n",
       " {'title': 'Syrtis Major Hemisphere Enhanced',\n",
       "  'img_url': 'https://astrogeology.usgs.gov//cache/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg'},\n",
       " {'title': 'Valles Marineris Hemisphere Enhanced',\n",
       "  'img_url': 'https://astrogeology.usgs.gov//cache/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg'}]"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "heading_url = zip(heading_list, full_imgs)\n",
    "\n",
    "hemisphereurl = []\n",
    "\n",
    "# Iterate through the zipped object\n",
    "for x,y in heading_url:\n",
    "    \n",
    "    hemi_dict = {}\n",
    "    \n",
    "    # Add hemisphere title to dictionary\n",
    "    hemi_dict['title'] = x\n",
    "    \n",
    "    # Add image url to dictionary\n",
    "    hemi_dict['img_url'] = y\n",
    "    \n",
    "    # Append the list with dictionaries\n",
    "    hemisphereurl.append(hemi_dict)\n",
    "\n",
    "hemisphereurl"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Reading Table form space facts \n",
    "\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://space-facts.com/mars/'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[                      0                              1\n",
       " 0  Equatorial Diameter:                       6,792 km\n",
       " 1       Polar Diameter:                       6,752 km\n",
       " 2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       " 3                Moons:            2 (Phobos & Deimos)\n",
       " 4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       " 5         Orbit Period:           687 days (1.9 years)\n",
       " 6  Surface Temperature:                   -87 to -5 °C\n",
       " 7         First Record:              2nd millennium BC\n",
       " 8          Recorded By:           Egyptian astronomers,\n",
       "   Mars - Earth Comparison             Mars            Earth\n",
       " 0               Diameter:         6,779 km        12,742 km\n",
       " 1                   Mass:  6.39 × 10^23 kg  5.97 × 10^24 kg\n",
       " 2                  Moons:                2                1\n",
       " 3      Distance from Sun:   227,943,824 km   149,598,262 km\n",
       " 4         Length of Year:   687 Earth days      365.24 days\n",
       " 5            Temperature:     -87 to -5 °C      -88 to 58°C,\n",
       "                       0                              1\n",
       " 0  Equatorial Diameter:                       6,792 km\n",
       " 1       Polar Diameter:                       6,752 km\n",
       " 2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       " 3                Moons:            2 (Phobos & Deimos)\n",
       " 4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       " 5         Orbit Period:           687 days (1.9 years)\n",
       " 6  Surface Temperature:                   -87 to -5 °C\n",
       " 7         First Record:              2nd millennium BC\n",
       " 8          Recorded By:           Egyptian astronomers]"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tables = pd.read_html(url)\n",
    "tables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = tables[0]\n",
    "\n",
    "df.columns = ['Mars Profile', 'Stats']\n",
    "df.set_index('Mars Profile', inplace=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "pandas.core.frame.DataFrame"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:pydata] *",
   "language": "python",
   "name": "conda-env-pydata-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
