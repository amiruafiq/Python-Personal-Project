import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://www.hmetro.com.my/"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the webpage
soup = BeautifulSoup(response.text, "html.parser")

# Find all quote blocks on the page
quote_blocks = soup.find_all("div", class_="quote")

# Extract and print each quote and its author
for quote_block in quote_blocks:
    quote = quote_block.find("span", class_="text").text
    author = quote_block.find("small", class_="author").text
    print(f"Quote: {quote}\nAuthor: {author}\n")
