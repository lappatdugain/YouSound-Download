import discord


async def help_command(interaction: discord.Interaction):
    try:
        embed = discord.Embed(title=f"Commands list",
                              description="- `/ping` : Use to ping bot"
                                          "\n- `/music` : Download youtube mp3 with url",
                              colour=discord.Colour.yellow())
        await interaction.response.send_message(embed=embed)
    except Exception as e:
        await interaction.response.send_message(f"Error: {e}")
