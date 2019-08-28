import discord                  # Discord.py API
import requests                 # To download the files
import os                       # To create the necessary directories
from datetime import datetime   # To print system date and time
from credentials import TOKEN   # Bot's token contained in credentials.py (ignored by git)

# Version Number
VERSION = "v0.5 - BETA BUILD"

# A list of commands with brief descriptions
help_block = "```" \
             "---HashBot HELP---" \
            "\n$hash - Hashes the attached file and sends a message containing the hash. Ex: $hash SHA256" \
            "\n$help - Sends this help message to the channel it was invoked in." \
            "\n$about - Sends a message containing information about this bot to the channel it was invoked in." \
            "```"

# A list of supported hashes
supported_hashes = "```" \
                   "---List of Supported Hashes---\n" \
                   "MD2, MD4, MD5, SHA1, SHA256" \
                   "```"

about_string = "Version: " + VERSION + "\nBuilt by Daniel Kuzmin \nhttps://github.com/danielkuzmin"


# Creates the necessary directories if they do not exist
def create_directories():
    try:
        # This is where the requested file is stored while it's being hashed
        os.makedirs(r"HASHBOT_FILES\TEMPFILES")
        # This is where the logs are
        os.makedirs(r"HASHBOT_FILES\LOGS")
    except FileExistsError:
        pass


# Message printed to the console when the bot starts
print(f'HashBot is powering up...')
print("Current System date and time: ", datetime.now())

client = discord.Client()

# Message printed to the console when the bot joins discord
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    # Creates a list of servers the bot is connected to
    servers = '\n - '.join([guild.name for guild in client.guilds])
    print(f'Servers Connected:\n - {servers}')
    create_directories()


@client.event
async def on_message(message):
    # Sends help_block to the channel it was invoked in
    if message.content == '$help':
        if message.author == client.user:
            return
        await message.channel.send(help_block)

    # Sends about_string to the channel it was invoked in
    if message.content == '$about':
        if message.author == client.user:
            return
        await message.channel.send(about_string)
        await message.channel.send(supported_hashes)

    # $hash command
    if '$hash' in message.content:
        if message.author == client.user:
            return

        print(str(datetime.now()) + " - $hash Command Invoked!")
        if not message.attachments:
            await message.channel.send("```Error: No file attached to message.```")
            await message.channel.send(help_block)
            return

        # Everything below occurs only if a file is attached
        print(message.attachments)

client.run(TOKEN)
