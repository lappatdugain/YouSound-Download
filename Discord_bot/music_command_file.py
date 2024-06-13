import discord
from pytube_url import url_youtube_mp3
import shutil


async def music_command(interaction: discord.Interaction, url: str):
    try:
        await interaction.response.defer()
        mp3 = url_youtube_mp3(url)
        await interaction.followup.send(file=discord.File(mp3))
        shutil.rmtree('./tmp')
    except Exception as e:
        await interaction.followup.send(f"Error: {e}")
        shutil.rmtree('./tmp')
