import requests

def get_news(api_key, keyword=None, topic=None):
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'apiKey': api_key,
        'language': 'en',
        'pageSize': 5,
    }
    if keyword:
        params['q'] = keyword
    if topic:
        params['category'] = topic

    response = requests.get(url, params=params)

    if response.status_code == 200:
        news_list = response.json().get('articles', [])
        return news_list if news_list else None
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None


def save_news(news, file_name="news.txt"):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i, article in enumerate(news, 1):
            file.write(f"News {i}:\n")
            file.write(f"Title: {article.get('title', 'No Title')}\n")
            file.write(f"Source: {article['source']['name']}\n")
            file.write(f"Published: {article.get('publishedAt', 'Unknown')}\n")
            file.write(f"Link: {article.get('url', 'No URL')}\n")
            file.write('-' * 50 + '\n')
    print(f"News saved in {file_name}")


def show_news(news):
    for i, article in enumerate(news, 1):
        print(f"{i}. {article.get('title', 'No Title')}")
        print(f"Source: {article['source']['name']}")
        print(f"Published: {article.get('publishedAt', 'Unknown')}")
        print(f"Link: {article.get('url', 'No URL')}")
        print('-' * 50)


def main():
    api_key = '697bb948b4064c378281c09703225d14'
    keyword = input("Enter a keyword to search for (or leave empty): ").strip()
    topic = input("Enter a topic (like sports, business) (or leave empty): ").strip()

    if not keyword and not topic:
        print("You need to enter at least a keyword or a topic!")
        return

    news = get_news(api_key, keyword, topic)

    if news:
        print("Here are the latest news articles:\n")
        show_news(news)
        save_news(news)
    else:
        print("No news found. Try a different keyword or topic.")

if __name__ == "__main__":
    main()

