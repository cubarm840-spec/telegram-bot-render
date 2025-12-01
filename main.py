from telegram.ext import Application, CommandHandler
from telegram import InputFile
import os

# Получаем токен из переменных окружения Render
TOKEN = os.environ.get("8140716585:AAEYA18MWOf9IiW5cIUPFzFIGUVIVrQahF4")

async def start(update, context):
    chat_id = update.effective_chat.id
    with open("photo.jpg", "rb") as img:
        await context.bot.send_photo(
            chat_id=chat_id,
            photo=InputFile(img),
            caption="Привет! Это стартовое сообщение с картинкой 🔥"
        )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("Бот запущен на Render!")
    app.run_polling()

if __name__ == "__main__":
    main()

