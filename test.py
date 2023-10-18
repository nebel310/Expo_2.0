# import config
# from config import open_weather_token
# import requests
# from pprint import pprint
# import datetime



# def weather(city, open_weather_token):


#     code_to_status = {
#         "Clear" : 'ясно',
#         "Clouds" : 'облачно',
#         "Rain" : 'дождь',
#         "Drizzle" : 'ливень',
#         "Thunderstorm" : 'гроза',
#         "Snow" : 'снег',
#         "Mist" : 'туман'
#     }


#     try:
#         r = requests.get(
#             f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
#         )

#         data = r.json()
#         #pprint(data)

#         city = data["name"]
#         cur_weather = data["main"]["temp"]
#         pressure = data["main"]["pressure"]
#         feels_like = data["main"]["feels_like"]
#         wind = data["wind"]["speed"]
#         sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
#         sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        

#         weather_status = data["weather"][0]["main"]

#         if weather_status in code_to_status:
#             ws = code_to_status[weather_status]
#         else:
#             ws = "я не знаю что на улице. посмотрите в окно."


#         print(f"Температура в городе Москве:\n Температура сейчас: {cur_weather} \n"
#               f"Давление: {pressure}\n"
#               f"Ощущается как: {feels_like}\n"
#               f"Скорость ветра: {wind}\n"
#               f"Закат: {sunset_timestamp} \n Статус погоды: {ws}")

#     except Exception as ex:
#         print(ex)
#         print('Пошел нахер')


# def main():
#     city = 'moscow'
#     weather(city, open_weather_token)


# if __name__ == '__main__':
#     main()


a = 1.1

print(int(a))