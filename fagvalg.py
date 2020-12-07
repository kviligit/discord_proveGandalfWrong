import discord

# Finds the relevant instance of the bot-token in the token.txt
TOKEN = open(“token.txt”,”r”).readline()
# Sets the command prefix to "!", telling the bot that all
# messages starting with a "!", is meant as a command to the bot.
client = commands.Bot(command_prefix = ‘!’)
client.run(TOKEN)

#answers with the ms latency
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round (client.latency * 1000)}ms ')
