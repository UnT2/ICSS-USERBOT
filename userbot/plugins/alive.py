from . import *

@icssbot.on(icss_cmd(pattern="السورس"))
async def ica(icss):
    await icss.client.send_file(
        icss.chat_id, ICSS_IMG, caption=ics_c
    )
    await icss.delete()
         
CMD_HELP.update({"alive": "{}".format(alv)})
