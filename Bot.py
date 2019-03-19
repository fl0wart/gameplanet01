import asyncio
import discord
from discord.ext.commands import Bot


Mike = Bot('gp!')

@Mike.event
async def on_ready():
    print ("Starting up")
    print ("My username is " + bot.user.name + " and i am running with the ID: " + bot.user.id)
    await Mike.change_presence(game=discord.Game(name="the users", type=3))
    print ("Started")
    
@Mike.command(pass_context = True)
async def say(ctx, *args):
    mesg = ' '.join(args)
    await Mike.delete_message(ctx.message)
    return await Mike.say(mesg)


Mike.run('NTU2Mzc1NDg1NjM5MTYzOTI1.D241eA.mX9gcWly0SQn9yLIEzSCtwwmdRQ')
