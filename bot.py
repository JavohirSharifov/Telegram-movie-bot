from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Insert your bot token directly here
BOT_TOKEN = "7522348429:AAFI6DVMFtnuekHUF-YbOnyUWdSPzvM6miU"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! How are you? How can I help you?")

if __name__ == "__main__":
    # Pass the token directly to the ApplicationBuilder
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()