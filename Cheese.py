import random
import discord
from discord.ext import commands
from discord import app_commands

class Cheese(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @app_commands.command(name="cheese", description="Send a cheese gif")
    @app_commands.guilds(discord.Object(id=785847181080526858))
    async def slash_cheese(self, interaction: discord.Interaction):
        with open('cheese.txt') as c:
            cheese = c.readlines()
             
        cheese_count = len(cheese)
        num = random.randrange(0, cheese_count)
        await interaction.response.send_message(cheese[num].strip())
        
    @commands.command()
    async def cheese(self, ctx):
        with open('cheese.txt') as c:
            cheese = c.readlines()
             
        cheese_count = len(cheese)
        num = random.randrange(0, cheese_count)
        await ctx.send(cheese[num].strip())
        print("Cheese Gif")
        
    @commands.Cog.listener()
    async def on_message(self, message):
        #await self.client.process_commands(message)
        
        if message.channel.id == 804497117020160010:
            # Avoid reacting to the bot's own messages
            if message.author == self.client.user:
                return
            
            # Check if the message is in the specified target channel
            if "cheese" in message.content.lower():
                # Add a reaction (example: thumbs up)
                await message.add_reaction("🧀")
                print("Cheese")      

async def setup(client):
    await client.add_cog(Cheese(client))