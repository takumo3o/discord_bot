import discord
from datetime import datetime, timedelta

#Botのアクセストークン
TOKEN = 'ODk4Mzg1Mzg1MTAzNzA0MTE1.YWjclw.MLGF55zstEdtgG1x5EIjNt_vI_E'

#discordサーバ内情報
SERVER_id = '703257945814859866'
alert_channel_id = '703998330937540670'
voice_channel_id = '703259498445406330'

#接続に必要なオブジェクトを生成
client = discord.Client()

#起動時に動作する処理
@client.event
async def on_ready():
    print('ログインしました')

#時間になったら通知する処理
#@client.event
#async def 

#指定ボイスチャンネル入室時に実行する処理（イベントハンドラ）
@client.event
async def on_voice_state_update(member, before, after):
    #if member.guild.id == SERVER_id and (before.channel != after.channel):
    if member.guild.id == SERVER_id and (voice_channel_id):
        now = datetime.utcnow() + timedelta(hours=9)
        alert_channel = client.get_channel(alert_channel_id)
        if before.channel is None: 
            msg = f'{now:%m/%d-%H:%M} に {member.name} が {voice_channel_id.channel.name} に参加しました。'
            await alert_channel.send(msg)

#Botの起動とDiscordサーバへの接続
client.run(TOKEN)