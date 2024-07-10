import asyncio
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import logging

DISCORD_TOKEN = "DISCORD_TOKEN"


class MarranBot(commands.Bot):
    sync_commands = False
    """Prevent rate-limiting."""

    def __init__(self, command_prefix, intents):
        super().__init__(command_prefix=command_prefix, intents=intents)

    async def on_ready(self):
        logging.info(f"{self.user} has connected!")

        try:
            if self.sync_commands:
                synced = await self.tree.sync()
                logging.info(f"Synced {len(synced)} command(s)")

            logging.info("Ready")
        except Exception as error:
            logging.error(error, exc_info=True)

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            pass
        elif isinstance(error, commands.CommandNotFound):
            await ctx.send(content=error)
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(content=error)
        else:
            logging.error(error, exc_info=True)
            await ctx.send("Internal error. Command failed")

    @commands.hybrid_command(name="ping", description="Pong!")
    async def ping(self, ctx: commands.Context, user: discord.User):
        await ctx.send(f"Pong! {user.mention}")


async def main() -> None:
    intents = discord.Intents.default()
    intents.message_content = True
    logging.basicConfig(level=logging.INFO)

    bot = MarranBot(command_prefix="!", intents=intents)
    await bot.start(os.getenv(DISCORD_TOKEN))


if __name__ == "__main__":
    load_dotenv()

    discord_token = os.getenv(DISCORD_TOKEN)

    if discord_token is None or discord_token.strip() == "":
        logging.error("'DISCORD_TOKEN' environment variable must be set")
        exit(1)

    asyncio.run(main())
