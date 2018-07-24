import discord
import asyncio
import mysql.connector
from discord.ext import commands

bot = commands.Bot(command_prefix='&')
@bot.event
async def on_ready():
    print('logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-----')
    await bot.change_presence(game=discord.Game(name='Support |DM me'),status=discord.Status.dnd)
@bot.event
async def on_message(message):
            msg = getattr(message.server, 'id', None)
            emb2 = (discord.Embed(color=0xff65a6))
            emb2.set_author(name="Support",
                            icon_url="https://media.discordapp.net/attachments/466276309501476874/470739248920657951/The_hall_support.png?width=480&height=480")
            emb2.add_field(name="**Thanks for the message!**", value="The hall team will get back to you as soon as possible!")
            emb = (discord.Embed(description='**' + format(message.author.name) + ' Have A Problem !**', color=0xff65a6))
            emb.set_author(name="The Problem :",
                            icon_url="https://media.discordapp.net/attachments/466276309501476874/470739248920657951/The_hall_support.png?width=480&height=480")
            emb.set_thumbnail(url=message.author.avatar_url)
            emb.add_field(name="**Question**", value=message.content)
            emb.add_field(name="**User ID**", value=message.author.id)
            if msg !='453672511092293634' :
                await bot.send_message(discord.Object(id='471067480316575744'),embed=emb)
                await bot.send_message(message.author,embed=emb2)
            await bot.process_commands(message)

@bot.command(pass_context=True)
async def send(ctx,user:discord.Member):
    s=ctx.message.content
    s2=s.split(',')[1]
    if ctx.message.channel.id == '471067480316575744':
        emb3 = (discord.Embed(description='**' + format(ctx.message.author.name) + ' Reply !**', color=0xff65a6))
        emb3.set_author(name=ctx.message.author.name,
                        icon_url=ctx.message.author.avatar_url)
        emb3.add_field(name="**Solution**", value=s2)
        await bot.send_message(user,embed=emb3)

bot.run("NDcxMDEyMjM4Njk4ODcyODMy.DjjUiw.BNOzts5B4GvGBTmXCwpqBy2kMAU")
