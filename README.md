# TelegramAntiVoice-telethon

Антиголосовой скрипт для телеграмм на основе telethon

# Установака
1. Скачать скрипт
2. Измените значения в
```
api_id = 000000
api_hash = ""

bot = TelegramClient("session_id", api_id, api_hash)
bot.start("ВАШ НОМЕР")
```
3. Запуск через консоль или любую IDE

# Опции 
1. Вы можете изменить длину удаленных голосовых сообщений, изменив значение в строке ``` if (event.message.voice) и (event.message.voice.attributes [0] .duration <10): ``` . Значение по умолчанию - 10 секунд.
2. Вы можете добавить пользователей, чьи сообщения не будут фильтроваться, написав им чат ``` voice_true ``` . Или можете запретить , написав им чат ``` voice_false ``` . Значение по умолчанию - ``` voice_false ``` .