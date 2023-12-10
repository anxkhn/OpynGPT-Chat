# OpynGPT Telegram Chat Bot

OpynGPT Telegram Chat Bot is a simple Telegram bot that utilizes the Telebot library and [OpynGPT](https://github.com/anxkhn/OpynGPT) python module for generating natural language responses based on user input.

## Getting Started

### Prerequisites

Before running the bot, ensure that you have the required Python libraries installed:

```bash
pip install telebot opyngpt python-dotenv
```

### Set Up Your Telegram Bot

1. Open Telegram and search for the "BotFather" bot.
2. Start a chat with BotFather and use the `/newbot` command to create a new bot.
3. Follow the instructions to set a name and username for your bot.
4. Once the bot is created, BotFather will provide you with a token. Copy this token.

### Create a .env File

Create a file named `.env` in the same directory as your script. Add the following line to the `.env` file:

```env
TOKEN=your_telegram_bot_token
```

Replace `your_telegram_bot_token` with the actual token you obtained from BotFather.

## Usage

1. Clone this repository or download the `main.py` file.

2. Modify the Python script (`main.py`) to include the environment variable loading for the Telegram bot token:

   ```python
   import os
   from dotenv import load_dotenv

   load_dotenv()
   TOKEN = os.getenv('TOKEN')
   if TOKEN is None:
       raise ValueError("Telegram bot token (TOKEN) not set in environment variables.")
   ```

3. Run your Python script:

   ```bash
   python main.py
   ```

4. Start a conversation with your bot on Telegram by searching for the bot's username, and the bot will respond to your messages using OpynGPT.

## Contributing

If you'd like to contribute to the development of OpynGPT Telegram Chat Bot, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the [GPLv3 License](https://www.gnu.org/licenses/gpl-3.0.html) - check the license file for more information.