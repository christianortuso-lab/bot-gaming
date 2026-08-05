import asyncio
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup

from config import BOT_TOKEN, CHANNEL_ID


async def invia_messaggio(testo, immagine, link):

    bot = Bot(token=BOT_TOKEN)

    tastiera = InlineKeyboardMarkup([
        [InlineKeyboardButton("🛒 Acquista ora", url=link)]
    ])

    await bot.send_photo(
        chat_id=CHANNEL_ID,
        photo=immagine,
        caption=testo,
        parse_mode="HTML",
        reply_markup=tastiera
        
    )


def invia(testo, immagine, link):
    asyncio.run(invia_messaggio(testo, immagine, link))