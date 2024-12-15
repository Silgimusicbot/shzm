from bot import bot
from pyrogram import filters


@bot.on_message(
    filters.command("start")
)
async def alive(_, message):
    await message.reply(
        f"Salam {message.from_user.mention}, Bu, Silgi tərəfindən hazırlanmış Shazam Telegram Botudur.\n\nℹ️ Siz mənə audio, video və ya səsli qeyd göndərə bilərsiniz ki, Shazam-da təhlil edib nəticələri sizə göndərim.."
    )