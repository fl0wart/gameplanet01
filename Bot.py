import asyncio
import discord
from discord.ext.commands import Bot

bot.loop.create_task(status_task())

Mike = Bot('gp!')

@Mike.command(pass_context = True)
async def say(ctx, *args):
    mesg = ' '.join(args)
    await Mike.delete_message(ctx.message)
    return await Mike.say(mesg)
@bot.event	                                                
async def status_task():
    while True:
        await bot.change_presence(game=discord.Game(name='GamePlanet 👀', type=3))
        
Mike.run(NTU2Mzc1NDg1NjM5MTYzOTI1.D241eA.mX9gcWly0SQn9yLIEzSCtwwmdRQ)
