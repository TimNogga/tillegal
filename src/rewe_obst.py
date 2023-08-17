from selenium import webdriver
import bs4 as bs
import numpy as np
import pandas as pd
import matplot

# Create a Safari WebDriver instance
driver = webdriver.Safari()

url = "https://www.rewe.de/angebote/nationale-angebote/?market-flyer=active"

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
import spacy
from collections import defaultdict

# Sample list of offers with (product, price) format
offers = [
    ("Gelb- oder weißfleischige Plattpfirsiche", "0,88 €"),
    ("Kernlose Tafeltrauben", "3,99 €"),
    ("Mirée Französische Kräuter", "0,99 €"),
    # ... (other offers)
]

# Define categories and their associated keywords
categories = {
    "Food": ["Apple", "Banana", "Orange", "Carrot", "Tomato", "Kirschen", "Pfifferlinge", "Zucchini", "Kirschen", "Pfifferlinge", "Zucchini"],
    "Drogerie": ["Shampoo", "Toothpaste"],
    "Beverages": ["Coca-Cola", "Volvic Bio Teegetränk", "Jack Daniel's Tennessee Whiskey"],
    # ... (other categories and keywords)
}

# Initialize a dictionary to store categorized offers
categorized_offers = defaultdict(list)

# Load a pre-trained language model
nlp = spacy.load("en_core_web_sm")

# Categorize the offers
for product, price in offers:
    doc = nlp(product.lower())  # Process text using spaCy
    matched_category = None
    for category, keywords in categories.items():
        if any(keyword.lower() in doc.text for keyword in keywords):
            matched_category = category
            break
    if matched_category:
        categorized_offers[matched_category].append((product, price))

# Print categorized offers
for category, offers_list in categorized_offers.items():
    print(f"{category}:")
    for product, price in offers_list:
        print(f"  {product}, Price: {price}")

driver.quit()




