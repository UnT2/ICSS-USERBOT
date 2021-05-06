from . import *

@icssbot.on(
    icss_cmd(
    outgoing=True, 
    pattern="سورس$"
    )
)
@icssbot.on(
    sudo_cmd(pattern="سورس$", allow_sudo=True)
)
async def ica(icss):
    ics_id = await reply_id(icss)
    await icss.client.send_file(
        icss.chat_id, ICSS_IMG, caption=ics_c, reply_to=ics_id
    )
    await icss.delete()
         
CMD_HELP.update({"alive": "{}".format(alv)})
