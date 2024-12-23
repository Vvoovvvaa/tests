import requests

API_KEY = "89b5075ff5bd2caa9f1ced1d1c2f9aee"

def fetch_weather_data(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    try:
        response = requests.get(url)
        if response.status_code == 200:
             return response.json()
    except Exception as e:
        print(f"Ошибка: {e}")
        return None

def display_weather(data, city, option=None):
    if not data:
        print(f"Не удалось получить данные для города {city}. Проверьте название города.")
        return

    try:
        main = data["main"]
        wind = data["wind"]
        weather = data["weather"][0]

        print(f'Погода в городе {city}:')
        print(f"Температура: {main['temp']}°C")
        print(f"Влажность: {main['humidity']}%")
        print(f"Скорость ветра: {wind['speed']} м/с")
        print(f"Описание: {weather['description']}")

        options = {
            "temperature": f"Температура: {main['temp']}°C",
            "density": f"Давление: {main['pressure']} гПа",
            "humidity": f"Влажность: {main['humidity']}%",
            "wind": f"Скорость ветра: {wind['speed']} м/с"
        }

        if option and option in options:
            print(options[option])
        elif option:
            print(f"Неизвестный параметр: {option}")
    except KeyError as e:
        print(f"Ошибка: отсутствует ключ {e} в данных ответа API.")

def main():
    city = input("Введите название города: ")
    option = input("Введите параметр (temperature, density, humidity, wind) или оставьте пустым для всех данных: ").lower()
    data = fetch_weather_data(city)
    display_weather(data, city, option)

if __name__ == '__main__':
    main()
