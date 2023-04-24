from aiogram import (
    Dispatcher, types
)
import requests
from src.config import load_config


async def get_weather(message: types.Message):
    '''Через API получаем температуру и описание погоды в указаном городе'''
    api_key = load_config().tg_bot.weather
    city = message.text.split()[-1]
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    # Достаем из данныз температуру и описание погоды
    tempeature = data['main']['temp']
    info = data['weather'][0]['description']

    text = f'Погода в {city} сейчас {info} и {tempeature} по °C'

    await message.answer(text)
    

async def weather_help(message: types.Message):
    text = f'Чтобы получить погоду используйте /weather в формате /weather Washington'
    await message.answer(text)


def register_weather(dp: Dispatcher):
    dp.register_message_handler(get_weather, commands='weather')
    dp.register_message_handler(weather_help, commands='weather_help')