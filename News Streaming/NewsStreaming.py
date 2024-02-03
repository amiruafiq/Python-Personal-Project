import requests

NEWS_API_KEY = 'ed2180d6995445b696bf2f3868ad3e6b'
NEWS_API_ENDPOINT = 'https://newsapi.org/v2/top-headlines'

def fetch_news(api_key, category='technology', country='us', num_articles=5):
    params = {
        'apiKey': api_key,
        'category': category,
        'country': country,
        'pageSize': num_articles
    }

    response = requests.get(NEWS_API_ENDPOINT, params=params)

    if response.status_code == 200:
        news_data = response.json()
        articles = news_data.get('articles', [])
        return articles
    else:
        print(f"Failed to fetch news. Status code: {response.status_code}")
        return None

def display_news(news_articles):
    if not news_articles:
        print("No news articles found.")
        return

    for idx, article in enumerate(news_articles, start=1):
        title = article.get('title', 'No Title')
        description = article.get('description', 'No Description')
        url = article.get('url', '#')

        print(f"{idx}. {title}")
        print(f"   {description}")
        print(f"   {url}\n")

if __name__ == "__main__":
    news_articles = fetch_news(NEWS_API_KEY, category='technology', num_articles=5)
    
    if news_articles:
        display_news(news_articles)
    else:
        print("No news articles found.")
