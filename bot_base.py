import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

BOT_TOKEN = "8403795604:AAFoJQqadN0vu89vbCLPpRtIvYOeyi66fH0"

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка команды /start"""
    user = update.message.from_user
    await update.message.reply_text(
        f"Привет, {user.first_name}! \n"
        f"Я простой бот. Отправь мне любое сообщение!"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обрабатывает команду /help"""
    help_text = """
    Доступные команды:
    /start - начать работу
    /help - получить помощь
    /about - о боте
    
    Просто напиши мне что-нибудь, и я отвечу!
    """
    await update.message.reply_text(help_text)

async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка команды /about"""
    await update.message.reply_text(
        "Это простой учебный бот \n"
        "Создан для демонстрации возможностей Python Telegram Bot API"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка текстовых сообщений"""
    user