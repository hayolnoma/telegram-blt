import telebot
from telebot import types

TOKEN = "7802345984:AAFAWMa5EFFFt7hK5GHkH3qpZbAcrRjkNIQ"
ADMIN_ID = 7099831932  # O‘zingizni telegram ID’ingiz

bot = telebot.TeleBot(TOKEN)

# /start komandasi
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton("📱 Kontaktni yuborish", request_contact=True)
    markup.add(button)
    
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEFz6RkTy6sTLP7o7jSyIzoWjtxneZJtgACkQEAAladvQoYhWyjaIZb8TQE")
    bot.send_message(message.chat.id,
        "👋 Assalomu alaykum!\n\nBotdan foydalanish uchun quyidagi tugma orqali telefon raqamingizni yuboring:",
        reply_markup=markup
    )

# Kontakt yuborilganda
@bot.message_handler(content_types=['contact'])
def contact_handler(message):
    user = message.contact
    info = (
        f"📥 Yangi foydalanuvchi:\n"
        f"👤 Ismi: {user.first_name}\n"
        f"📞 Tel: {user.phone_number}\n"
        f"🆔 ID: {user.user_id}"
    )
    bot.send_message(ADMIN_ID, info)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🕋 Islomiy kitoblar", "📈 Top 100 kitoblar")
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEFz6ZkTy7bPq0AsL2vh_EcK51fCIvslgACmgADVp29Chw6AB9P1OD6NAQ")
    bot.send_message(message.chat.id, "✅ Rahmat! Endi quyidagi menyudan foydalaning:", reply_markup=markup)

# Islomiy kitoblar menyusi
@bot.message_handler(func=lambda msg: msg.text == "🕋 Islomiy kitoblar")
def islomic_books_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("/tafsiri_hilol", "/jannat_vasfi", "/rizq_baraka")
    markup.add("/istigfor_salovat", "/quron_qalblar", "/baxtli_hayot", "/paygambar_uyida")
    markup.add("🔙 Ortga")
    bot.send_message(message.chat.id, "📚 Islomiy kitoblar ro‘yxati:", reply_markup=markup)

# Top 100 kitoblar menyusi
@bot.message_handler(func=lambda msg: msg.text == "📈 Top 100 kitoblar")
def top100_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("/top100_list", "🔙 Ortga")
    bot.send_message(message.chat.id, "📘 Eng ko‘p o‘qilgan 100 kitob:", reply_markup=markup)

# Fayl komandalar
@bot.message_handler(commands=['tafsiri_hilol'])
def send_tafsir_files(message):
    files = [
        ("BQACAgIAAxkBAAIFLmhhXKdgu11GhgwQ18D9OOViFhGnAAKrfQACVbwRS4MNu7y8ExOsNgQ", "Tafsiri Hilol 1-juz"),
        ("BQACAgIAAxkBAAIFKGhhXKN0cN8EiQkosHXLOWtjqlqsAAKpfQACVbwRS-chZ6AkeVqANgQ", "2-juz"),
        ("BQACAgIAAxkBAAIFKmhhXKUFCars3HsQ2LlQGMSSFoThAAKqfQACVbwRS5D7QRnHad3-NgQ", "3-juz"),
        ("BQACAgIAAxkBAAIFLGhhXKaoMPAhlF29fzGApDliwK3ZAAJlfgACSksQS0WWXCsvjV4lNgQ", "5-juz"),
        ("BQACAgIAAxkBAAIFMGhhXKiibqxaiEWL1FIt7KySCO73AAKsfQACVbwRS6GXbV38K1zLNgQ", "6-juz"),
    ]
    for file_id, caption in files:
        bot.send_document(message.chat.id, file_id, caption=caption)

@bot.message_handler(commands=['jannat_vasfi'])
def send_jannat_vasfi(message):
    bot.send_document(message.chat.id, "BQACAgIAAxkBAAIFMWhhXKj9wSbRXR2PuX87SusD_SfCAAKtfQACVbwRS8s00cjEUqRtNgQ")

@bot.message_handler(commands=['rizq_baraka'])
def send_rizq_baraka(message):
    bot.send_document(message.chat.id, "BQACAgIAAxkBAAIFNGhhXKniA6BE9kc2sNONhhyV5g12AAKufQACVbwRS2atCcvdMikENgQ")

@bot.message_handler(commands=['istigfor_salovat'])
def send_istigfor_salovat(message):
    bot.send_document(message.chat.id, "BQACAgIAAxkBAAIFNmhhXKnfQ0oQ7gNGzz37L7EqfEwAA699AAJVvBFLJKWFdOmmQIk2BA")

@bot.message_handler(commands=['quron_qalblar'])
def send_quron_qalblar(message):
    bot.send_document(message.chat.id, "BQACAgIAAxkBAAIFOGhhXKpAi3TO69fuEt6tXWl8lIBHAAKwfQACVbwRS2KvXGliYx4nNgQ")

@bot.message_handler(commands=['baxtli_hayot'])
def send_baxtli_hayot(message):
    bot.send_document(message.chat.id, "BQACAgIAAxkBAAIFOmhhXKosSVrR28TAn9X6wUnw1P5FAAKxfQACVbwRSyRuVmhuqdYNNgQ")

@bot.message_handler(commands=['paygambar_uyida'])
def send_paygambar_uyida(message):
    bot.send_document(message.chat.id, "BQACAgIAAxkBAAIFPGhhXKt5U4tiyrhANx8o1SRXtXIEAAImdgACKAcRS9ZfB25AzSW0NgQ")

@bot.message_handler(commands=['top100_list'])
def send_top100_txt(message):
    bot.send_document(message.chat.id, "BQACAgIAAxkBAAIFPWhhXKsEZgHTew7T8R19Y8aebBt5AAKyfQACVbwRS4y7Bhr1YAgvNgQ")

# Ortga
@bot.message_handler(func=lambda msg: msg.text == "🔙 Ortga")
def go_back(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🕋 Islomiy kitoblar", "📈 Top 100 kitoblar")
    bot.send_message(message.chat.id, "🔙 Asosiy menyuga qaytdingiz", reply_markup=markup)

# Boshqa xabarlarga javob
@bot.message_handler(func=lambda msg: True)
def fallback(message):
    bot.send_message(message.chat.id, "⚠️ Tugmalar orqali harakat qiling, xo‘jayin.")

print("🤖 Bot ishga tushdi...")
bot.infinity_polling()
