import asyncio
import discord
from discord.ext.commands import Bot


Mike = Bot('gp!')

@Mike.event
async def on_ready():
    print ("Starting up")
    print ("My username is " + Mike.user.name + " and i am running with the ID: " + Mike.user.id)
    await Mike.change_presence(game=discord.Game(name="IG: @gameplanet_official", type=1))
    print ("Started")
    
Mike.remove_command('help')

@Mike.command(pass_context = True)
async def say(ctx, *args):
    mesg = ' '.join(args)
    await Mike.delete_message(ctx.message)
    return await Mike.say(mesg)

@Mike.command(pass_context = True)
async def announce(ctx, channel: discord.Channel=None, *, msg: str):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed=discord.Embed(title="description="{}".format(msg), color = discord.Color((r << 16) + (g << 8) + b))
    await client.send_message(channel, embed=embed)
    await client.delete_message(ctx.message)
    
Mike.run('NTU2Mzc1NDg1NjM5MTYzOTI1.D241eA.mX9gcWly0SQn9yLIEzSCtwwmdRQ')
