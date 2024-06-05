from discord.ext import commands

class Cats(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def meow(self, ctx):
        await ctx.send("meow")

async def setup(client):
    await client.add_cog(Cats(client))
