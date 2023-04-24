from aiogram import (
    Dispatcher, types
)


async def send_poll(message: types.Message):
    '''Создаем poll с вариантоми ответов и вопросом'''
    try:
        text = message.text.split(',')
        # Разделяем вопрос от ответов
        question = text[0][8:]
        options = [x for x in text[1:]]

        # Создаем опрос
        poll = types.Poll(
            question=question,
            options=options,
        )
    
        await message.answer_poll(
            question=poll.question,
            options=poll.options,
            type=poll.type,
        )
    except Exception as ex:
        await message.answer('Формат /newpoll вопрос, вариант ответа1, вариант ответа2!')
    


async def poll_help(message: types.Message):
    text = f'Для создания опроса используйте /newpoll\nВ формате /newpoll вопрос, вариант ответа1, вариант ответа2, и другие варианты'
    await message.answer(text)


def register_poll(dp: Dispatcher):
    dp.register_message_handler(send_poll, commands='newpoll')
    dp.register_message_handler(poll_help, commands='poll_help')