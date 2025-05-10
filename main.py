import telebot
from telebot import types
import os
from dotenv import load_dotenv
from keep_alive import keep_alive
keep_alive()

load_dotenv()

TOKEN = token=os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('English', callback_data='english')
    btn2 = types.InlineKeyboardButton('Russian', callback_data='russian')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Let's get started! Choose the language:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.data == 'english':
        bot.send_message(call.message.chat.id, 'Welcome to your personal <b><em>fitness assistant</em></b>!💪\n\nThis bot will help you quickly find the technique for the exercise you need🏋\nSo you won’t have to waste time looking for videos anymore🕓', parse_mode='HTML')
        bot.send_message(call.message.chat.id, 'Select a muscle group to get exercise options for it, or enter the name of the exercise you’re interested in👇')
    elif call.data == 'russian':
        bot.send_message(call.message.chat.id, 'Добро пожаловать к твоему личному <b><em>фитнес-помощнику</em></b>!💪\n\nЭтот бот поможет тебе быстро найти технику нужного упражнения🏋\nTак что тебе больше не придётся тратить время на поиск видео🕓', parse_mode='HTML')
        bot.send_message(call.message.chat.id, 'Выберите группу мышц, чтобы получить варианты упражнений на неё, или введите название интересующего вас упражнения👇')

bot.polling(non_stop=True)
