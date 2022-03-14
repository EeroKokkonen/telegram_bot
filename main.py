import constants as keys
from telegram.ext import *
import responses as R

print("Bot started...")

def krypto_command(update,context):
    text = [(update.message.text).lower()]
    text = text[0].split()
    try:
        response = R.krypto(text[1]) + R.lisa_valinta(text[1], text[2])
    except Exception as e:
        print(e)
        response = R.krypto(text[1])

    update.message.reply_text(response)

def louhinta_command(update,context):
    text = [update.message.text.lower()]
    text = text[0].split()

    try:
        response = R.louhinta(text[1], float(text[2]))
    except Exception as e:
        print(e)
        response = R.louhinta(text[1], 100)

    update.message.reply_text(response)


def osake_command(update,context):
    text = [update.message.text.lower()]
    text = text[0].split()
    response = R.osake(text[1])

    update.message.reply_text(response)


def main():
    updater = Updater(keys.TG_API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("krypto", krypto_command))
    dp.add_handler(CommandHandler("louhinta", louhinta_command))
    dp.add_handler(CommandHandler("osake", osake_command))

    updater.start_polling(1)
    updater.idle()

main()
