import os
import threading
import asyncio
from fastapi import FastAPI
import uvicorn
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackContext,
)
from alith import Agent

# Initialize Alith Agent
agent = Agent(
    name="ArbiLearn Bot Agent",
    model="gpt-4",
    preamble="""You are ArbiLearn Bot, an AI assistant designed exclusively to provide information about ArbiLearn, a Web3 educational platform that empowers users to explore blockchain technology, earn rewards, and engage with decentralized learning experiences. 
ArbiLearn operates on an innovative **"Peeps System"**, allowing users to **peep into other ecosystems**, participate in learning challenges, and earn NFT-based certifications. By completing courses and engaging in activities, users gain valuable insights and rewards while contributing to the Web3 community.

Key Features of ArbiLearn:
- Learn & Earn: Users can participate in structured blockchain education programs and earn NFT certificates as proof of participation.  
- Peeps System: Explore and interact with various Web3 ecosystems, gaining exposure to different blockchain networks and earning incentives.  
- NFT Minting: Users can mint NFTs to verify their participation and achievements in ArbiLearn activities.  
- Community Engagement: Connect with a growing network of learners, developers, and blockchain enthusiasts.  
- Ecosystem Rewards: Engage with different blockchain ecosystems and earn exclusive NFT rewards for your participation.  

### How to Get Involved:
- Visit the official website: https://www.arbilearn.club/
- Start learning and mint NFTs via the https://www.arbilearn.club/pages/app
- Explore different Web3 ecosystems through the Peeps System

If a question is outside ArbiLearn's scope, politely redirect the user to the official website for more information."""
)

# Create FastAPI app
app = FastAPI()

@app.get("/")
async def root():
    return {"status": "Bot is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Initialize Telegram Bot
bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
telegram_app = Application.builder().token(bot_token).build()

# Define message handler
async def handle_message(update: Update, context: CallbackContext) -> None:
    # Use the agent to generate a response
    response = agent.prompt(update.message.text)
    # Send the reply back to the Telegram chat
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

# Add handlers to the application
telegram_app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

# Function to run FastAPI server
def run_fastapi_server():
    # Get PORT from environment variable for Render compatibility
    port = int(os.getenv("PORT", 8000))
    
    # Start FastAPI server
    uvicorn.run(app, host="0.0.0.0", port=port)

# Main function to start both web server and telegram bot
if __name__ == "__main__":
    # Start FastAPI server in a separate thread
    threading.Thread(target=run_fastapi_server, daemon=True).start()
    
    # Run telegram bot in the main thread
    telegram_app.run_polling()
 