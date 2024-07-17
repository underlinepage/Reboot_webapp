from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Начать", web_app={"url": "https://your-repo-name.github.io/reboot-webapp/index.html"})]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Добро пожаловать в ReBoot! Нажмите кнопку ниже, чтобы начать.', reply_markup=reply_markup)

def main() -> None:
    token = '7488471918:AAGiQ14HSIJPN5DJiw8RHhE3uF8WLMnPFk4'
    updater = Updater(token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
