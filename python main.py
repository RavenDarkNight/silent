import os
import datetime
import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor 

bot = Bot(token='7888778707:AAG1254oxPDwFeR9ZKniRxrGOqI8B0ayIQ8')
dp = Dispatcher(bot)
@dp.message.handler(commands=["start"])
async def start_command(message: types.Message):
	await message.reply("Привет! Напиши мне название города и я пришлю сводку погоды")

if __name__ == "__main__":
	# С помощью метода executor.start_polling опрашиваем
     # Dispatcher: ожидаем команду /start
	executor.start_polling(dp)