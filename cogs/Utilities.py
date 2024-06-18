import discord
from discord.ext import commands
from discord import app_commands

class Utilities(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @app_commands.command(name="clear", description="Clear intros from people who have left")
    @app_commands.guilds(discord.Object(id=785847181080526858))
    async def clear(self,interaction: discord.Interaction):
        if interaction.channel.id == :
            async for message in interaction.channel.history(limit=100):
                if not interaction.guild.get_member(message.author.id):
                    await message.delete()  
            await interaction.response.send_message("Messages from users not in the server have been cleared.", delete_after=5)
        else:
            await interaction.response.send_message("This command can only be used in a specific channel.", delete_after=5)

    @app_commands.command(name="weather", description="Find out the weather of a city!")
    @app_commands.guilds(discord.Object(id=785847181080526858))
    async def weather(self,interaction: discord.Interaction, city: str, temp_units:str=None):  
            api_key = 'YOUR API KEY' # API key from weatherapi.com
        url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}"
        response = requests.get(url)
        weather_data = response.json()

        location = weather_data['location']
        current = weather_data['current']
        forecast = weather_data['forecast']['forecastday'][0]['day']

        # Temperature conversion
        if temp_units == 'k':
            temp = f"\nTemperature: {current['temp_c'] + 273.15:.2f} K \nFeels Like:: {current['feelslike_f']+273.15:.2f} K \nHigh: {forecast['maxtemp_c']+273.15:.2f} K \nLow: {forecast['mintemp_c']+273.15:.2f} K\n"
            wind = f"Wind: {current['wind_kph']} kph"
            precip = f"Precipitation: {current['precip_mm']} mm \nHumidity: {current['humidity']}%"
        elif temp_units == 'i' or temp_units == 'f':
            temp = f"\nTemperature: {current['temp_f']}°F \nFeels Like:: {current['feelslike_f']}°F \nHigh: {forecast['maxtemp_f']}°F \nLow: {forecast['mintemp_f']}°F\n"
            wind = f"Wind: {current['wind_mph']} mph"
            precip = f"Precipitation: {current['precip_in']} in \nHumidity: {current['humidity']}%"
        else:  # default to metric
            temp = f"\nTemperature: {current['temp_c']}°C \nFeels Like: {current['feelslike_c']}°C \nHigh: {forecast['maxtemp_c']}°C \nLow: {forecast['mintemp_c']}°C\n"
            wind = f"Wind: {current['wind_kph']} kph"
            precip = f"Precipitation: {current['precip_mm']} mm \nHumidity: {current['humidity']}%"
                
        loc = f"{location['name']}"
        loc_reg = f"{location['country']} - {location['region']}"
        cond = f"{current['condition']['text']}"
        update = f"\nLast updated: {current['last_updated']}\n"
        icon = f"http:{current['condition']['icon']}"
        
        embed = discord.Embed(
            title=f"{loc}",
            description=(f"{cond}\n--{temp}--\n{precip}\n{wind}"),
            color=16777215  # You can change the color
        )
        embed.timestamp = discord.utils.utcnow()
        embed.set_thumbnail(url=icon)
        embed.set_footer(text=update)
        embed.set_author(name=loc_reg)
        await interaction.response.send_message(embed=embed)

async def setup(client):
    await client.add_cog(Utilities(client))
