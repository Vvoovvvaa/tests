import requests


API_KEY ="89b5075ff5bd2caa9f1ced1d1c2f9aee"

def get_weather(city, option=None):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f'Погода в городе {city}:')
        print(f"Температура: {data['main']['temp']}")
        print(f"Ощущается как: {data['main']['feels_like']}")
        print(f"Влажность: {data['main']['humidity']}")
        print(f"Давление: {data['main']['pressure']}")
        print(f"Скорость ветра: {data['wind']['speed']}")
        print(f"Описание: {data['weather'][0]['description']}")
        
    
       
        if option:
            if option == "":
                  option = None
            elif option == "temperature":
                print(f"Температура: {data['main']['temp']}")
            elif option == "density":
                print(f"Давление: {data['main']['pressure']}")
            elif option == "humidity":
                print(f"Влажность: {data['main']['humidity']}")
            elif option == "wind":
                print(f"Скорость ветра: {data['wind']['speed']}")
            else:
                print(f"Неизвестный параметр: {option}")
    else:
        print(f"Ошибка: не удалось получить данные для города {city}. Проверьте название города.")


def main():
    city = input("Введите название города: ")
    option = input("Введите параметр (temperature, density, humidity, wind) или оставьте пустым для всех данных: ").lower()
    get_weather(city, option)

if __name__ == '__main__':
    main()
