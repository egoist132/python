import asyncio
from random import choice
from telethon import TelegramClient
from telethon.events import NewMessage

APP_ID = 1252636
API_HASH = '4037e9f957f6f17d461b0c288ffa50f1'

# 🎮 Тематические эмодзи
BLOCK = '⬛️'
GAMING_EMOJIS = ['🎮', '💻', '🔥', '🕹️', '💥', '⚡️']
MAGIC_PHRASES = ['компы', 'играть', 'пошли в компы']
EDIT_DELAY = 0.03  # немного медленнее для красивой анимации

# "карта" анимации (узор)
PARADE_MAP = '''
00000000000
00111011100
01111111110
01111111110
00111111100
00011111000
00001110000
00000100000
'''

client = TelegramClient('tg-account', APP_ID, API_HASH)


def generate_gaming_pattern():
    output = ''
    for c in PARADE_MAP:
        if c == '0':
            output += BLOCK
        elif c == '1':
            output += choice(GAMING_EMOJIS)
        else:
            output += c
    return output


async def process_invite(event: NewMessage.Event):
    await client.edit_message(event.peer_id.user_id, event.message.id, 'эй 👋')
    await asyncio.sleep(1)
    await client.edit_message(event.peer_id.user_id, event.message.id, 'эй, братан 👊')
    await asyncio.sleep(1)
    await client.edit_message(event.peer_id.user_id, event.message.id, 'пошли в ДОТУ 🎮')
    await asyncio.sleep(1)
    await client.edit_message(event.peer_id.user_id, event.message.id, 'ДОТА ЖДЁТ 💻🔥')
    await asyncio.sleep(1)
    await client.edit_message(event.peer_id.user_id, event.message.id, 'БЫСТРЕЕ ПУДЖ ПУШИТ МИДДДД')


async def process_build_pattern(event: NewMessage.Event):
    output = ''
    for i in range(8):
        output += '\n'
        for j in range(11):
            output += BLOCK
            await client.edit_message(event.peer_id.user_id, event.message.id, output)
            await asyncio.sleep(EDIT_DELAY / 2)


async def process_gaming_animation(event: NewMessage.Event):
    for i in range(50):
        text = generate_gaming_pattern()
        await client.edit_message(event.peer_id.user_id, event.message.id, text)
        await asyncio.sleep(EDIT_DELAY)


@client.on(NewMessage(outgoing=True))
async def handle_message(event: NewMessage.Event):
    msg = event.message.message.lower()
    if any(word in msg for word in MAGIC_PHRASES): # Это функицю чувк не трогай
        await process_build_pattern(event)
        await process_gaming_animation(event)
        await process_invite(event)


if __name__ == '__main__':
    print('[*] Connect to client...')
    client.start()
    client.run_until_disconnected()