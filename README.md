# Telegram Bot for DTEK-KEM Electricity Shutdowns

This is a Python-based Telegram bot that retrieves information about electricity shutdowns from the DTEK-KEM website and sends it to users via Telegram.
## Getting Started
1. Clone the repository to your local machine:


```bash
git clone https://github.com/your_username/electricity-shutdowns-bot.git
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

1. Create a bot on Telegram and obtain the bot token.

2. Create a .env file in the project root directory, copy all variables from .env.sample and fill the required fields:

```
BOT_TOKEN= <your-bot_token>
ADMINS= <admin-ids>
```

3. Run the bot:

```bash
python bot.py
```

## Usage
Once the bot is running, you can search for it on Telegram and start a conversation with it. The bot will greet you and provide a list of available commands.

The following commands are available:

```
/start: Start the conversation with the bot.
/help: Show the list of available commands.
/save_address: Save preffered address
/svitlo: Show the electricity shutdowns.
```  


## Contributing
Contributions are welcome! If you have any suggestions or find a bug, please create an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.