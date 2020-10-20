import os
from discord.ext import commands
from config import settings
from config import access

# import time

bot = commands.Bot(command_prefix=settings['prefix'])


@bot.command()
async def Kredo(ctx, number: int, *args):
    if ctx.message.author.id in access:
        if (number is None) or (len(args) == 0):
            return await ctx.send('%Kredo (кол-во пингов) (Роли/пользователи, которых надо пингануть через пробел)')
        for _ in range(number):
            await ctx.send(" ".join(x for x in args))
    else:
        await ctx.send('**Только деду Хосту и владыке Kredo позволено пользоваться этой командой!** (*И моему '
                       'создателю*)')
