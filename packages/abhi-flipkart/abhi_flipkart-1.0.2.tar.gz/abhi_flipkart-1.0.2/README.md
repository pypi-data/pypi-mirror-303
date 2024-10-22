# Flipkart Scraper

A Python package to scrape product details such as price, title, rating, and other information from Flipkart.com. This package offers both an all-in-one method for retrieving all product details at once and separate methods for retrieving specific product details.

## Features

- Get product title
- Get product price
- Get product rating
- Get all product details at once

## Installation

You can install the `abhi-flipkart` package using `pip`:

```bash
pip install abhi-flipkart
```

Requirements
Make sure you have the following packages installed:

requests
beautifulsoup4
These will be automatically installed with the package.



## Usage

```python
from flipkart import FlipkartScraper

# Provide the product URL
product_url = 'https://www.flipkart.com/samsung-galaxy-s23-fe-purple-256-gb/p/itm8f6a49271bf21?pid=MOBGVTA2VGHCJFGG&lid=LSTMOBGVTA2VGHCJFGG1TC2LI&marketplace=FLIPKART&store=tyy%2F4io&srno=b_1_1&otracker=CLP_BannerX3&fm=organic&iid=en_Xqy_OHyrcQALLToVeCOiYi6XfZ1TBn8U_wcElBhYNuR7OzG-guKfCEmcxu3dm4paf1YFLsimTplvCE6DlbZbrvUFjCTyOHoHZs-Z5_PS_w0%3D&ppt=clp&ppn=mobile-phones-store&ssid=stxkg1hx740000001729468470030'

# Create a scraper instance
scraper = FlipkartScraper(product_url)

# Get individual details
title = scraper.get_title()
price = scraper.get_price()
rating = scraper.get_rating()

# Get all details at once
details = scraper.get_all_details()

print(f"Title: {title}")
print(f"Price: {price}")
print(f"Rating: {rating}")
print(f"Details: {details}")
```

## License

