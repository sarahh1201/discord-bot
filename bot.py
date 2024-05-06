import random
import datetime
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix="-", intents=discord.Intents.all())

#Prints message to terminal saying the bot is in use
@client.event
async def on_ready():
    print("Bot In Use")
 
#Prints Hello to the chat   
@client.command()
async def hello(ctx):
    await ctx.send(f"Hello <@{ctx.author.id}>!")

#Send welcome embed
@client.event
async def on_member_join(member):
    channel = client.get_channel() 
    today = datetime.date.today()
    # Create the embed with basic components
    embed = discord.Embed(
        title="Welcome!",
        description=f"Welcome to my server!",
        color=0 # You can change the color
    )
    embed.set_thumbnail(url=" ")
    embed.set_footer(text=f"Date: {today.strftime('%d/%m/%Y')}")

    # Send the embed in the channel where the command was used
    await channel.send(f"Welcome <@{member.id}>!",embed=embed)

#Send leave embed
@client.event
async def on_member_remove(member):
    channel = client.get_channel() 
    today = datetime.date.today()
    # Create the embed with basic components
    embed = discord.Embed(
        title="Farewell",
        description=f"<@{member.id}> has left.",
        color=0 # You can change the color
    )
    embed.set_thumbnail(url=" ")
    embed.set_footer(text=f"Date: {today.strftime('%d/%m/%Y')}")

    # Send the embed in the channel where the command was used
    await channel.send(embed=embed)

#Topic generator 
@client.command()
async def topic(ctx, topic_number: int=None):
    with open('topic.txt') as topic:
        lines = topic.readlines()
        
    topic_count = len(lines)
    
    if topic_count > 0:
        # If a topic number is provided, use it (ensuring it is within range)
        if topic_number is not None and 0 <= topic_number - 1 < topic_count:
            num = topic_number - 1

        else:
            num = random.randrange(0, topic_count) 

        # Create the embed with basic components
        embed = discord.Embed(
            title="Topic Number: " + str(num+1),
            description=lines[num].strip(),
            color=0 # You can change the color
        )

        # Set the footer with text and an icon (optional)
        embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar.url)

        # Set the current timestamp
        embed.timestamp = discord.utils.utcnow()

        # Send the embed in the channel where the command was used
        await ctx.send(embed=embed)
        print("Topic")
    else:
        await ctx.send("Invalid topic number.")
        
@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.channel.id == :
        # Avoid reacting to the bot's own messages
        if message.author == client.user:
            return
        
        # Check if the message is in the specified target channel
        if "cheese" in message.content.lower():
            # Add a reaction (example: thumbs up)
            await message.add_reaction("🧀")
            print("Cheese")

client.run(TOKENKEY)
