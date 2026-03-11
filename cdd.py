from discord.ext import commands
import discord
import os
import random
import requests

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents) 

@bot.event
async def on_ready():
    print(f"Fizemos login como {bot.user}")
    
@bot.command()
async def info(ctx):
    embed = discord.Embed(
        title="UrsoVesgo",
        description="Vou te ajudar a como deixar o mundo melhor! :D",
        color=discord.Color.green()
    )

    embed.add_field(
        name="🍀 Comandos:",
        value="!hello\n!info\n!agro",
        inline=False
    )

    embed.set_footer(text="Aproveite! ^^")
    await ctx.send(embed=embed)


@bot.command()
async def hello(ctx):
    await ctx.send("Opa! Sou o UrsoVesgo, posso te ajudar a manter o mundo saudável de uma maneira legal :D")


@bot.command()
async def meme(ctx):
    img_image = random.choice(os.listdir('memes'))

    with open(f'memes/{img_image}', 'rb') as f:
        picture = discord.File(f)

    await ctx.send(file=picture)


bot.run("MTQ3ODg4ODQ5MDI0NTgyMDYwOQ.GFxaUT.sE-thpBL2wTwEIAq69sPs0nfwYezP8xSc9MoNY")
