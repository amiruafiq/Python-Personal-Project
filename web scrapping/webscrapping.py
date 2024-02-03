# FAILED
import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    # Send an HTTP request to the specified URL with allow_redirects=True
    response = requests.get(url, allow_redirects=True)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract information based on the HTML structure of the website
        article_titles = []
        for article in soup.find_all('div', class_='nbg-image'):
            title = article.find('h2').text.strip()
            article_titles.append(title)
            # Print the title in the terminal
            print("- " + title)

        return article_titles
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None

def export_to_text(article_titles, output_filename="output.txt"):
    try:
        # Write article titles to a text file
        with open(output_filename, "w", encoding="utf-8") as text_file:
            for title in article_titles:
                text_file.write(title + "\n")
        print(f"Text file '{output_filename}' exported successfully.")
    except Exception as e:
        print(f"Failed to export to text file. Error: {e}")

if __name__ == "__main__":
    # Specify the URL of the website you want to scrape
    target_url = "https://www.hmetro.com.my/"

    # Call the scraping function and export to a text file
    titles = scrape_website(target_url)

    if titles:
        # Export to a text file
        export_to_text(titles)
    else:
        print("Failed to export to text file.")
