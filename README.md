# ArbiLearn Telegram Bot

A Telegram bot powered by GPT-4 that provides information about ArbiLearn, a Web3 educational platform. The bot runs alongside a FastAPI web server for health checks and status monitoring.

## Features

- **AI-Powered Responses**: Uses the Alith Agent with GPT-4 to generate informative responses about ArbiLearn
- **Web3 Education**: Provides details about ArbiLearn's features, including the Peeps System, NFT minting, and learning opportunities
- **Web Server Integration**: Includes a FastAPI server for health checks and deployment monitoring
- **Containerization-Ready**: Designed to run in containerized environments like Docker

## Prerequisites

- Python 3.7+
- Telegram Bot Token (from [@BotFather](https://t.me/BotFather))
- Alith API access for GPT-4 integration

## Installation

1. **Clone the repository**

```bash
git clone <repository-url>
cd arbilearn-telegram-bot
```

2. **Create and activate a virtual environment**

```bash
python3 -m venv telegram_bot_env
source telegram_bot_env/bin/activate  # On Windows: telegram_bot_env\Scripts\activate
```

3. **Install the required packages**

```bash
pip install fastapi uvicorn python-telegram-bot alith
```

Or install from requirements.txt:

```bash
pip install -r requirements.txt
```

## Configuration

Set the environment variable for your Telegram Bot Token:

```bash
export TELEGRAM_BOT_TOKEN="your_telegram_bot_token_here"
```

On Windows:
```cmd
set TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
```

You can also specify a custom port for the FastAPI server (default is 8000):
```bash
export PORT=8080
```

## Usage

Start the bot by running:

```bash
python tg-bot.py
```

This will:
- Launch the FastAPI server in a background thread
- Start the Telegram bot in the main thread
- Begin responding to messages from users

## How It Works

1. When a user sends a message to the bot, the `handle_message` function processes it
2. The message is passed to the Alith Agent, which generates a response about ArbiLearn
3. The bot sends the response back to the user

## Project Structure

- `tg-bot.py` - Main application file containing both the Telegram bot and FastAPI server
- `Dockerfile` - Configuration for Docker containerization
- `requirements.txt` - Python dependencies

## API Endpoints

- `GET /` - Returns the status of the bot
- `GET /health` - Health check endpoint for monitoring and deployment platforms

## Deployment

### Docker Deployment

Build and run using Docker:

```bash
docker build -t arbilearn-bot .
docker run -e TELEGRAM_BOT_TOKEN="your_token_here" -p 8000:8000 arbilearn-bot
```

### Cloud Deployment

The bot is designed to work with cloud platforms like Render or Heroku:

1. Set the `TELEGRAM_BOT_TOKEN` environment variable in your deployment platform
2. Deploy the code to your platform of choice
3. The application will automatically use the PORT environment variable if provided

## Troubleshooting

- **Bot not responding**: Verify your `TELEGRAM_BOT_TOKEN` is correct and the bot is running
- **Web server issues**: Check the FastAPI server logs for errors
- **Thread-related errors**: The application has been structured to run the Telegram bot in the main thread to avoid asyncio and signal handler issues

## About ArbiLearn

ArbiLearn is a Web3 educational platform that empowers users to explore blockchain technology, earn rewards, and engage with decentralized learning experiences. It operates on the innovative "Peeps System" allowing users to peep into other ecosystems and earn NFT-based certifications.

For more information, visit [ArbiLearn's official website](https://www.arbilearn.club/).
