import random
import discord
from discord.ext import commands
from discord import app_commands

class Topic(commands.Cog, name = "Topics",description="Generate a topic for the chat!"):
    def __init__(self, client):
        self.client = client
    
    def generate_topic_embed(self, user: discord.User,topic_number: int=None) -> discord.Embed:
        with open('topic.txt') as topic_file:
            topics = topic_file.readlines()

        topic_count = len(topics)
        if topic_count > 0:
            if topic_number is not None and 0 <= topic_number - 1 < topic_count:
                num = topic_number - 1

            else:
                num = random.randrange(0, topic_count) 

            # Create the embed with basic components
            embed = discord.Embed(
                title="Topic Number: " + str(num + 1),
                description=topics[num].strip(),
                color=15269838  # You can change the color
            )

            # Set the footer with text and an icon (optional)
            embed.set_footer(text=user.name, icon_url=user.display_avatar.url)

            # Set the current timestamp
            embed.timestamp = discord.utils.utcnow()
            print("Topic")
            return embed
        else:
            raise ValueError("No topics available.")
        
    async def button_callback(self, interaction: discord.Interaction):
        new_embed = self.generate_topic_embed(interaction.user)
        if new_embed:
            view = self.create_view()
            await interaction.response.send_message(embed=new_embed, view=view)
        else:
            await interaction.response.send_message("No topics available.")

    def create_view(self):
        button = discord.ui.Button(label="New Topic", style=discord.ButtonStyle.gray)
        button.callback = self.button_callback
        view = discord.ui.View()
        view.add_item(button)
        return view

    @app_commands.command(name="topic", description="Send a topic to the chat")
    @app_commands.guilds(discord.Object(id=785847181080526858))
    async def slash_topic(self, interaction: discord.Interaction, topic_number: int=None):
        embed=self.generate_topic_embed(interaction.user,topic_number)
        view = self.create_view() 

        # Send the embed in the channel where the command was used
        await interaction.response.send_message(embed=embed,view=view)
        
    @commands.command()
    async def topic(self, ctx, topic_number: int=None):
        embed=self.generate_topic_embed(ctx.author,topic_number)
        view = self.create_view() 
            
        # Send the embed in the channel where the command was used
        await ctx.send(embed=embed,view=view)

async def setup(client):
    await client.add_cog(Topic(client))
