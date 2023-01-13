# Библиотека 👇
# pip install python-telegram-bot --pre

from telegram import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telegram.ext import filters, ApplicationBuilder, MessageHandler
async def send_data(update, context):
    message = update.message.text
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'Хочешь посмотреть в городе {message}?',
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Посмотреть...', web_app=WebAppInfo(f'https://wttr.in/{message}'))]
        ])
    )
bot = ApplicationBuilder().token('5802737784:AAFuNPswGYDU5KkDEpgJkRXcMWyNFBtOC3Q').build()
bot.add_handler(MessageHandler(filters.TEXT, send_data))
bot.run_polling()