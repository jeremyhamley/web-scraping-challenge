#imports
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from bs4 import BeautifulSoup
import pandas as pd
import time



def init_browser():
    executable_path = {'executable_path': 'C:\\Users\\jerem\\chromedriver\\chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)



def scrape():
    browser = init_browser()
    # add dictionary to store data
    mars_data = {}
    
    #Mars news
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    time.sleep(5)
    html = browser.html
    soup = BeautifulSoup(html, 'lxml')

    #store news data
    news = soup.find('li', class_='slide')
    news_img = news.find('div', class_='list_image').img['src']
    news_date = news.find('div', class_='list_date').text
    news_title = news.find('h3').text
    news_para = news.find('div', class_='article_teaser_body').text
    #add to dict
    mars_data['news_date'] = news_date
    mars_data['news_title'] = news_title
    mars_data['news_para'] = news_para
    mars_data['news_img'] = (f"https://mars.nasa.gov{news_img}")


    #featured image
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    time.sleep(3)
    html = browser.html
    soup = BeautifulSoup(html, 'lxml')

    #store image title
    img_title = soup.find('h1').text

    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(1)
    browser.click_link_by_partial_text('more info')
    time.sleep(1)

    html = browser.html
    soup = BeautifulSoup(html, 'lxml')

    featured_image_fig = soup.find('figure', class_='lede')
    #store image url
    featured_image_url = (f"https://www.jpl.nasa.gov{featured_image_fig.img['src']}")
    featured_image_cap = featured_image_fig.img['alt']
    #add to dict
    mars_data['featured_img_title'] = img_title
    mars_data['featured_image_url'] = featured_image_url
    mars_data['featured_image_cap'] = featured_image_cap


    #Mars weather
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    time.sleep(5)
    html = browser.html
    soup = BeautifulSoup(html, 'lxml')
    #store weather data
    article = soup.find('article', class_= 'css-1dbjc4n r-1loqt21 r-18u37iz r-1ny4l3l r-o7ynqc r-6416eg')
    weather = article.find_all('span', class_= 'css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0')
    weather_text= (weather[4].text)
    #add to dict
    mars_data['weather'] = weather_text



    #Mars facts
    url = 'https://space-facts.com/mars/'
    browser.visit(url)
    time.sleep(3)
    tables = pd.read_html(url)

    #store facts_1
    facts_db = tables[0]
    facts_db.rename(columns={0:'Mars Planet Profile'}, inplace=True)
    facts_db.rename(columns={1:''}, inplace=True)
    facts_db.set_index('Mars Planet Profile', inplace=True)
    fact_dict = facts_db.to_html()

    #store facts_2
    facts2_db = tables[1]
    facts2_db.set_index('Mars - Earth Comparison', inplace=True)
    fact2_dict = facts2_db.to_html()

    #add to dict
    mars_data['facts_1'] = fact_dict
    mars_data['facts_2'] = fact2_dict


    #Mars Hemisphere images
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    time.sleep(3)
    html = browser.html
    soup = BeautifulSoup(html, 'lxml')

    
    hemi_names = soup.find_all('h3')
    
    #store hemisphere data
    for name in hemi_names:
        browser.click_link_by_partial_text(name.text)
        time.sleep(2)
        html = browser.html
        soup = BeautifulSoup(html, 'lxml')
    
        url_li = soup.find('li')
        url_a = url_li.find('a')
        url_pic = url_a.get('href')

        name = name.text
        name_db = name.replace(' ','_')
        mars_data[name_db] = name
        mars_data[f'{name_db}_url'] = url_pic


        browser.back()
        time.sleep(1)


    browser.quit()   

    return mars_data
