import asyncio
from telegram_bot import Bot

TOKEN = "8916046424:AAFBbqOb_E1LB_b0JfBVwPFRwYpNphNXVR0"
CANALE = "@GamingScontiItalia"

async def main():
    bot = Bot(TOKEN)

    msg = await bot.send_message(
        chat_id=CANALE,
        text="Test connessione!"
    )

    print(f"Funziona! ID chat: {msg.chat_id}")

asyncio.run(main())