import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!",intents=intents)


@bot.event
async def on_ready():
    print(f'Bot is up')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)



@bot.tree.command(name="ping", description="command ping")
async def ping(interaction: discord.Integration):
    await interaction.response.send_message("Pong")

from help_command_file import help_command


@bot.tree.command(name="help", description="Commands list")
async def help(interaction: discord.Integration):
    await help_command(interaction)



from music_command_file import music_command


@bot.tree.command(name="music", description="Download youtube mp3 with url")
@app_commands.describe(url="url youtube")
async def music(interaction: discord.Integration, url: str):
    await music_command(interaction, url)




# Run the bot

bot.run("****")
