from . import *

@icssbot.on(icss_cmd(pattern="السورس"))
async def ica(icss):
    _, check_sgnirts = check_data_base_heal_th()
    await icss.client.send_file(
        icss.chat_id, ICSS_IMG, caption=ics_c
    )
    await icss.delete()

@icssbot.on(icss_cmd(pattern="ping"))
async def ping(e):
    S = datetime.now()
    e = await eor(e, "⌭")
    E = datetime.now()
    Ms = (E - S).microseconds / 1000
    await eor(e, Ping.format(Ms, mention))

         
CMD_HELP.update({"Bot": "{}".format(alv)})
