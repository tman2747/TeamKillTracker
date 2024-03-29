import settings
import discord
from discord.ext import commands
import sqlite3

def update_kills(player_id, player_name):
    with sqlite3.connect("DiscordBot.db") as conn:
        db = conn.cursor()
        db.execute('''INSERT INTO leaderboard (player_id, player_name, kills, last_updated) 
                      VALUES (?, ?, 1, CURRENT_TIMESTAMP) 
                      ON CONFLICT(player_id) 
                      DO UPDATE SET kills = kills + 1, last_updated = CURRENT_TIMESTAMP''',
                    (player_id, player_name))
        conn.commit()

def get_leaderboard():
    with sqlite3.connect("DiscordBot.db") as conn:
        db = conn.cursor()
        db.execute("SELECT player_name, kills, last_updated FROM leaderboard ORDER BY kills DESC")
        return db.fetchall()

def run():
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        print("Bot is now ready for use")
        print(bot.user)

    @bot.command()
    async def TK(ctx, Player: discord.Member):
        update_kills(str(Player.id), Player.display_name)
        await ctx.send(f"Kill counted for {Player.display_name}")

    @bot.command()
    async def leaderboard(ctx):
        leaderboard_data = get_leaderboard()
        if not leaderboard_data:
            await ctx.send("The leaderboard is currently empty.")
            return

        leaderboard_message = "Leaderboard:\n"
        for player_name, kills, last_updated in leaderboard_data:
            last_kill_date = last_updated.split(' ')[0] 
            leaderboard_message += f"{player_name}: {kills} kills (Last Teamkill: {last_kill_date})\n"
        await ctx.send(leaderboard_message)

    bot.run(settings.DISCORD_API_SECRET)

if __name__ == "__main__":
    connection = sqlite3.connect("DiscordBot.db")
    db = connection.cursor()
    db.execute('''CREATE TABLE IF NOT EXISTS leaderboard (
        player_id TEXT PRIMARY KEY,
        player_name TEXT NOT NULL,
        kills INTEGER NOT NULL DEFAULT 0,
        last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    connection.commit()
    connection.close()
    run()
