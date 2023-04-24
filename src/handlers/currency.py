import requests
import json
from money import valut
from aiogram import (
    Dispatcher, types,
)
from src.config import load_config

async def convert(message: types.Message): 
    '''Проводим ваолидацию входных данных и отпровляем через API данные ковертации, отпровляем конечный результат'''       
    text = message.text.split()
    api_key = load_config().tg_bot.currency
    if len(text) == 4:
        try:
            # Делаем универсальным запрос
            amount = text[1]
            from_ = text[2].upper()
            to = text[3].upper()
            
            if from_ not in valut or to not in valut:
                await message.answer('Чтобы получить список доступных валют введите: /currancy_info')
            
            if not amount.replace('.', '').isdigit():
                await message.answer('Только положительные числа')
            
            # Отпровляем запрос
            data = requests.get(f'https://api.fastforex.io/convert?from={from_}&to={to}&amount={amount}&api_key={api_key}').text
            json_data = json.loads(data)
            response = f"{amount} {from_} 🤸‍♂️ {json_data['result'][to]} {to}"

            await message.answer(response)
        except Exception as ex:
            message.answer('Упс, ошибка соеденения, попробуйте позже(')

    else:
        await message.answer('Формат: /convert 425000 RUB USD, где RUB переводятся в USD')


async def currancy_info(message: types.Message):
    photo_1 = open('media/first.png', 'rb')
    photo_2 = open('media/second.png', 'rb')

    await message.answer_photo(photo_2)
    await message.answer_photo(photo_1)


async def convert_help(message: types.Message):
    text = f'Для ковертации волют используйте /convert в формате: /convert 425000 RUB USD, где RUB переводятся в USD\nЧтобы получить список доступных валют введите: /currancy_info'
    await message.answer(text)



def register_currency(dp: Dispatcher):
    dp.register_message_handler(convert, commands='convert')
    dp.register_message_handler(currancy_info, commands='currancy_info')
    dp.register_message_handler(convert_help, commands='convert_help')