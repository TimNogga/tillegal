from selenium import webdriver
import bs4 as bs
import numpy as np
import pandas as pd
import matplot

# Create a Safari WebDriver instance
driver = webdriver.Safari()

url = "http://www.rewe.de/angebote/nationale-angebote"

# Navigate to the URL using Safari WebDriver
driver.get(url)

# Get the fully rendered HTML content
html_content = driver.page_source

# Search the HTML content for article tags
soup = bs.BeautifulSoup(html_content, 'html.parser')

# Loop through each article element and extract the price and article information
for article in soup.find_all('article', class_='cor-offer-renderer-tile cor-link'):
    # Find price and article title elements within the article
    price_tag = article.find('div', class_='cor-offer-price__tag-price')
    article_title = article.find('a', class_='cor-offer-information__title-link')

    if price_tag and article_title:
        price = price_tag.get_text(strip=True)
        article_text = article_title.get_text(strip=True)
        print(f"Article: {article_text}, Price: {price}")

# Close the WebDriver

driver.quit()




