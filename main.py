from stt import *
from tts import *
import config
from config import open_weather_token
import requests
from pprint import pprint
import datetime




def greeting():
    speak('привет')


def goodbye():
    speak('до свидания')


def help():
    speak('я умею показывать погоду, считать, писать и переводить, как чи+сла, так, и буквы')




def weather(city, open_weather_token, command):


    code_to_status = {
        "Clear" : 'ясная',
        "Clouds" : 'облачная',
        "Rain" : 'дождь',
        "Drizzle" : 'ливень',
        "Thunderstorm" : 'гроза',
        "Snow" : 'снег',
        "Mist" : 'туманно'
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )

        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]
        pressure = data["main"]["pressure"]
        feels_like = data["main"]["feels_like"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        

        weather_status = data["weather"][0]["main"]

        if weather_status in code_to_status:
            ws = code_to_status[weather_status]
        else:
            ws = "я не могу понять погоду. посмотрите в окно."
        
        speak("Что вам подсказать по погоде?")
        if 'полная сводка' in listen():
            text = f"В городе москве сейчас:, {int(cur_weather)} градусов, но ощущается как {int(feels_like)}."

            if code_to_status["Clouds"] or code_to_status["Clear"]:
                text += ' Погода {ws}.'
            elif code_to_status["Rain"] or code_to_status["Drizzle"] or code_to_status["Thunderstorm"]:
                text += ' На улице {ws}.'

            text += f' Скорость ветра {int(wind)} метров в секунду. Давление {pressure} паскаль.'
            speak(text)

        elif 'сколько градусов' in listen():
            text = f"В городе москве сейчас:, {int(cur_weather)} градусов, но ощущается как {int(feels_like)}."

            if code_to_status["Clouds"] or code_to_status["Clear"]:
                text += ' Погода {ws}.'
            elif code_to_status["Rain"] or code_to_status["Drizzle"] or code_to_status["Thunderstorm"]:
                text += ' На улице {ws}.'
            
            speak(text)
        
        elif 'ветер' in listen() or 'давление' in listen():
            text = f'Скорость ветра {int(wind)} метров в секунду. Давление {pressure} паскаль.'
            speak(text)
        
        elif 'когда' in listen() or 'закат' in listen() or 'рассвет' in listen():
            text = f"Рассвет {sunrise_timestamp}, а закат {sunset_timestamp}"
            speak(text)
        
        else:
            pass
            #УСЛОВИЕ ВЫХОДА ИЗ ФУНКЦИИ


    except Exception as ex:
        print(ex)
        print('Ошибка в погоде')




def open_browser():
    speak('команда в разработке')


def calc():
    speak('команда в разработке')


def convert():
    speak('команда в разработке')


def translate():
    speak('команда в разработке')




def main():
    city = 'moscow'
    speak(f'Здравствуйте, я ваш виртуальный друг, {config.SP_NAME}.')

    while True:
        user_command = listen()
        try:
            execute_command(user_command)
        except CommandNotFoundException:
            print('команда не найдена')
        except Exception as e:
            speak('попробуй сказать еще раз')
            print("Ошибка в main.")
        

def execute_command(command):
    for cmd, synonyms in config.VA_CMD_LIST.items():
        if command in synonyms:
            if cmd == "greeting":
                greeting()
            elif cmd == 'goodbye':
                goodbye()
            elif cmd == 'help':
                help()
            elif cmd == 'weather':
                weather()
            elif cmd == 'open_browser':
                open_browser()
            elif cmd == 'calc':
                calc()
            elif cmd == 'convert':
                convert()
            elif cmd == 'translate':
                translate()
            return

    raise CommandNotFoundException()


class CommandNotFoundException(Exception):
    pass


if __name__ == "__main__":
    main()