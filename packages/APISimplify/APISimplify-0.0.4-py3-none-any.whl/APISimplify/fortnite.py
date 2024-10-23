import requests
import discord
from discord.ext import commands

class Fortnite:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://fortniteapi.io/v1/"

    def get_player_stats(self, username, platform):
        url = f"{self.base_url}/stats/{platform}/{username}"
        headers = {"Authorization": self.api_key}
        print("Request URL:", url) 
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch player stats:", response.status_code, response.text)
            return None
        
    def get_store_items(self):
        url = f"{self.base_url}/shop"
        headers = {"Authorization": self.api_key}
        print("Request URL:", url) 
        response = requests.get(url, headers=headers)

        print("Response Status Code:", response.status_code)
        print("Response Text:", response.text)

        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch store items:", response.status_code, response.text)
            return None

class DiscordBot:
    def __init__(self, discord_token, fortnite_api_key):
        self.discord_token = discord_token
        self.fortnite_api = Fortnite(fortnite_api_key)

        intents = discord.Intents.default()
        intents.message_content = True  

        self.bot = commands.Bot(command_prefix='!', intents=intents)  

        self.register_events()
        self.register_commands()

    def register_events(self):
        @self.bot.event
        async def on_ready():
            print(f'Bot is online as {self.bot.user}!')

    def register_commands(self):
        @self.bot.command(name='store')
        async def store(ctx):
            store_data = self.fortnite_api.get_store_items()  
            if store_data and 'items' in store_data:
                items = store_data['items']
                item_list = '\n'.join([f"{item['name']} - {item['price']}" for item in items])
                await ctx.send(f"**Fortnite Store Items:**\n{item_list}")
            else:
                await ctx.send("Could not retrieve store data.")

    def run(self):
        self.bot.run(self.discord_token)
