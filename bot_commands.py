from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
import os
# import XandO as xo

def calcrun(userexp):
    return eval(userexp)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'/hi\n/time\n/help\n/calc')

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет {update.effective_user.first_name}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'/hi\n/time\n/help\n/sum')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{datetime.datetime.now().time()}')


async def calc_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Результат выражения: {calcrun(update.message.text.split(" ")[1])}')
