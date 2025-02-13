from asyncio import sleep
from userbot.events import register
from userbot.cmdhelp import CmdHelp
from userbot import SILGI_VERSION

@register(outgoing=True, pattern=r"^\.globalspam$")
async def silgi(event):
    chat = "@spambot"
    
    await event.edit("🚀 **Spam bot ilə əlaqə qurulur...**")
    
    async with event.client.conversation(chat) as conv:
        await conv.send_message("/start")
        await conv.get_response()

        await conv.send_message("This is a mistake")
        await conv.get_response()

        await conv.send_message("Yes")
        await conv.get_response()

        await conv.send_message("No! Never did that!")
        await conv.get_response()

        await conv.send_message("Someone report me but I have not any wrong limited why account")
        await conv.get_response()
    await sleep(4)
    await event.edit("✅ **Global Spam müraciəti tamamlandı!**\n⏳ **1 - 2 saat ərzində global spam açılacaq.**")

CmdHelp("globalspam").add_command(
    "globalspam", None, "@SpamBot-a avtomatik müraciət göndərir."
).add_info(
    "Hesabınızın limitini qaldırmaq üçün avtomatik mesajlar göndərir."
).add_info(
    "[SILGI](@hvseyn) tərəfindən hazırlanmışdır."
).add()
