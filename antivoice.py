from telethon import TelegramClient, events, sync, utils
import time

api_id = 0000000
api_hash = '*********************************'

bot = TelegramClient("session_id", api_id, api_hash)
bot.start("+7*********")
# If you have a cloud password, just set field like bot.start("PHONE NUMBER")
whitelist = []


@bot.on(events.NewMessage(outgoing=True, pattern='(?i)voice_true|voice_false'))
async def addWhitelist(event):
    user_id = event.message.peer_id.user_id
    if event.message.text == 'voice_true' or event.message.text == 'Voice_true':
        if user_id not in whitelist:
            whitelist.append(user_id)
            await bot.delete_messages(event.chat_id, [event.id])
            await event.respond('__Вам разрешили функцию голосовых сообщений.__')
        else:
            await bot.delete_messages(event.chat_id, [event.id])
            m = await event.respond('__Пользователь уже белом списке голосовых сообщений.__')
            time.sleep(2)
            await bot.delete_messages(event.chat_id, [m.id])
    elif event.message.text == 'voice_false' or event.message.text == 'Voice_false':
        if user_id in whitelist:
            whitelist.remove(user_id)
            await bot.delete_messages(event.chat_id, [event.id])
            await event.respond('__Вам ограничили функцию голосовых сообщений.__')

        else:
            await bot.delete_messages(event.chat_id, [event.id])
            m = await event.respond('__Пользователь уже черном списке голосовых сообщений.__')
            time.sleep(2)
            await bot.delete_messages(event.chat_id, [m.id])


@bot.on(events.NewMessage(incoming=True))
async def NewMes(event):
    if (event.chat_id > 0) and (event.chat_id not in whitelist):
        if event.message.voice and (event.message.voice.attributes[0].duration < 10):
            await event.respond('__Пользователь ограничил функцию голосовых сообщений.__')
            await bot.delete_messages(event.chat_id, [event.id])


bot.run_until_disconnected()
