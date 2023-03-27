from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import Responses as R
import Constants as keys


def start_command(update, context):
    update.message.reply_text("Type something")


def handle_messages(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)
    if response.endswith(".jpg") or response.endswith(".png"):
        update.message.reply_photo(photo=response)
    else:
        update.message.reply_text(response)


def error(update, context):
    print(f"update {update} caused error {context.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(MessageHandler(Filters.text, handle_messages))
    dp.add_error_handler(error)

    updater.start_polling()
    print("Bot started...")
    updater.idle()


if __name__ == '__main__':
    main()
