


from telethon.errors import ChatSendInlineForbiddenError
from telethon.errors.rpcerrorlist import BotMethodInvalidError as bmi

from . import *

REPOMSG = (
    "• **ASTEROID USERBOT** •\n\n",
    "• Repo - [Click Here](https://github.com/TEAMROYAL/Asteroid)\n",
    "• Addons - [Click Here](https://github.com/TEAMROYAL/AsteroidAddons)\n",
    "• Support - @Asteriod_support",
)


@Asteroid_cmd(pattern="repo$")
async def repify(e):
    try:
        q = await Asteriod_bot.inline_query(asst.me.username, "repo")
        await q[0].click(e.chat_id)
        if e.sender_id == Asteriod_bot.uid:
            await e.delete()
    except (ChatSendInlineForbiddenError, bmi):
        await eor(e, REPOMSG)
