import discord
from discord.ext import commands
from discord.utils import find
import random
from keep_alive import keep_alive

client = commands.Bot(help_command=None, command_prefix='::')

hi = "Sup nerds. My name is The Nerd Bot. My founding father is @ʂαϝƚҽƈԋ_2911#9789. I'm mainly hanging 'round here to help u guys with notes and schedules for your session in Playpen. Hope u guys find me useful. \nIf you want to know how to get to me, just type ::help to se it all. \nIf u have any suggestions, contact @ʂαϝƚҽƈԋ_2911#9789 immediately."


@client.event
async def on_ready():
    await client.change_presence(
        status=discord.Status.online, activity=discord.Game('::help'))
    print('I am good to go!')


@client.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == 'general', guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send(hi.format(guild.name))


@client.command()
async def ping(ctx):
    await ctx.send(f'My Ping is:{round(client.latency * 1000)}ms')


@client.command(aliases=['pwheel', 'divination', '8ball'])
async def predict(ctx, *, question):
    responses = [
        'As I see it, yes.', 'Ask again later.', 'Better not tell you now.',
        'Cannot predict now.', 'Concentrate and ask again.',
        'Don’t count on it.', 'It is certain.', ' It is decidedly so.',
        'Most likely.', 'My reply is no.'
    ]
    await ctx.send(f'Question:{question}\n Answer: {random.choice(responses)}')





@client.command()
async def give(ctx, sub, ch):
    if sub == 'ban2' and ch == '1':
        await ctx.send('Link to note here')
    elif sub == 'ban2' and ch == '2':
        await ctx.send('Link to note here')
    elif sub == 'ban2' and ch == '3':
        await ctx.send('Link to note here')
    elif sub == 'ban2' and ch == '4':
        await ctx.send('Link to note here')
    elif sub == 'phys' and ch == '1':
        await ctx.send('Link to note here')
    elif sub == 'phys' and ch == '2':
        await ctx.send('Link to note here')
    elif sub == 'phys' and ch == '3':
        await ctx.send('Link to note here')
    elif sub == 'phys' and ch == '4':
        await ctx.send('Link to note here')
    elif sub == 'chem' and ch == '1':
        await ctx.send('Link to note here')
    elif sub == 'chem' and ch == '2':
        await ctx.send('Link to note here')
    elif sub == 'chem' and ch == '3':
        await ctx.send('Link to note here')
    elif sub == 'chem' and ch == '4':
        await ctx.send('Link to note here')
    elif sub == 'biol' and ch == '1':
        await ctx.send('Link to note here')
    elif sub == 'biol' and ch == '2':
        await ctx.send('Link to note here')
    elif sub == 'biol' and ch == '3':
        await ctx.send('Link to note here')
    elif sub == 'biol' and ch == '4':
        await ctx.send('Link to note here')
    elif sub == 'bstu' and ch == '1':
        await ctx.send('Link to note here')
    elif sub == 'bstu' and ch == '2':
        await ctx.send('Link to note here')
    elif sub == 'bstu' and ch == '3':
        await ctx.send('Link to note here')
    elif sub == 'bstu' and ch == '4':
        await ctx.send('Link to note here')
    elif sub == 'econ' and ch == '1':
        await ctx.send('Link to note here')
    elif sub == 'econ' and ch == '2':
        await ctx.send('Link to note here')
    elif sub == 'econ' and ch == '3':
        await ctx.send('Link to note here')
    elif sub == 'econ' and ch == '4':
        await ctx.send('Link to note here')
    elif sub == 'comp' and ch == '1':
        await ctx.send('Notes upto 15 Jan: https://drive.google.com/u/0/uc?id=1aHYGgIcx-FMR0B_-WCitRoTa7OFEvx3P&export=download')
    elif sub == 'comp' and ch == '2':
        await ctx.send('Link to note here')
    elif sub == 'comp' and ch == '3':
        await ctx.send('Link to note here')
    elif sub == 'comp' and ch == '4':
        await ctx.send('Link to note here')
    elif sub == 'eng2' and ch == '1':
        await ctx.send('Link to note here')
    elif sub == 'eng2' and ch == '2':
        await ctx.send('Link to note here')
    elif sub == 'eng2' and ch == '3':
        await ctx.send('Link to note here')
    elif sub == 'eng2' and ch == '4':
        await ctx.send('Link to note here')
    elif sub == 'routine' and ch == 'sunflower':
        await ctx.send(
            'Get your routine here: https://drive.google.com/uc?id=1jn6vxhMhdJ_5oQqSARV7VcDKaddJ2F33&export=download'
        )
    elif sub == 'routine' and ch == 'lotus':
        await ctx.send(
            'Get your routine here: https://drive.google.com/uc?id=1gypirmTw0R8ZIZKurS3c52GqBek4b_jv&export=download'
        )
    elif sub == 'routine' and ch == 'tulip':
        await ctx.send(
            'Get your routine here: https://drive.google.com/uc?id=1Hbvm8c9oRAJsn6wqgPuleIP0qJxL8Dgl&export=download'
        )
    elif sub == 'routine' and ch == 'rose':
        await ctx.send(
            'Get your routine here: https://drive.google.com/uc?id=1h7KVlGWbtfaTsf9j-uGvv-jMXpQm34ol&export=download'
        )
    else:
        await ctx.send(
            'Syntax error. Please check out the command list:'
        )


@client.command()
async def joinclass(ctx, sub): #Join class command: gives students zoom class links directly on demand
    if sub == 'eng1':
        await ctx.send(
            'Zoom Join Link Here'
        )
    elif sub == 'eng2':
        await ctx.send(
            'Zoom Join Link Here'
        )
    elif sub == 'ban1':
        await ctx.send(
            'Zoom Join Link Here'
        )
    elif sub == 'ban2':
        await ctx.send(
            'Zoom Join Link Here'
        )
    elif sub == 'phys':
        await ctx.send('Zoom Join Link Here')
    elif sub == 'chem':
        await ctx.send(
            'Zoom Join Link Here'
        )
    elif sub == 'biol':
        await ctx.send(
            'Zoom Join Link Here'
        )
    elif sub == 'bstu':
        await ctx.send(
            'Zoom Join Link Here'
        )
    elif sub == 'econ':
        await ctx.send(
            'Zoom Join Link Here'
        )
    elif sub == 'comp':
        await ctx.send(
            'Zoom Join Link Here'
        )
    elif sub == 'admt':
        await ctx.send(
            'Zoom Join Link Here'
        )
    elif sub == 'matd':
        await ctx.send('Zoom Join Link Here')


@client.command()
async def help(ctx):
    await ctx.send(
        'Get all the command lists and know haw to use me from here: https://sites.google.com/view/playpen8/the-nerd-bot?authuser=0'
    ) #The website is no longer available


keep_alive() #So that the bot is running continuosuly
client.run('Discord API Token Here') #API Token removed for confidentiality
