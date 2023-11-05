from stt import *
from tts import *
import config
from config import open_weather_token
import requests
from pprint import pprint
import datetime
from num2words import num2words
import subprocess
import webbrowser
from playsound import playsound
import random





def greeting():
    speak('привет.')


def goodbye():
    speak('до свидания.')


def help():
    speak('я умею показывать погоду, считать, писать и переводить, как чи+сла, так, и буквы, а также выполнять простые действия с вашим компьютером.')




def thank():
    speak("Всегда пожалуйста.")




def weather(city, open_weather_token):


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
        
        print('cheked: weather')
        text = f"В городе москве сейчас:, {num2words(int(cur_weather), lang='ru')} градусов по ц+е+льсию, но ощущается как {num2words(int(feels_like), lang='ru')}."

        if ws == code_to_status["Clouds"] or ws == code_to_status["Clear"]:
            text += f' Погода {ws}.'
        elif code_to_status["Rain"] or code_to_status["Drizzle"] or code_to_status["Thunderstorm"]:
            text += f' На улице {ws}.'

        text += f" Скорость ветра {num2words(int(wind), lang='ru')} метров в секунду. Давление {num2words(int(pressure), lang='ru')} паскаль."
        speak(text)


    except Exception as ex:
        print(ex)
        print('Ошибка в погоде')




def open_browser():
    path_to_exe = "C:/Users/vladg/AppData/Local/Yandex/YandexBrowser/Application/browser.exe"
    subprocess.Popen(path_to_exe)


def open_sites():
    speak("Какой сайт открыть?")
    search = listen()
    # search = str(input("Сайт: "))

    if 'мэш' in search or 'меж' in search or 'мэж' in search:
        webbrowser.open('https://dnevnik.mos.ru/diary/schedules', new=0)

    elif 'ютуб' in search:
        webbrowser.open('https://youtube.com', new=0)

    elif 'поисковик' in search or 'яндекс' in search:
        webbrowser.open('https://yandex.com', new=0)
    
    elif 'переводчик' in search:
        webbrowser.open('https://translate.yandex.ru/', new=0)
    
    elif 'перплексити' in search or 'чат' in search or 'чат джипити' in search:
        webbrowser.open('https://www.perplexity.ai/', new=0)
    
    elif 'сборник' in search:
        webbrowser.open('https://vk.com/doc3619616_672138766?hash=lMtTIuayMdBoxRCGj2dinguhNOWEcyD5zByEVv01I8o', new=0)
    
    elif 'математика' in search:
        webbrowser.open('https://app.idroo.com/boards/PsMhS6XVtj', new=0)
        webbrowser.open('https://mathb-ege.sdamgia.ru/', new=0)
    
    else:
        speak("Это сложно. Поискать в интернете?")

        if 'да' in listen() or 'давай' in listen():
            speak(f"Вот, что мне удалось найти по запросу, {search}.")
            url = f"https://www.yandex.com/search?text={search}"
            webbrowser.open(url, new=0)

        else:
            print("exit")




def calc():
    speak('команда в разработке.')




def convert():
    speak('команда в разработке.')




def translate():
    speak('команда в разработке.')




def main():
    city = 'moscow'
    # speak(f'Здравствуйте, я ваш виртуальный друг, {config.SP_NAME}.')
    speak(f'Чпокс.')

    while True:
        user_command = listen()
        # Для теста:
        # user_command = str(input("Команда: "))
        try:
            execute_command(user_command)
        except CommandNotFoundException:
            print('команда не найдена')
        except Exception as e:
            speak('попробуй сказать еще раз.')
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
            elif cmd == 'thank':
                thank()
            elif cmd == 'weather':
                weather('moscow', config.open_weather_token)
            elif cmd == 'open_browser':
                open_browser()
            elif cmd == 'open_sites':
                open_sites()
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
