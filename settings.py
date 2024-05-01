import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_API_SECRET = os.getenv("DISCORD_API_TOKEN")
dns = os.getenv("dns")
usernamemqtt = os.getenv("usernamemqtt")
password = os.getenv("password")
