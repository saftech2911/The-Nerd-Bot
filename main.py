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
        await ctx.send('Wait for it to be given....')
    elif sub == 'ban2' and ch == '2':
        await ctx.send('Wait for it to be given....')
    elif sub == 'ban2' and ch == '3':
        await ctx.send('Wait for it to be given....')
    elif sub == 'ban2' and ch == '4':
        await ctx.send('Wait for it to be given....')
    elif sub == 'phys' and ch == '1':
        await ctx.send('Wait for it to be given....')
    elif sub == 'phys' and ch == '2':
        await ctx.send('Wait for it to be given....')
    elif sub == 'phys' and ch == '3':
        await ctx.send('Wait for it to be given....')
    elif sub == 'phys' and ch == '4':
        await ctx.send('Wait for it to be given....')
    elif sub == 'chem' and ch == '1':
        await ctx.send('Wait for it to be given....')
    elif sub == 'chem' and ch == '2':
        await ctx.send('Wait for it to be given....')
    elif sub == 'chem' and ch == '3':
        await ctx.send('Wait for it to be given....')
    elif sub == 'chem' and ch == '4':
        await ctx.send('Wait for it to be given....')
    elif sub == 'biol' and ch == '1':
        await ctx.send('Wait for it to be given....')
    elif sub == 'biol' and ch == '2':
        await ctx.send('Wait for it to be given....')
    elif sub == 'biol' and ch == '3':
        await ctx.send('Wait for it to be given....')
    elif sub == 'biol' and ch == '4':
        await ctx.send('Wait for it to be given....')
    elif sub == 'bstu' and ch == '1':
        await ctx.send('Wait for it to be given....')
    elif sub == 'bstu' and ch == '2':
        await ctx.send('Wait for it to be given....')
    elif sub == 'bstu' and ch == '3':
        await ctx.send('Wait for it to be given....')
    elif sub == 'bstu' and ch == '4':
        await ctx.send('Wait for it to be given....')
    elif sub == 'econ' and ch == '1':
        await ctx.send('Wait for it to be given....')
    elif sub == 'econ' and ch == '2':
        await ctx.send('Wait for it to be given....')
    elif sub == 'econ' and ch == '3':
        await ctx.send('Wait for it to be given....')
    elif sub == 'econ' and ch == '4':
        await ctx.send('Wait for it to be given....')
    elif sub == 'comp' and ch == '1':
        await ctx.send('Notes upto 15 Jan: https://drive.google.com/u/0/uc?id=1aHYGgIcx-FMR0B_-WCitRoTa7OFEvx3P&export=download')
    elif sub == 'comp' and ch == '2':
        await ctx.send('Wait for it to be given....')
    elif sub == 'comp' and ch == '3':
        await ctx.send('Wait for it to be given....')
    elif sub == 'comp' and ch == '4':
        await ctx.send('Wait for it to be given....')
    elif sub == 'eng2' and ch == '1':
        await ctx.send('Wait for it to be given....')
    elif sub == 'eng2' and ch == '2':
        await ctx.send('Wait for it to be given....')
    elif sub == 'eng2' and ch == '3':
        await ctx.send('Wait for it to be given....')
    elif sub == 'eng2' and ch == '4':
        await ctx.send('Wait for it to be given....')
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
            'Syntax error. Error code: 6969. Please check out the command list:'
        )


@client.command()
async def joinclass(ctx, sub):
    if sub == 'eng1':
        await ctx.send(
            f'Here are the links. Choose whichever suitable:\nKawkab miss: https://www.google.com/url?q=https%3A%2F%2Fus04web.zoom.us%2Fj%2F73806308522%3Fpwd%3DUS85STdycEdqamw2UnMrV2dBdUY0dz09&sa=D&sntz=1&usg=AFQjCNHPOenPejLqNIND2Oq41IetxT7v1A\nRoohi miss: https://www.google.com/url?q=https%3A%2F%2Fus04web.zoom.us%2Fj%2F4378056418%3Fpwd%3DT2RMempNY1FWdEpYRE9pc1RJd3BUUT09&sa=D&sntz=1&usg=AFQjCNG5FzQayWR_Dq8YvlNHayhKmKO49A'
        )
    elif sub == 'eng2':
        await ctx.send(
            'Join link: https://www.google.com/url?q=https%3A%2F%2Fus04web.zoom.us%2Fj%2F9757036484%3Fpwd%3DUFF3WjhYUHh2RTVtN0RwUTErNFJkZz09&sa=D&sntz=1&usg=AFQjCNFcU-vFtX2n6tob7EIlP-y8ACgh3w'
        )
    elif sub == 'ban1':
        await ctx.send(
            'Join link: https://www.google.com/url?q=https%3A%2F%2Fus04web.zoom.us%2Fj%2F7336020645%3Fpwd%3DdXhVODZYMlA0MmFJZVZXZDhjdHkzQT09&sa=D&sntz=1&usg=AFQjCNFbTm9a58v-Xw9_cI41KjimZTWFDw'
        )
    elif sub == 'ban2':
        await ctx.send(
            'Join link: https://www.google.com/url?q=https%3A%2F%2Fus04web.zoom.us%2Fj%2F5434558529%3Fpwd%3DdytKaTJ3RjIxYXN1WmZUNkN2cFBlUT09&sa=D&sntz=1&usg=AFQjCNExu5zzTEc9Xi3_apWbugP9bQSVvA'
        )
    elif sub == 'phys':
        await ctx.send('Join link: https://us04web.zoom.us/j/9614923043?pwd=Qm1QVUMvNGZQRVgzQ0pYa0xRRXlmZz09')
    elif sub == 'chem':
        await ctx.send(
            'Join link: https://www.google.com/url?q=https%3A%2F%2Fus04web.zoom.us%2Fj%2F2141180447%3Fpwd%3DdVZWL1lpQUV6L2pYYUNqeHRtTkJQdz09&sa=D&sntz=1&usg=AFQjCNF8JXeAc6JXyg6zbmi8f88aJIDBFQ'
        )
    elif sub == 'biol':
        await ctx.send(
            'Join link: https://www.google.com/url?q=https%3A%2F%2Fus04web.zoom.us%2Fj%2F5707770669%3Fpwd%3DSDd3L0EvdmRKWHcxSmFKeVVMd2VBUT09&sa=D&sntz=1&usg=AFQjCNGjyDQ83B5YaquZHjdgFqzmLJSPzQ'
        )
    elif sub == 'bstu':
        await ctx.send(
            'Join link: https://www.google.com/url?q=https%3A%2F%2Fus04web.zoom.us%2Fj%2F7910053527%3Fpwd%3DM1RseUVKWmp3NXpoU0x0K2ZMamxWdz09&sa=D&sntz=1&usg=AFQjCNG-xKwLX6fiP70F49fmQOJXJ5GHJg'
        )
    elif sub == 'econ':
        await ctx.send(
            'Join link: https://zoom.us/j/8912796017?pwd=SjF6Tk01bWJRRHpuMHRUVDlXWG84QT09'
        )
    elif sub == 'comp':
        await ctx.send(
            'Join link for Mehidi Sir: https://www.google.com/url?q=https%3A%2F%2Fus02web.zoom.us%2Fj%2F81860791451%3Fpwd%3DWFBTUmdWdWU2cXZBcVdkNDcyTUV3dz09&sa=D&sntz=1&usg=AFQjCNHlEY6XXbXhdWJARAwXXbd3PF7KlA \nJoin link for Ishmam Sir: https://us04web.zoom.us/j/5065622363?pwd=cHVOM1JMRkxFWHZHZkpGbHRqUm1CZz09'
        )
    elif sub == 'admt':
        await ctx.send(
            'Join link: https://zoom.us/j/2498364585?pwd=K1Y2ZWNKNitkWkxuWVBORDZOMHJtUT09'
        )
    elif sub == 'matd':
        await ctx.send('https://us04web.zoom.us/j/6266764690?pwd=UXlUYThISXpMeWo1dncwd0JrWEZnZz09')


@client.command()
async def help(ctx):
    await ctx.send(
        'Get all the command lists and know haw to use me from here: https://sites.google.com/view/playpen8/the-nerd-bot?authuser=0'
    )


keep_alive()
client.run('Discord API Token Here')
