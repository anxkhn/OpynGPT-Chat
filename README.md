# OpynGPT Telegram Chat Bot

![Presentation1](https://github.com/anxkhn/OpynGPT-Chat/assets/83116240/b1e4b6a6-c9e6-4a33-9388-644d337bac12)

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

### Clone the OpynGPT-Chat Repository

1. Open a terminal window.

2. Clone the OpynGPT-Chat repository:

   ```bash
   git clone https://github.com/anxkhn/OpynGPT-Chat.git
   ```

3. Navigate to the cloned directory:

   ```bash
   cd OpynGPT-Chat
   ```

### Create a .env File

Create a file named `.env` in the same directory as your script. Add the following line to the `.env` file:

```env
TOKEN=your_telegram_bot_token
```

Replace `your_telegram_bot_token` with the actual token you obtained from BotFather.

## Usage

1. Run the Python script:

   ```bash
   python bot_script.py
   ```

2. Start a conversation with your bot on Telegram by searching for the bot's username, and the bot will respond to your messages using OpynGPT.

## Testing Live Bot

You can checkout the live OpynGPT Telegram Chat Bot by accessing [@OpynGPT_Chatbot](https://t.me/OpynGPT_Chatbot) on Telegram. Send messages to the bot, and it will respond using OpynGPT.

## Contributing

If you'd like to contribute to the development of OpynGPT Telegram Chat Bot, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the [GPLv3 License](https://www.gnu.org/licenses/gpl-3.0.html) - check the license file for more information.
