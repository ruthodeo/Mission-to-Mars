#!/usr/bin/env python
# coding: utf-8

# In[116]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[117]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[118]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[119]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[120]:


slide_elem.find('div', class_='content_title')


# In[121]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[122]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


#  ### Featured Images

# In[123]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[124]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[125]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[126]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[127]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[128]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[129]:


df.to_html()


# In[130]:


browser.quit()


# In[131]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[132]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[133]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[134]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[135]:


slide_elem.find('div', class_='content_title')


# In[136]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[137]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[138]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[139]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[140]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[141]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[142]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[144]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[145]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[146]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[161]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[162]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []


# In[163]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[164]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[165]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
html = browser.html
img_soup = soup(html,'html.parser')
results = img_soup.find_all('div', class_='description')

for item in results:
    # gets image title and adds title to list
    title = item.find('h3').text
    
    # gets href, appends it to URL base, visits new page
    href = item.find('a')['href']
    img_url = url + href
    browser.visit(img_url)
    new_html = browser.html
    new_soup = soup(new_html, 'html.parser')

    # Gets image url from new page
    image_tag = new_soup.find('div', class_ = 'downloads')
    jpg_url = image_tag.find('a')['href']
    jpg_url = url + jpg_url
    
    # Adds items to hemisphere_image_urls
    temp_dict = dict({'img_url': jpg_url, 'title': title})
    hemisphere_image_urls.append(temp_dict)


# In[166]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[113]:


# 5. Quit the browser
browser.quit()


# In[ ]:





# In[ ]:




