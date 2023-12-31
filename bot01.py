import asyncio
import logging
import sys
from os import getenv
import json

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

# Bot token can be obtained via https://t.me/BotFather
TOKEN = '6862552140:AAHwKP4xWWHLv16LRsPGIuBuRTfw2gJ3XIM'

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    with open('msgs/' + repr(message.from_user.id) + '.txt', 'w') as f:
        f.write('{"step": "This is great begining of new conversation!"}')
        f.close()
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")

    
        
        
@dp.message()
async def give_smth(message: types.Message) -> None:
    if message.text == 'groovy':
        f = open('msgs/' + repr(message.from_user.id) + '.txt', 'r')
        params = json.loads(f.readline())
        await message.answer(params['step'])
    else:
        await message.answer("That's right way almost!")

        

async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())