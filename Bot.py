import asyncio
import discord
from discord.ext.commands import Bot


Mike = Bot('gp!')

@Mike.command(pass_context = True)
async def say(ctx, *args):
    mesg = ' '.join(args)
    await Mike.delete_message(ctx.message)
    return await Mike.say(mesg)

game = discord.Game("with the users!")

Mike.run('NTU2Mzc1NDg1NjM5MTYzOTI1.D241eA.mX9gcWly0SQn9yLIEzSCtwwmdRQ')
