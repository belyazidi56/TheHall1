# welcome-bot
# import all necessary commands and libraries
import discord
import asyncio

client = discord.Client()


@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')
    await client.change_presence(game=discord.Game(name='The Hall'))


@client.event
async def on_member_join(member):
    print("Recognised that a member called " + member.name + " joined")
    newUserMessage = """**Welcome to The Hall :house: """ + member.name + """ please make sure to read the rules and enjoy your stay
The Hall is a community based server centred around providing a fun and relaxed environment for its users.
-We have :**
```diff
- Custom Bots , NSFW content , Games , Active Members , Partner and Hypesquad Discord Members , Giveaways , Music , Ranking System  and more...``` """

    await client.change_presence(game=discord.Game(name='The Hall'))
    await client.send_message(member, newUserMessage)
    emb=(discord.Embed(description=':house: |_**Hello '+member.name+' :wave:  Welcome to the Hall, have fun!**_',color=0xff65a6))
    emb.set_author(name="Welcome To The Hall",icon_url="https://cdn.discordapp.com/attachments/466276309501476874/469602792265220096/Hall.jpg")
    emb.set_thumbnail(url=member.avatar_url)
    await client.send_message(discord.Object(id='453679995357888522'),embed=emb)
    print("Sent message to " + member.name)
@client.event
async def on_member_remove(member):
    await client.send_message(discord.Object(id='469630446494416908'), ':negative_squared_cross_mark: |** Goodbye ' + member.name + ' :hand_splayed: we will miss you! **:confused:')
    print("Sent leave message to " + member.name)


client.run('NDY5NjAzMTU3NTA5NjY4ODY0.DjLP6g.AORkb3xerZT3uc1WshPcPz-cDew')
