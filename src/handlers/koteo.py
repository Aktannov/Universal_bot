import requests
from bs4 import BeautifulSoup
from aiogram import (
    Dispatcher, types
)
import random


    
async def send_koteo(message: types.Message):
    '''Парсим google images, где достаем случайное изображение'''
    try:
        url = 'https://www.google.com/search?q=cats+pinterest&sxsrf=APwXEddhRvRYyBCoriM1iO3R1hkAXcu0xQ:1682173052148&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiDieX51r3-AhUJkMMKHbGADW8Q_AUoAXoECAEQAw&biw=1920&bih=950&dpr=1'
        response = requests.get(url).text

        # Парсим фотки и отпровляем, не сохроняя их у себя 
        soup = BeautifulSoup(response, 'lxml')
        listing = soup.find_all('img')
        photo = str(listing[random.randint(1, 20)]).split(' ')[3][5:-3]
        await message.answer_photo(photo)
    except Exception as ex:
        await message.answer('Упс, ошибка соеденения, попробуйте позже(')


def register_koteo(dp: Dispatcher):
    dp.register_message_handler(send_koteo, commands='koteo')