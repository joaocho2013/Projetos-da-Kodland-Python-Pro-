from bot_logic import gen_pass
from discord.ext import commands
import discord
# Permissões do bot
intents = discord.Intents.default()
intents.message_content = True
# Criar o bot com prefixo $
bot = commands.Bot(command_prefix="$", intents=intents)
# Evento: quando o bot estiver pronto
@bot.event
async def on_ready():
    print(f"Fizemos login como {bot.user}")
# Comando: hello
@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")
# Comando: bye
@bot.command()
async def bye(ctx):
    await ctx.send("🙂")
# Comando: senha
@bot.command()
async def senha(ctx):
    senha_gerada = gen_pass(10)
    await ctx.send(f"🔐 Sua senha gerada é: {senha_gerada}")

bot.run("seu token")
