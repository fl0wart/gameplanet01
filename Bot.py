import discord
from discord.ext import commands
import asyncio

bot=commands.Bot(command_prefix='gp!')
@bot.event
async def on_ready():
    print('Logged in as '+bot.user.name+' (ID:'+bot.user.id+') | Connected to '+str(len(bot.servers))+' servers | Connected to '+str(len(set(bot.get_all_members())))+' users')
    print('--------')
    await bot.change_presence(game=discord.Game(name="IG: @gameplanet_official!", type=1))

bot.remove_command('help')

@bot.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def say(ctx, *args):
    mesg = ' '.join(args)
    await bot.delete_message(ctx.message)
    return await bot.say(mesg)
  
@bot.command(pass_context = True)
@commands.has_permissions(administrator=True) 
async def announce2(ctx, channel: discord.Channel=None, *, msg: str):
    embed=discord.Embed(description="{}".format(msg),color=0x00ffff)
    await bot.send_message(channel, embed=embed)
    await bot.delete_message(ctx.message)
    
bot.run('NTU2Mzc1NDg1NjM5MTYzOTI1.D241eA.mX9gcWly0SQn9yLIEzSCtwwmdRQ')
