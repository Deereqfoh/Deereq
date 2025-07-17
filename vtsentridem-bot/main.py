from telegram import Poll
from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = "ТВОЯ_ТОКЕН_СТРОКА"
GROUP_CHAT_ID = -1002704974185  # твоя група

async def start_poll(update, context):
    await context.bot.send_poll(
        chat_id=GROUP_CHAT_ID,
        question="Ідемо в центр?",
        options=["Так", "Ні"],
        is_anonymous=False
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("poll", start_poll))

app.run_polling()
