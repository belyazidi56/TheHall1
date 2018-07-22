import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

client = discord.Client()

bot = commands.Bot(command_prefix='&')

@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')
    await client.change_presence(game=discord.Game(name='&helpme'))


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
    emb.set_image(url='https://cdn.discordapp.com/attachments/469630446494416908/470419518280302616/giphy.gif')
    emb.set_thumbnail(url=member.avatar_url)
    await client.send_message(discord.Object(id='453679995357888522'),embed=emb)
    print("Sent message to " + member.name)
@client.event
async def on_member_remove(member):
    emb1 = (discord.Embed(description=':negative_squared_cross_mark: |** Goodbye ' + member.name + ' :hand_splayed: we will miss you! **:confused:',color=0xff65a6))
    emb1.set_author(name="GoodBye",icon_url="https://cdn.discordapp.com/attachments/466276309501476874/469602792265220096/Hall.jpg")
    emb1.set_thumbnail(url=member.avatar_url)
    emb1.set_image(url='https://cdn.discordapp.com/attachments/469630446494416908/470417307345223700/JhgS.gif')
    await client.send_message(discord.Object(id='453693951950716939'),embed=emb1)
    print("Sent leave message to " + member.name)

@bot.event
async def on_ready():
    print ("Ready when you are xd")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def Welcome(ctx,user: discord.Member):
    emb3 = (discord.Embed(description='Welcome '+format(user.name)+'',color=0xff65a6))
    emb3.set_thumbnail(url=user.avatar_url)
    emb3.set_image(url='https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif')
    await bot.say(embed=emb3)

@bot.command(pass_context=True)
async def helpme(ctx):
        emb4 = (discord.Embed(description='Help', color=0xff65a6))
        emb4.set_author(name="The Hall",
                        icon_url="https://cdn.discordapp.com/attachments/466276309501476874/469602792265220096/Hall.jpg")
        emb4.add_field(name="**Welcome @[User] :**",value="\nSay Welcome To New Member")
        emb4.add_field(name="**Info @[User]**", value="\nShow Member Information")
        await bot.say(embed=emb4)
@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    emb2 = (discord.Embed(description=''+format(user.name)+' Information :',color=0xff65a6))
    emb2.set_author(name="User Info",icon_url="https://cdn.discordapp.com/attachments/466276309501476874/469602792265220096/Hall.jpg")
    emb2.set_thumbnail(url=user.avatar_url)
    emb2.add_field(name="**Username**", value=format(user.name))
    emb2.add_field(name="**User ID**", value=format(user.id))
    emb2.add_field(name="**User Status**", value=format(user.status))
    emb2.add_field(name="** User_Hightest_Role**", value=format(user.top_role))
    emb2.add_field(name="** User_Joined_At**", value=format(user.joined_at))
    await bot.say(embed=emb2)



bot.run('NDY5NjAzMTU3NTA5NjY4ODY0.DjLP6g.AORkb3xerZT3uc1WshPcPz-cDew')
