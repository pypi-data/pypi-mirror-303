import os
from pyrogram import Client
from Geez import bot1, bot

async def fake_log():
    botlog_chat_id = os.environ.get('BOTLOG_CHATID1')
    if botlog_chat_id:
        return
    
    await bot1.start()
    group_name = 'GeezPyro BotLog'
    group_description = "GeezPyro BotLog"
    group_description = 'Grup botlog berhasil dibuat, mohon jangan keluar jadi group ini\n\n Geez Pyro'
    group = await bot1.create_supergroup(group_name, group_description)
    with open('.env', 'a') as env_file:
        env_file.write(f'\nBOTLOG_CHATID1={group.id}')

    message_text = 'Grouplog berhasil diaktifkan,\nmohon masukkan bot anda ke group ini!'
    await bot1.send_message(group.id, message_text)
    await bot1.stop()


async def izzy_meira(client: bot):
    group_name = "GeezPyro BotLog"
    async for dialog in client.get_dialogs():
        if dialog.chat.title == group_name:
            return dialog.chat
    return None

async def geezlog(client):
    group_name = "GeezPyro BotLog"
    group_description = "GeezPyro BotLog"
    group_message = 'Grup botlog berhasil dibuat, mohon jangan keluar jadi group ini\n\n Geez Pyro'
    group = await izzy_meira(client)
    if group == 0:
        await client.create_supergroup(group_name, group_description)
        await client.send_message(group.id, group_message)
        return group
    return None