import discord
from discord.ext import commands
from discord import app_commands
    
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="-", intents=discord.Intents.all())

async def load_cogs():
    extensions=["cogs.Cats", "cogs.Greetings", "cogs.Cheese", "cogs.Topics","cogs.Utilities"]
    for extension in extensions: 
        try:
            await client.load_extension(extension)
            print(f'Loaded extention {extension}')
        except Exception as e:
            print(f'Failed to load extention {extension}')
            print(e)
 
@client.event
async def on_ready():
    await load_cogs()
    print("\n")
    await client.tree.sync(guild=discord.Object(id=785847181080526858)) #Syncs the slash commands created in the tree
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name = 'you'))
    print(f'Logged in as {"essences"} ({1235064927417270363})')
    print('------')

@client.tree.command( # The start of the slash command
    name="ping", # Name of the command
    description="Ping the bot", # Description of it
    guild=discord.Object(id=785847181080526858) # States the guild to register it with
    )
async def ping(ctx): # Creates the function for the command
    await ctx.response.send_message(f"Ping {client.latency}") # this just returns the latencey of how long it took the bot to respond, just what the command I made does

client.run(TOKENKEY)
