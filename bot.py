from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Insert your bot token here
BOT_TOKEN = "7522348429:AAFI6DVMFtnuekHUF-YbOnyUWdSPzvM6miU"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello my name is Javohir, how can I help you?")

async def reply_nothing_found(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Nothing found")

if __name__ == "__main__":
    # Set up the application with the bot token
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Add handlers for the start command and all other messages
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_nothing_found))

    # Run the bot
    application.run_polling()