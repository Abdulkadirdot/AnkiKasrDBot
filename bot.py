pip install python-telegram-bot

from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

# Function to delete join messages
def delete_join_message(update: Update, context: CallbackContext):
    # Check if the message is a new user joining
    if update.message.new_chat_members:
        # Delete the message with the new join info
        update.message.delete()

# Main function to set up the bot
def main():
    # Replace 'YOUR_API_TOKEN' with the token you got from BotFather
    updater = Updater('7913927976:AAE94-bg05ISGG9r9u0Z-c5rVvlj3qE4kaQ', use_context=True)
    
    dispatcher = updater.dispatcher
    
    # Handler to listen for new members joining
    dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, delete_join_message))
    
    # Start the bot
    updater.start_polling()
    
    # Keeps the bot running
    updater.idle()

if __name__ == '__main__':
    main()
