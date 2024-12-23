from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Функция для обработки команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Привет, {update.effective_user.first_name}! Я твой бот.")

# Создаём приложение с токеном
app = ApplicationBuilder().token("7339994974:AAHb3OL5xR6OOTEZ3DntmyrAU3VW1MXiHGc").build()

# Добавляем обработчик команды /start
app.add_handler(CommandHandler("start", start))

if __name__ == "__main__":
    print("Бот успешно запущен!")  # Логирование
    app.run_polling()  # Правильный отступ
