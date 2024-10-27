# Project Title

## Description
A brief description of your project goes here. Explain what it does, its purpose, and any important features.

## Features

- **Keylogger**: Captures and sends keystrokes to a specified Telegram chat.
- **Chat ID Retrieval**: Provides an easy way to get your chat ID using inline buttons.


## Installation

# Clone the repository

```bash

git clone https://github.com/HexShad0w/hexa_KeyLogger.git
```
# Navigate into the project directory

```bash

cd hexa_KeyLogger

```

## Install dependencies

```bash

pip install python-telegram-bot pynput

```


## Usage 

** Get your Chat ID :**

```bash

python3 get_chat_id.py
```
Start your bot and you will get your chat ID

** Start the KeyLogger : **

Make sure to edit the code -> **Your_telegram_token** & **Chat_id**

```bash
python keylogger_bot.py
```
Once the bot is running, you can start a chat with it on Telegram and use the following commands:

```bash
/start: Initializes the bot and provides usage instructions.
/key_logger: Starts the keylogger to capture keystrokes.
/exit: Stops the keylogger and shuts down the bot.

```

