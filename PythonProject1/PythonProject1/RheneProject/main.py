maindummy = """
#!/usr/bin/env python
import asyncio
import logging
import os
import time
import discord
from PythonProject1.RheneProject.dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.message_content = True
from discord.ext import commands

bot = commands.Bot(command_prefix='>', intents=intents)

@bot.event
async def on_ready():
    print(f"We are ready to go in, {bot.user.name}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "kill it with fire" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention}, You should EXTERMINATE yourself. NOW!")

    await bot.process_commands(message)

@bot.command()
async def hi(ctx):
    await ctx.send(f"I don't feel up to it.")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hi?")

@bot.command()
async def snipe(ctx):
    await ctx.send("Who should I spam ping? Um, I mean... *snipe*? Could you tell me their @?")

    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    try:
        user_message = await bot.wait_for("message", check=check, timeout=30.0)  # Waits for 30 seconds
        thevictim = user_message.content
        bignono = 0
        if "@" not in thevictim:
            await ctx.send(f"I don't think that's the right format which I require!")
        if "@" in thevictim:
            await ctx.send("How many pings...?")
            user_message = await bot.wait_for("message", check=check, timeout=10.0)
            maxim = user_message.content
            try:
                maxim = int(maxim)
            except ValueError:
                bignono = 1
            except asyncio.TimeoutError:
                await ctx.send("...")
        if bignono == 1:
            await ctx.send("Please enter an integer, you little dimwit. :wilted_rose:")
        if bignono == 0:
            maxim = int(maxim)
            count = 0
            while count < maxim:
                await ctx.send(f"{thevictim}")
                count = count + 1
                time.sleep(0.01)
    except asyncio.TimeoutError:
        await ctx.send("I didn't hear you, dumbass.")

@bot.command()
async def calc(ctx, *, expression: str):
    await ctx.send(f"I fuckin' hate maths.")
    try:
        allowed_chars = "0123456789+-*/(). "
        if not all(c in allowed_chars for c in expression):
            await ctx.send("This... is a security measure! Use only numbers, +, -, *, /, (, ) and spaces.")
            return

        result = eval(expression)
        await ctx.send(f'The result of `{expression}` is: **{result}**')
    except (SyntaxError, ZeroDivisionError, TypeError) as e:
        await ctx.send(f'I do not think this is valid: {e}')
    except Exception as e:
        await ctx.send(f'An unexpected error occurred, whoopsies!: {e}')

@bot.command()
async def kys(ctx):
    await ctx.send(f"I see. {ctx.author.mention}. guess who's getting the uhhhh the ermmm the gun tonight")


bot.run(token, log_handler=handler, log_level=logging.INFO)
"""