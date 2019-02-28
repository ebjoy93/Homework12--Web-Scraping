#imports
from splinter import Browser
from bs4 import BeautifulSoup
import time
import pandas as pd

#chrome driver executable
def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    
    #mars news
    browser = init_browser()
    
    news_url = "https://mars.nasa.gov/news/"
    browser.visit(news_url)
    time.sleep(1)
    
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    
    article = soup.find("div", class_='list_text')
    news_title = article.find("div", class_="content_title").text
    news_p = article.find("div", class_ ="article_teaser_body").text

    #print(news_title)
    #print(news_p)
    
    #output = [news_title, news_p]

    #pulling images
    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)
    time.sleep(1)    
    
    image = soup.find("div",{"class":"carousel_items"})

    featured_img = soup.find("article")
    featured_img_url = featured_img_url = image_url+featured_img['style'].split(':')[1].split('\'')[1]

    #print(featured_image_url)

    #pulling twitter info
    mars_weather_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(mars_weather_url)
    time.sleep(1)
    
    tweets = mars_weather_soup.find('ol', class_='stream-items')
    mars_weather = tweets.find('p', class_="tweet-text").text

    #print(mars_weather)

    #pulling mars facts
    facts_url = "https://space-facts.com/mars/"
    browser.visit(facts_url)
    time.sleep(1)
    
    facts_url = "https://space-facts.com/mars/"

    browser.visit(facts_url)
    mars_data = pd.read_html(facts_url)
    mars_data = pd.DataFrame(mars_data[0])
    mars_facts = mars_data.to_html(header = False, index = False)

    #print(mars_facts)
    
    #pulling hemispheres 
    hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemispheres_url)
    time.sleep(1)
    
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    mars_hemisphere = []

    products = soup.find("div", class_ = "result-list" )
    hemispheres = products.find_all("div", class_="item")

    for hemisphere in hemispheres:
        title = hemisphere.find("h3").text
        title = title.replace("Enhanced", "")
        end_link = hemisphere.find("a")["href"]
        
        image_link = "https://astrogeology.usgs.gov/" + end_link    
        
        browser.visit(image_link)
        html = browser.html
        soup=BeautifulSoup(html, "html.parser")
        
        downloads = soup.find("div", class_="downloads")
        image_url = downloads.find("a")["href"]
        mars_hemisphere.append({"title": title, "img_url": image_url})
    
    #print(mars_hemisphere)



    #scrape into a dict
    final_data = {
                    "news_title" : news_title,
                    "news_p" : news_p,
                    "featured_image_url" : featured_image_url,
                    "mars_weather" : mars_weather,
                    "mars_facts" : mars_facts,
                    "mars_hemisphere" : mars_hemisphere
                }

    return final_data
