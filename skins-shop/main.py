from aiogram import executor, Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TOKEN

# config.py
# PROVIDER_PAYMASTER_TOKEN = "PROVIDER_PAYMASTER_TOKEN"
#
# TOKEN = "TOKEN"
# if not TOKEN:
#     exit('Error: token not found!')

bot = Bot(
    token=TOKEN,
    parse_mode=types.ParseMode.HTML,
)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

if __name__ == '__main__':
    executor.start_polling(dp)