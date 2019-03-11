# myapp/telegrambot.py
# Example code for telegrambot.py module
from pprint import pprint

import telegram
from telegram.ext import CommandHandler, MessageHandler, Filters
from django_telegrambot.apps import DjangoTelegramBot

import logging

from app_blog.models import Post
from toc.utils import QueryObjects

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    bot.sendMessage(update.message.chat_id,
                    text='Hello. Use /post X command, where X is a post id at https://turbo-octo-cat-project-001.herokuapp.com/')


def help(bot, update):
    chat_id = update.message.chat_id
    # bot.send_message(update.message.chat_id, text='::')
    # update.message.reply_text(f"Here is your query: ")
    # bot.send_photo(chat_id=chat_id, photo=open('app_blog/static/app_blog/logo_transparent.png', 'rb'))
    # bot.send_document(chat_id=chat_id, document=open('/Users/jeronimoprogrammer/Desktop/WHR_web.pdf', 'rb'))

    custom_keyboard = [['top-left', 'top-right'],
                       ['1', '2', 'tree'],
                       ['bottom-left', 'bottom-right']]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    bot.send_message(chat_id=chat_id,
                     text="Custom Keyboard Test",
                     reply_markup=reply_markup)

    reply_markup = telegram.ReplyKeyboardRemove()
    bot.send_message(chat_id=chat_id, text="I'm back.", reply_markup=reply_markup)


def post(bot, update, args):
    post = QueryObjects.get_object(Post, args[0])
    bot.send_message(chat_id=update.message.chat_id,
                     text=f'''*{post.title.upper()}*    
 
{post.content} [{update.message.chat.username}](tg://user?id={update.message.chat.id})
```block_language
Your code here
```
`inline fixed-width code`
''',
                     parse_mode=telegram.ParseMode.MARKDOWN)

    '''
    *bold text*
    _italic text_
    [inline URL](http://www.example.com/)
    [inline mention of a user](tg://user?id=123456789)
    `inline fixed-width code`
    ```block_language
    pre-formatted fixed-width code block
    '''


def echo(bot, update):
    bot.sendMessage(update.message.chat_id, text=update.message.text)


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    logger.info("Loading handlers for telegram bot")

    # Default dispatcher (this is related to the first bot in settings.DJANGO_TELEGRAMBOT['BOTS'])
    dp = DjangoTelegramBot.dispatcher
    # To get Dispatcher related to a specific bot
    # dp = DjangoTelegramBot.getDispatcher('BOT_n_token')     #get by bot token
    # dp = DjangoTelegramBot.getDispatcher('BOT_n_username')  #get by bot username

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("post", post, pass_args=True))

    # on noncommand i.e message - echo the message on Telegram
    # dp.add_handler(MessageHandler([Filters.text], echo))

    # log all errors
    dp.add_error_handler(error)
