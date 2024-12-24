import requests

def get_news(api_key, keyword):
    url = f'https://newsapi.org/v2/everything?q={keyword}&apiKey={api_key}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['articles']
        else:
            print("Ошибка при получении новостей.")
            return []
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return []

def save_news(news):
    with open("news.txt", "w", encoding="utf-8") as file:
        for article in news:
            title = article.get('title', 'Без заголовка')
            url = article.get('url', 'Без ссылки')
            file.write(f"Заголовок: {title}\nСсылка: {url}\n\n")
    print("Новости сохранены в файл news.txt")

def main():
    api_key = "697bb948b4064c378281c09703225d14"  
    keyword = input("Введите ключевое слово для поиска новостей: ")

    if not keyword:
        print("Вы не ввели ключевое слово.")
        return

    news = get_news(api_key, keyword)

    if news:
        print("\nПоследние новости:")
        for article in news:
            print(f"Заголовок: {article.get('title', 'Без заголовка')}")
            print(f"Ссылка: {article.get('url', 'Без ссылки')}\n")
        save_news(news)
    else:
        print("Новостей по вашему запросу не найдено.")

if __name__ == "__main__":
    main()
