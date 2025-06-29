
import telebot
import os

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🕋 Islomiy kitoblar", "📈 Top 100 kitoblar")
    bot.send_message(message.chat.id,
    "Assalomu alaykum!\n\n"
    "Botimizga hush kelibsiz. Men sizga kitoblar haqida yordam bera olaman."
)
@bot.message_handler(func=lambda message: message.text == "📈 Top 100 kitoblar")
def top_books(message):
    bot.send_document(message.chat.id, "BQACAgIAAxkBAAIFPWhhXKsEZgHTew7T8R19Y8aebBt5AAKyfQACVbwRS4y7Bhr1YAgvNgQ")

@bot.message_handler(func=lambda message: message.text == "🕋 Islomiy kitoblar")
def islomic_books(message):
    bot.send_message(message.chat.id, "🕌 Islomiy kitoblar bo‘limi:
/jannat_vasfi
/baxtli_hayot
/tafsiri_hilol")

@bot.message_handler(commands=['jannat_vasfi'])
def send_jannat(message):
    bot.send_document(message.chat.id, "BQACAgIAAxkBAAIFMWhhXKj9wSbRXR2PuX87SusD_SfCAAKtfQACVbwRS8s00cjEUqRtNgQ")

@bot.message_handler(commands=['baxtli_hayot'])
def send_baxtli(message):
    bot.send_document(message.chat.id, "BQACAgIAAxkBAAIFOmhhXKosSVrR28TAn9X6wUnw1P5FAAKxfQACVbwRSyRuVmhuqdYNNgQ")

@bot.message_handler(commands=['tafsiri_hilol'])
def send_tafsir(message):
    files = [
        ("BQACAgIAAxkBAAIFLmhhXKdgu11GhgwQ18D9OOViFhGnAAKrfQACVbwRS4MNu7y8ExOsNgQ", "Tafsiri Hilol 1-juz"),
        ("BQACAgIAAxkBAAIFKGhhXKN0cN8EiQkosHXLOWtjqlqsAAKpfQACVbwRS-chZ6AkeVqANgQ", "Tafsiri Hilol 2-juz"),
        ("BQACAgIAAxkBAAIFKmhhXKUFCars3HsQ2LlQGMSSFoThAAKqfQACVbwRS5D7QRnHad3-NgQ", "Tafsiri Hilol 3-juz"),
        ("BQACAgIAAxkBAAIFLGhhXKaoMPAhlF29fzGApDliwK3ZAAJlfgACSksQS0WWXCsvjV4lNgQ", "Tafsiri Hilol 5-juz"),
        ("BQACAgIAAxkBAAIFMGhhXKiibqxaiEWL1FIt7KySCO73AAKsfQACVbwRS6GXbV38K1zLNgQ", "Tafsiri Hilol 6-juz"),
    ]
    for file_id, caption in files:
        bot.send_document(message.chat.id, file_id, caption=caption)

print("🤖 Bot ishga tushdi... Kutyapman...")
bot.infinity_polling()
