import settings
import discord
from discord.ext import commands


def run():
    intents = discord.Intents.all()

    bot = commands.Bot(command_prefix='!',intents=intents)

    @bot.event
    async def on_ready():
        print("Bot is now ready for use")
        print(bot.user)
    @bot.command()
    async def TK(ctx):
        await ctx.send("kill counted")

    bot.run(settings.DISCORD_API_SECRET)

if __name__ == "__main__":
    run()