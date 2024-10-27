# Hexa Keylogger

## Description

Hexa Keylogger is a Python-based application that captures keystrokes using the `pynput` library and sends them to a specified Telegram chat via the Telegram Bot API. The bot includes command handlers to start and stop the keylogger, allowing for basic interaction through Telegram messages.

## Features

- **Keylogger**: Captures and sends keystrokes to a specified Telegram chat.
- **Chat ID Retrieval**: Provides an easy way to get your chat ID using inline buttons.


## Installation

## Clone the repository

```bash

git clone https://github.com/HexShad0w/hexa_KeyLogger.git
```
## Navigate into the project directory

```bash

cd hexa_KeyLogger

```

## Install dependencies

```bash

pip install python-telegram-bot pynput

```


## Usage 

**1. Get your Chat ID :** 

```bash

python3 get_chat_id.py
```
Start your bot and you will get your chat ID

**2. Start the KeyLogger :**

Make sure to edit the code -> **Your_Telegram_Token** and **Your_Chat_ID**

```bash
python keylogger_bot.py
```
Once the bot is running, you can start a chat with it on Telegram and use the following commands:

```bash
/start: Initializes the bot and provides usage instructions.
/key_logger: Starts the keylogger to capture keystrokes.
/exit: Stops the keylogger and shuts down the bot.
```

