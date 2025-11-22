import telebot
import os
import datetime

TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.reply_to(message, "ربات Grok Calls فعال شد! 🚀\nبنویس /call یا کال بده")

@bot.message_handler(func=lambda m: True)
def call(message):
    txt = message.text.lower()
    if any(x in txt for x in ['call', 'کال', 'update', 'گم', 'gem']):
        now = datetime.datetime.now().strftime('%H:%M')
        calls = f"""GROK FRESH CALLS — {now}

$ZIGGY (Solana) → MC ~1.2M → +20,000% 24h
CA: FDcjznQLP6KLCgrEPF35PNpFMebmGLDhPji8TCmVdkK8

$HOSICO (Cat meta) → MC ~1.1M
CA: 9pB5v3qN8m2K1jL9xP7zT2rY5uV6wQ8eR4tS3aFpump

$POKE (Sui rotation) → MC ~390K
CA: FmTrnBv3XAJGbddtBa3oC15QGBVt7pnMeKmg52SWzTgq

Ape small • DYOR • NFA 🚀
هر ۵ دقیقه دوباره بزن /call"""
        bot.reply_to(message, calls)
    else:
        bot.reply_to(message, "بنویس /call یا کال بده")

print("ربات روشن شد!")
bot.infinity_polling()
commit
