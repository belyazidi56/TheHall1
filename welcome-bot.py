import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
bot = commands.Bot(command_prefix='&')
bot.remove_command('help')
demsg=[
    'fuck',
    'nigga',
    'hentai',
    'nigger',
    'niga',
    'nussy',
    'boobs',
    'boob',
    'dirt',
    'shit'
]


@bot.command(pass_context=True)
async def welcome(ctx, user: discord.Member):
    emb3 = (discord.Embed(description='Welcome ' + format(user.name) + '', color=0xff65a6))
    emb3.set_thumbnail(url=user.avatar_url)
    emb3.set_image(url='https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif')
    await bot.say(embed=emb3)


@bot.command(pass_context=True)
async def help(ctx):
    emb4 = (discord.Embed(description='Help', color=0xff65a6))
    emb4.set_author(name="The Hall",
                    icon_url="https://media.discordapp.net/attachments/466276309501476874/470739164392980490/Hall_Normal.png?width=480&height=480")
    emb4.add_field(name="**welcome @[User] :**", value="Say Welcome To New Member", inline=False)
    emb4.add_field(name="\n**Info @[User]**", value="Show Member Information", inline=False)
    emb4.add_field(name="\n**iamnsfw**", value="Earn NSFW Role", inline=False)
    await bot.say(embed=emb4)


@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    emb2 = (discord.Embed(description='' + format(user.name) + ' Information :', color=0xff65a6))
    emb2.set_author(name="User Info",
                    icon_url="https://media.discordapp.net/attachments/466276309501476874/470739164392980490/Hall_Normal.png?width=480&height=480")
    emb2.set_thumbnail(url=user.avatar_url)
    emb2.add_field(name="**Username**", value=format(user.name))
    emb2.add_field(name="**User ID**", value=format(user.id))
    emb2.add_field(name="**User Status**", value=format(user.status))
    emb2.add_field(name="** User_Hightest_Role**", value=format(user.top_role))
    emb2.add_field(name="** User_Joined_At**", value=format(user.joined_at))
    await bot.say(embed=emb2)

@bot.event
async def on_ready():
    print('logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-----')
    await bot.change_presence(game=discord.Game(name='The Hall |&help'))
@bot.event
async def on_member_join(member):
    print("Recognised that a member called " + member.name + " joined")
    newUserMessage = """**Welcome to The Hall :house: """ + member.name + """ please make sure to read the rules and enjoy your stay
The Hall is a community based server centred around providing a fun and relaxed environment for its users.
-We have :**
```diff
- Custom Bots , NSFW content , Games , Active Members , Partner and Hypesquad Discord Members , Giveaways , Music , Ranking System  and more...``` """

    await bot.send_message(member, newUserMessage)
    emb=(discord.Embed(description=':house: |_**Hello '+member.name+' :wave:  Welcome to the Hall, have fun!**_',color=0xff65a6))
    emb.set_author(name="Welcome To The Hall",icon_url="https://media.discordapp.net/attachments/466276309501476874/470739164392980490/Hall_Normal.png?width=480&height=480")
    emb.set_image(url='https://cdn.discordapp.com/attachments/469630446494416908/470419518280302616/giphy.gif')
    emb.set_thumbnail(url=member.avatar_url)
    await bot.send_message(discord.Object(id='453679995357888522'),embed=emb)
    print("Sent message to " + member.name)
@bot.listen()
async def on_message(message):
    content = message.content.lower()
    for word in demsg:
        if word in content:
            await bot.delete_message(message)
            await bot.send_message(message.channel,"**Hey "+message.author.name+"!** You're not allowed to use that word here! Please Do not Use It Again! :open_mouth:")
            break
    await bot.process_commands(message)


@bot.event
async def on_message(message):
    emb6 = (discord.Embed(description=' NSFW Role Request !', color=0xff65a6))
    emb6.set_author(name="Role Request",
                    icon_url="https://media.discordapp.net/attachments/466276309501476874/470739164392980490/Hall_Normal.png?width=480&height=480")
    emb6.set_thumbnail(url=message.author.avatar_url)
    emb6.add_field(name="**:white_check_mark: Success "+message.author.name+" | Role Earned**", value='_'+message.author.id+'_')

    emb7 = (discord.Embed(description='NSFW Role Request ! ', color=0xff65a6))
    emb7.set_author(name="Role Request ",
                    icon_url="https://media.discordapp.net/attachments/466276309501476874/470739164392980490/Hall_Normal.png?width=480&height=480")
    emb7.set_thumbnail(url=message.author.avatar_url)
    emb7.add_field(name="**:question:ERROR | You already have nsfw role. :open_mouth:**", value=message.author.id)
    if message.content.startswith("&iamnsfw"):
            role = discord.utils.get(message.server.roles, name='nsfw')
            if role in message.author.roles:
                await bot.send_message(message.channel, embed=emb7)
            else:
                    try:
                        await bot.add_roles(message.author, role)
                        await bot.send_message(message.channel, embed=emb6)
                    except discord.Forbidden:
                        return
    await bot.process_commands(message)
    @bot.event
    async def on_member_remove(member):
        emb1 = (discord.Embed(description=':negative_squared_cross_mark: |** Goodbye ' + member.name + ' :hand_splayed: we will miss you! **:confused:',color=0xff65a6))
        emb1.set_author(name="GoodBye",icon_url="https://media.discordapp.net/attachments/466276309501476874/470739164392980490/Hall_Normal.png?width=480&height=480")
        emb1.set_thumbnail(url=member.avatar_url)
        emb1.set_image(url='https://cdn.discordapp.com/attachments/469630446494416908/470417307345223700/JhgS.gif')
        await bot.send_message(discord.Object(id='453693951950716939'),embed=emb1)
        print("Sent leave message to " + member.name)



bot.run('NDcwNDI4NDI0MjMwNjY2MjQw.DjbuJw.MlPrz-XrKiaZpLQpDKjsJPOXwqA')
