import requests
import time

def get_crypto_data(filter_name=None, filter_price=None):
    try:
        url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=15&page=1&sparkline=false"
        response = requests.get(url)
        if response.status_code != 200:
            print("Ошибка при запросе данных.")
            return []

        data = response.json()
        filtered_data = []

        for coin in data:
            name = coin["name"]
            price = coin["current_price"]

            if filter_name and filter_name.lower() not in name.lower():
                continue
            if filter_price and price <= filter_price:
                continue

            filtered_data.append({
                "name": name,
                "symbol": coin["symbol"],
                "price": price,
                "market_cap": coin["market_cap"],
                "volume": coin["total_volume"],
                "change": coin["price_change_percentage_24h"]
            })

        return filtered_data
    except Exception as e:
        print("Ошибка:", e)
        return []

def display_data(data):
    if not data:
        print("Нет данных для отображения.")
        return

    for coin in data:
        print(f"Имя: {coin['name']}, Символ: {coin['symbol']}")
        print(f"Цена: ${coin['price']}, Рыночная капитализация: ${coin['market_cap']}")
        print(f"Объём: ${coin['volume']}, Изменение за 24ч: {coin['change']}%")
        print("-" * 30)

def main():
    while True:
        name_filter = input("Фильтр по имени (оставьте пустым для пропуска): ")
        price_filter = input("Фильтр по минимальной цене (оставьте пустым для пропуска): ")
        data = get_crypto_data(name_filter, price_filter)
        display_data(data)

        print("Обновление через 5 секунд...")
        time.sleep(5)

if __name__ == "__main__":
    main()
