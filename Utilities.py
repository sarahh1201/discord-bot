import discord
from discord.ext import commands
from discord import app_commands

class Utilities(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @app_commands.command(name="clear", description="Clear intros from people who have left")
    @app_commands.guilds(discord.Object(id=785847181080526858))
    async def clear(self,interaction: discord.Interaction):
        if interaction.channel.id == 936772660636033095:
            async for message in interaction.channel.history(limit=100):
                if not interaction.guild.get_member(message.author.id):
                    await message.delete()  
            await interaction.response.send_message("Messages from users not in the server have been cleared.", delete_after=5)
        else:
            await interaction.response.send_message("This command can only be used in a specific channel.", delete_after=5)
            

async def setup(client):
    await client.add_cog(Utilities(client))