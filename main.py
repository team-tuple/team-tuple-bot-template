from bot.config import *
import discord
from discord.ext import commands
from tmddn import *
import os

print(tmddn_like(16384))
print(double_tmddn(34123))
intents = discord.Intents.all()
bot = commands.Bot(shard_count=5, command_prefix="!", intents=intents, help_command=None)

if __name__ == '__main__':
    for filename in os.listdir("bot.cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"bot.cogs.{filename[:-3]}")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching))
    print("ready!")


bot.run("token")

일단 템플릿은 넣어두고 
보안이를 시작하죠