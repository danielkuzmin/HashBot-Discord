import discord                  # Discord.py API
from datetime import datetime   # To print system date and time
from credentials import TOKEN   # Bot's token contained in credentials.py

# Message printed to the console when the bot starts
print(f'HashBot is powering up...')
print("Current System date and time: ", datetime.now())

client = discord.Client()

# Message printed to the console when the bot joins discord
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    servers = '\n - '.join([guild.name for guild in client.guilds])
    print(f'Servers Connected:\n - {servers}')

client.run(TOKEN)
