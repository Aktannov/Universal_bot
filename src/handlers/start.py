from aiogram import Dispatcher, types

async def start_info(message: types.Message):
    text = f'Функции данного бота:\n- /weather_help погода в вашем городе\n- /convert_help конвертация валют\n- /poll_help создание опроса\n- /koteo 🐱🐱🐱'
    await message.answer(text)

def register_info(dp: Dispatcher):
    dp.register_message_handler(start_info, commands='start')