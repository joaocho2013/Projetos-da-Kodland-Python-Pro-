import discord
from discord.ext import commands
import os
import uuid

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")


@bot.command()
async def imagem(ctx):

    if not ctx.message.attachments:
        await ctx.send("Você precisa enviar uma imagem junto com o comando")
        return

    attachment = ctx.message.attachments[0]

    if not attachment.content_type or not attachment.content_type.startswith("image/"):
        await ctx.send("O arquivo enviado não é uma imagem")
        return

    os.makedirs("imagens", exist_ok=True)

    extensao = os.path.splitext(attachment.filename)[1]
    nome_unico = f"{uuid.uuid4()}{extensao}"

    caminho = os.path.join("imagens", nome_unico)

    await attachment.save(caminho)

    await ctx.send(f" Imagem salva com sucesso\nNome: `{nome_unico}`")


bot.run("aqui fica o codigo fessora")   
