# welcome-bot
# import all necessary commands and libraries
import discord
import asyncio

client=discord.Client()

@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')
newUserMessage = "Welcome " + member.name + " To The Hall :house: Server "
@client.event
async def on_member_join(member):
    print("Recognised that a member called " + member.name + " joined")
    await client.send_message(member, newUserMessage)
    print("Sent message to " + member.name)

client.run('NDY5NjAzMTU3NTA5NjY4ODY0.DjLP6g.AORkb3xerZT3uc1WshPcPz-cDew')
