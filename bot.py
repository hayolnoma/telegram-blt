import telebot
from telebot import types

TOKEN = '7802345984:AAFAWMa5EFFFt7hK5GHkH3qpZbAcrRjkNIQ'
ADMIN_ID = 7099831932
bot = telebot.TeleBot(TOKEN)

# Start
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("📱 Kontaktni yuborish", request_contact=True)
    markup.add(btn)
    bot.send_message(message.chat.id,
        "👋 Assalomu alaykum!\nBotdan foydalanish uchun kontaktingizni yuboring:",
        reply_markup=markup)

# Contact
@bot.message_handler(content_types=['contact'])
def contact_handler(message):
    user = message.contact
    info = (
        f"📥 Yangi foydalanuvchi:\n"
        f"👤 Ism: {user.first_name}\n"
        f"📞 Tel: {user.phone_number}\n"
        f"🆔 ID: {user.user_id}"
    )
    bot.send_message(ADMIN_ID, info)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🕋 Islomiy kitoblar", "📈 Top 100 kitoblar")
    bot.send_message(message.chat.id, "✅ Rahmat! Kategoriyani tanlang:", reply_markup=markup)

# Islomiy kitoblar tugmasi
@bot.message_handler(func=lambda m: m.text == "🕋 Islomiy kitoblar")
def islomic_books_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("/tafsir", "/jannat", "/rizq", "/baxtli", "/paygambar", "/quron")
    markup.add("🔙 Ortga")
    bot.send_message(message.chat.id, "🕌 Islomiy kitoblardan birini tanlang:", reply_markup=markup)

# Top 100 kitoblar tugmasi
@bot.message_handler(func=lambda m: m.text == "📈 Top 100 kitoblar")
def top100_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("/top100")
    markup.add("🔙 Ortga")
    bot.send_message(message.chat.id, "📊 Tanlang:", reply_markup=markup)

# Ortga
@bot.message_handler(func=lambda m: m.text == "🔙 Ortga")
def go_back(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🕋 Islomiy kitoblar", "📈 Top 100 kitoblar")
    bot.send_message(message.chat.id, "🔙 Asosiy menyuga qaytdik.", reply_markup=markup)

# Hujjatlarni yuborish
@bot.message_handler(commands=['tafsir'])
def send_tafsir(message):
    with open("files/tafsir_1_juz.pdf", "rb") as f:
        bot.send_document(message.chat.id, f)

@bot.message_handler(commands=['jannat'])
def send_jannat(message):
    with open("files/jannat_vasfi.pdf", "rb") as f:
        bot.send_document(message.chat.id, f)

@bot.message_handler(commands=['rizq'])
def send_rizq(message):
    with open("files/rizq_baraka.pdf", "rb") as f:
        bot.send_document(message.chat.id, f)

@bot.message_handler(commands=['baxtli'])
def send_baxtli(message):
    with open("files/baxtli_hayot.pdf", "rb") as f:
        bot.send_document(message.chat.id, f)

@bot.message_handler(commands=['paygambar'])
def send_paygambar(message):
    with open("files/paygambar_uyida.pdf", "rb") as f:
        bot.send_document(message.chat.id, f)

@bot.message_handler(commands=['quron'])
def send_quron(message):
    with open("files/quron_qalblar.pdf", "rb") as f:
        bot.send_document(message.chat.id, f)

@bot.message_handler(commands=['top100'])
def send_top100(message):
    with open("files/top100.txt", "rb") as f:
        bot.send_document(message.chat.id, f)

# Fallback
@bot.message_handler(func=lambda message: True)
def fallback(message):
    bot.send_message(message.chat.id, "Iltimos, menyudan foydalaning.")

print("🤖 Bot ishga tushdi... kutyapman.")
bot.infinity_polling()
