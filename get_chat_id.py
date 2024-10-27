from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [[InlineKeyboardButton("Get Chat ID", callback_data='get_chat_id')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Get Your Chat ID :', reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    if query.data == 'get_chat_id':
        await query.message.reply_text(f'Your chat ID is: {query.message.chat.id}')

if __name__ == "__main__":
    TOKEN  = input("Please enter your bot token : ") 
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    application.run_polling()
