from telegram.ext import CommandHandler, Updater
from telegram import Bot, Update
from credentials import bot_token

TOKEN = bot_token
bot = Bot(TOKEN)

# This is the initial message upon the User clicking on 'Start'
def start(update: Update, context):
    greeting = 'Hi, I am NUSCopilot! How can I help?'
    bot.send_message(chat_id=update.message.chat_id, text=greeting)

# This is the tentative list of commands for the Bot
def help(update: Update, context):
    avail_commands = [
        '/help --> Your help a tap away ~',
        '/makan --> Grab a snack from SuperSnacks?',
        '/spaces --> Book your facilities?',
        '/feedback --> Want to provide suggestions for improvements?'
    ]
    help_text = '\n'.join(avail_commands)
    bot.send_message(chat_id=update.message.chat_id, text=f'Available commands:\n\n{help_text}')

def makan(update: Update, context):
    bot.send_message(chat_id=update.message.chat_id, text='Implementation in progress')

def spaces(update: Update, context):
    bot.send_message(chat_id=update.message.chat_id, text='Implementation in progress')

def feedback(update: Update, context):
    bot.send_message(chat_id=update.message.chat_id, text='Implementation in progress')

def main():
    updater = Updater(TOKEN)

    # What actions to be triggered when the dispatcher receives update from the updater
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("makan", makan))
    dispatcher.add_handler(CommandHandler("spaces", spaces))
    dispatcher.add_handler(CommandHandler("feedback", feedback))

    updater.start_polling()

if __name__ == '__main__':
    import logging
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%I:%M:%S %p',
        level=logging.INFO,
    )

    logger = logging.getLogger(__name__)

    try:
        main()
    except Exception as e:
        logger.error(e)
