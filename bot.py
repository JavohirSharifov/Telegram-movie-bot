import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Function to handle the "/start" command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello! How are you? How can I help you? I'm ready to assist you with anything you want on Telegram.")

# Main function to run the bot
def main():
    # Get the bot token from environment variables
    TOKEN = os.getenv("7522348429:AAE39Kw9yMSZP4XYgcEfNeunzBP04w8ylTs")
    if not TOKEN:
        print("Error: 7522348429:AAE39Kw9yMSZP4XYgcEfNeunzBP04w8ylTs is not set in environment variables.")
        return
    
    # Initialize the bot application
    application = ApplicationBuilder().token(TOKEN).build()

    # Add the "/start" command handler
    application.add_handler(CommandHandler("start", start))

    # Start the bot
    print("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()