import logging
from http.client import responses
from traceback import print_tb

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
    user_message = update.message.text.lower()
    if 'привет' in user_message:
        response = "И тебе привет!"
    elif 'как дела' in user_message:
        response = "Отлично! А у тебя?"
    elif 'пока' in user_message:
        response = "До свидания! Жду твоего возвращения"
    else:
        response = f"Вы написали: '{update.message.text}'\nПопробуйте команду /help"

    await update.message.reply_text(response)


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка ошибок"""
    logging.error(f"Ошибка: {context.error}")

def main():
    """Запуск бота"""
    application = Application.builder().token(BOT_TOKEN).build()

    #Обработчики команд
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("about", about_command))

    #Обработчик текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    #Обработчик ошибок
    application.add_error_handler(error_handler)

    print("Бот запущен...")
    application.run_polling()

if __name__ == "__main__":
    main()


