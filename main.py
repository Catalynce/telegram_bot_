from telegram.ext import CommandHandler, Updater, MessageHandler, CallbackQueryHandler, CallbackContext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

updater = Updater(token='1755775018:AAFeUk_3Paa1LDA9cp1W6xsBw0t_FDHNu0A')
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Даров! Это бот."
                                                                    "Если будет нужна помощь пиши: /help")

def WRX(update: Update, _: CallbackContext) -> ' ':
    keyboard = [
        [
            InlineKeyboardButton("Option 1", callback_data='1'),
            InlineKeyboardButton("Option 2", callback_data='2'),
        ],
        [InlineKeyboardButton("Option 3", callback_data='3')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Please choose:', reply_markup=reply_markup)


def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет")

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=
    f'''/Creator - создатель бота.
/Games - игры
/Music - музыка''')

def Creator(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'''https://vk.com/id_kostyl_gang - Vk
https://t.me/Catalynce - telegram''')

def echo(update, context,):
    help_text = f'''Я не знаю команду {update.message.text}
/help - список команд.'''
    context.bot.send_message(chat_id=update.effective_chat.id, text=help_text)

def button(update: Update, _: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=f"Selected option: {query.data}")


updater.dispatcher.add_handler(CommandHandler('WRX', WRX))
updater.dispatcher.add_handler(CallbackQueryHandler(button))

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

hello_handler = CommandHandler('hello', hello)
dispatcher.add_handler(hello_handler)

help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

Creator_handler = CommandHandler('Creator', Creator)
dispatcher.add_handler(Creator_handler)


updater.start_polling()
updater.idle()