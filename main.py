import constants as keys
from telegram.ext import *
import responses as R

print("Bot started...")

def help_command(update,context):
    response = R.help()

    update.message.reply_text(response)


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
    text = text[0].split()  # Parsing user message to list
    response = ""
    kortti = True   # Determines if user want to know mining info from specific card or not
    valuutat = ['eth', 'rvn', 'cfx', 'ton', 'erg']

    if text[1] == "3070ti":
        louhinta_nopeus = [60, 36, 75, 3130, 171]
    elif text[1] == "3060":
        louhinta_nopeus = [36, 24.6, 46, 1860, 121]
    elif text[1] == "3060ti":
        louhinta_nopeus = [62, 30.5, 56, 2410, 173]
    elif text[1] == "3060til":
        louhinta_nopeus = [45, 31, 53, 2320, 144]
    elif text[1] == "3080ti":
        louhinta_nopeus = [90, 59, 112, 4880, 269]
    elif text[1] == "3080":
        louhinta_nopeus = [100, 42, 92, 4330, 228]
    elif text[1] == "3080l":
        louhinta_nopeus = [72, 49, 90, 4110, 226]
    elif text[1] == "3070":
        louhinta_nopeus = [62, 32, 58, 2780, 173]
    elif text[1] == "3070l":
        louhinta_nopeus = [45, 32, 59, 2780, 146]
    elif text[1] == "1660s":
        louhinta_nopeus = [31.7, 14.2, 25, 1280, 62.9]
    else:
        kortti = False


    if kortti == True:
        for i in range(len(valuutat)):
            response += R.louhinta(valuutat[i], louhinta_nopeus[i], 1) + "\n"
    else:
        try:
            response = R.louhinta(text[1], float(text[2]), 0)
        except Exception as e:
            response = R.louhinta(text[1], 100, 0)

    update.message.reply_text(response)


def osake_command(update,context):
    text = [update.message.text.lower()]
    text = text[0].split()
    response = R.osake(text[1])

    update.message.reply_text(response)

def kellotus_command(update,context):
    text = [update.message.text.lower()]
    text = text[0].split()

    response = R.kellotus(text[1])

    update.message.reply_text(response)


def main():
    updater = Updater(keys.TG_API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("krypto", krypto_command))
    dp.add_handler(CommandHandler("louhinta", louhinta_command))
    dp.add_handler(CommandHandler("osake", osake_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("kello", kellotus_command))

    updater.start_polling(1)
    updater.idle()

main()
