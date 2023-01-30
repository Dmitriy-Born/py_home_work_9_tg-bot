from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import bot_commands as bc
# import XandO as XO
import datetime


app = ApplicationBuilder().token("5724308043:AAE1xDePWbG4LQegS3YBrMr3dAPPHcRUavU").build()

app.add_handler(CommandHandler("start", bc.start_command))
app.add_handler(CommandHandler("hi", bc.hi_command))
app.add_handler(CommandHandler("time", bc.time_command))
app.add_handler(CommandHandler("help", bc.help_command))
app.add_handler(CommandHandler("calc", bc.calc_command))
# app.add_handler(CommandHandler("xo", bc.xo))

print('start_server')

app.add_handler(CommandHandler("hello", bc.hi_command))

app.run_polling()