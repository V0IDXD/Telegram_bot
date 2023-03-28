import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import view_source as vs
import Constants as keys


def start_command(update, context):
    update.message.reply_text("Type something")


def handle_messages(update, context):
    text = str(update.message.text).lower()
    user_message = str(text).lower()
    k = user_message.split("//")
    if "tapas.io" in k[1]:
        update.message.reply_text("Ek min...")
        response_ls = vs.get_image_url(user_message)
        title, temp_link, temp_sc = response_ls
        update.message.reply_text(f"Title: <b>{title}</b>", parse_mode='HTML')
        with requests.get(temp_link, stream=True) as r:
            r.raise_for_status()
            update.message.reply_photo(r.raw)
        update.message.reply_text(f"<i>Secret Panel--></i>", parse_mode='HTML')
        update.message.reply_animation(animation=temp_sc)


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
