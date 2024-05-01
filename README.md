# Team Kill Tracker Discord Bot

## Overview

I developed this Team Kill Tracker bot to keep track of team kills among  me my friends during our games. I am hosting this bot on a Raspberry Pi 🥧 in my basement :) For the database, I'm using SQLite3.

## Features

- 😡 **Kill Tracking**: Record each team kill with a simple command.
- 🏆 **Leaderboard**: Displays a leaderboard of all players sorted by the number of team kills.
- 🐔 **Chicken feeder:** I had another project where I wanted to make a chicken feeder that was controlled by a discord bot and rather than making a new bot I just added it to his one. [Link to Chicken Feeder](https://github.com/tman2747/ChickenFeeder)

## Commands
- `!tk @DiscordUser` - Record a team kill for the mentioned user. This increments the user's kill count in the leaderboard.
- `!tk leaderboard` - Display the current leaderboard, showing players ranked by their number of team kills.
- `!tk help` - Show help information for the bot.
- `!tk` - Displays: `Use !tk @DiscordUser to record a team kill for the specified player.` 
- `!tk feedchicken ` used to send mqtt message to the chicken feeder. [Link to Chicken Feeder](https://github.com/tman2747/ChickenFeeder)

## Future
- Make the leaderboard display prettier using discord embed 
