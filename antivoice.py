import time
from telethon import TelegramClient, events


tel = '+7**********'
api_id = 000000
api_hash = '********************************'
# Телеграм API ид и API хеш с сайта https://my.telegram.org/apps

bot = TelegramClient("session_id", api_id, api_hash)
bot.start(phone=tel)
# Ваш номер телефона. при первом запуске вы получите код на телеграм, вводите его в консоль
whitelist = []  # Список белого листа с id пользователей
voice_len = 5  # Мин длина голосового


def fuck(x):  # Переопределение длины голосовых
    global voice_len
    voice_len = x


# Обработка команды voice_true|voice_false
@bot.on(events.NewMessage(outgoing=True, pattern='(?i)voice_true|voice_false|voice5|voice10|voice15'))
async def addWhitelist(event):
    user_id = event.message.peer_id.user_id
    m_text = event.message.text.lower()

    if m_text == 'voice_true':  # Если ввели команду voice_true
        if user_id not in whitelist:
            whitelist.append(user_id)
            await bot.delete_messages(event.chat_id, [event.id])  # Удаление команды voice_true из чата
            await event.respond('__Вам разрешили функцию голосовых сообщений.__')
        else:
            await bot.delete_messages(event.chat_id, [event.id])
            # Удаление команды voice_true из чата при повторном вводе
            m = await event.respond('__Пользователь уже белом списке голосовых сообщений.__')
            # Записываем event в переменную m
            time.sleep(2)  # Задержка на 2сек до удаление
            await bot.delete_messages(event.chat_id, [m.id])
            # Удаляем текст "__Пользователь уже белом списке голосовых сообщений.__" полученным id из переменной m
    elif m_text == 'voice_false':  # Если ввели команду voice_false
        if user_id in whitelist:
            whitelist.remove(user_id)
            await bot.delete_messages(event.chat_id, [event.id])  # Удаление команды voice_false из чата
            await event.respond('__Вам ограничили функцию голосовых сообщений.__')
        else:
            await bot.delete_messages(event.chat_id, [event.id])
            # Удаление команды voice_false из чата при повторном вводе
            m = await event.respond('__Пользователь уже черном списке голосовых сообщений.__')
            # Записываем event в переменную m
            time.sleep(2)  # Задержка на 2сек до удаление
            await bot.delete_messages(event.chat_id, [m.id])
            # Удаляем текст "__Пользователь уже черном списке голосовых сообщений.__" полученным id из переменной m
    elif m_text == "voice5":
        await bot.delete_messages(event.chat_id, [event.id])
        # Удаление команды voice5 из чата
        m = await event.respond('__Голосовые сообщение до 5сек под запретом.__')
        fuck(5)
        time.sleep(2)  # Задержка на 2сек до удаление
        await bot.delete_messages(event.chat_id, [m.id])
        # Удаляем текст "__Голосовые сообщение до 5сек под запретом.__" полученным id из переменной m
    elif m_text == "voice10":
        await bot.delete_messages(event.chat_id, [event.id])
        # Удаление команды voice10 из чата
        m = await event.respond('__Голосовые сообщение до 10сек под запретом.__')
        fuck(10)
        time.sleep(2)  # Задержка на 2сек до удаление
        await bot.delete_messages(event.chat_id, [m.id])
        # Удаляем текст "__Голосовые сообщение до 10сек под запретом.__" полученным id из переменной m
    elif m_text == "voice15":
        await bot.delete_messages(event.chat_id, [event.id])
        # Удаление команды voice15 из чата
        m = await event.respond('__Голосовые сообщение до 15сек под запретом.__')
        fuck(15)
        time.sleep(2)  # Задержка на 2сек до удаление
        await bot.delete_messages(event.chat_id, [m.id])
        # Удаляем текст "__Голосовые сообщение до 15сек под запретом.__" полученным id из переменной m


@bot.on(events.NewMessage(incoming=True))
async def NewMes(event):
    if (event.chat_id > 0) and (event.chat_id not in whitelist):
        if event.message.voice and (event.message.voice.attributes[0].duration < voice_len):
            await event.respond('__Пользователь ограничил функцию голосовых сообщений.__')
            await bot.delete_messages(event.chat_id, [event.id])


bot.run_until_disconnected()
