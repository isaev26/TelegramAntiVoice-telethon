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
1. Вы можете изменить длину удаленных голосовых сообщений, написав в чат ``` voice5 ``` длина 5сек, ``` voice10 ``` длина 10сек, ``` voice15 ``` длина 15сек. Значение по умолчанию - 5 секунд.
2. Вы можете добавить пользователей, чьи сообщения не будут фильтроваться, написав им в чат ``` voice_true ``` . Или можете запретить , написав им в чат ``` voice_false ``` . Значение по умолчанию - ``` voice_false ``` .

# Поддержка
Приветствуется любая помощь ;)