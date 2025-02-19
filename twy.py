import discord
from discord import app_commands
from discord.ext import commands
import requests
from dotenv import load_dotenv
import os

load_dotenv()

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)
tree = bot.tree

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    try:
        synced = await tree.sync()
        print(f'Synced {len(synced)} commands.')
    except Exception as e:
        print(f'Failed to sync commands: {e}')

@tree.command(name="pixel", description="Check the price of Pixel in PHP")
async def pixel(interaction: discord.Interaction):
    try:
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=pixels&vs_currencies=php&include_24hr_change=true')
        data = response.json()
        pixel_price_php = data['pixels']['php']
        pixel_24h_change = data['pixels']['php_24h_change']

        change_symbol = "🔺" if pixel_24h_change > 0 else "🔻"

        await interaction.response.send_message(f'The current price of Pixel is **₱ {pixel_price_php:.2f}** {change_symbol} {pixel_24h_change:.2f}%')
    except Exception as e:
        await interaction.response.send_message(f'An error occurred: {e}')

@tree.command(name="pol", description="Check the price of Polygon (POL, ex-MATIC) in PHP")
async def pol(interaction: discord.Interaction):
    try:
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=matic-network&vs_currencies=php&include_24hr_change=true')
        data = response.json()
        pol_price_php = data['matic-network']['php']
        pol_24h_change = data['matic-network']['php_24h_change']

        change_symbol = "🔺" if pol_24h_change > 0 else "🔻"

        await interaction.response.send_message(f'The current price of Polygon (POL, ex-MATIC) is **₱ {pol_price_php:.2f}** {change_symbol} {pol_24h_change:.2f}%')
    except Exception as e:
        await interaction.response.send_message(f'An error occurred: {e}')

@tree.command(name="ronin", description="Check the price of Ronin (RON) in PHP")
async def ronin(interaction: discord.Interaction):
    try:
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ronin&vs_currencies=php&include_24hr_change=true')
        data = response.json()
        ronin_price_php = data['ronin']['php']
        ronin_24h_change = data['ronin']['php_24h_change']

        change_symbol = "🔺" if ronin_24h_change > 0 else "🔻"

        await interaction.response.send_message(f'The current price of Ronin (RON) is **₱ {ronin_price_php:.2f}** {change_symbol} {ronin_24h_change:.2f}%')
    except Exception as e:
        await interaction.response.send_message(f'An error occurred: {e}')

@tree.command(name="usdc", description="Check the price of USDC in PHP")
async def usdc(interaction: discord.Interaction):
    try:
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=usd-coin&vs_currencies=php&include_24hr_change=true')
        data = response.json()
        usdc_price_php = data['usd-coin']['php']
        usdc_24h_change = data['usd-coin']['php_24h_change']

        change_symbol = "🔺" if usdc_24h_change > 0 else "🔻"

        await interaction.response.send_message(f'The current price of USDC is **₱ {usdc_price_php:.2f}** {change_symbol} {usdc_24h_change:.2f}%')
    except Exception as e:
        await interaction.response.send_message(f'An error occurred: {e}')

@tree.command(name="usdt", description="Check the price of USDT in PHP")
async def usdt(interaction: discord.Interaction):
    try:
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=tether&vs_currencies=php&include_24hr_change=true')
        data = response.json()
        usdt_price_php = data['tether']['php']
        usdt_24h_change = data['tether']['php_24h_change']

        change_symbol = "🔺" if usdt_24h_change > 0 else "🔻"

        await interaction.response.send_message(f'The current price of USDT is **₱ {usdt_price_php:.2f}** {change_symbol} {usdt_24h_change:.2f}%')
    except Exception as e:
        await interaction.response.send_message(f'An error occurred: {e}')

@tree.command(name="slp", description="Check the price of SLP in PHP")
async def slp(interaction: discord.Interaction):
    try:
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=smooth-love-potion&vs_currencies=php&include_24hr_change=true')
        data = response.json()
        slp_price_php = data['smooth-love-potion']['php']
        slp_24h_change = data['smooth-love-potion']['php_24h_change']

        change_symbol = "🔺" if slp_24h_change > 0 else "🔻"

        await interaction.response.send_message(f'The current price of SLP is **₱ {slp_price_php:.2f}** {change_symbol} {slp_24h_change:.2f}%')
    except Exception as e:
        await interaction.response.send_message(f'An error occurred: {e}')

bot.run(os.getenv('BOT_TOKEN'))