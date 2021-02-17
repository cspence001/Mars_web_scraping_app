
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd

def init_browser():
    executable_path = {'executable_path': "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser =init_browser()
    mars_dict = {}
    
    #latest news 
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    articles = soup.find_all('div', class_='list_text')

    for article in articles:
        news_title = article.find('div', class_='content_title').text
        news_p = article.find('div', class_='article_teaser_body').text

    #featured_img
    jp_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(jp_url) 
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')  
    main = soup.find('div', class_='header')
    img = main.find_all('img', class_='headerimage fade-in')
    for src in img:
        src=src.get('src')
        featured_image_url = jp_url.replace('index.html', src)


    #facts table
    facts_url = 'https://space-facts.com/mars/'
    table = pd.read_html(facts_url)
    facts_table = table[0]
    html_table = facts_table.to_html()

    #hemispheres
    main_url = 'https://astrogeology.usgs.gov/'
    hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemispheres_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    section = soup.find('div', class_='collapsible results')
    hemispheres = section.find_all('div', class_='item')

    for title in hemispheres:
        hem_title = title.find('div', class_='description')
        titles = hem_title.h3.text

    mars_urls = []
    
    for url in hemispheres:
        url_ext = url.find('a')['href']
        browser.visit(main_url+url_ext)
    
        url_html = browser.html
        soup = BeautifulSoup(url_html, 'html.parser')
    
        img_list = soup.find('li')
        img_url = img_list.find('a')['href']
    
    mars_urls.append({"title" : titles, "img_url" : img_url})

    #full dictionary 
    mars_dict = {
        'hemispheres_imgs':mars_urls,
        'news_title':news_title,
        'news_p':news_p,
        'featured_img':featured_image_url,
        'facts_table':html_table
        }

    browser.quit()
    
    return mars_dict

