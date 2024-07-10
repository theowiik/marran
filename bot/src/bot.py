import asyncio
import logging
import os

from discord import Intents
from discord.ext.commands import BadArgument, Bot, CommandNotFound, CommandOnCooldown
from dotenv import load_dotenv

from cogs.dev_cog import DevCog

DISCORD_TOKEN = "DISCORD_TOKEN"


class MarranBot(Bot):
    sync_commands = False
    """Prevent rate-limiting."""

    def __init__(self, command_prefix: str, intents):
        super().__init__(command_prefix=command_prefix, intents=intents)

    async def on_ready(self) -> None:
        logging.info(f"{self.user} has connected!")

        try:
            if self.sync_commands:
                synced = await self.tree.sync()
                logging.info(f"Synced {len(synced)} command(s)")

            logging.info("Ready")
        except Exception as error:
            logging.error(error, exc_info=True)

    async def on_command_error(self, ctx, error) -> None:
        logging.error(f"Error in command {ctx.command}:", exc_info=error)

        if isinstance(error, BadArgument):
            pass
        elif isinstance(error, CommandNotFound):
            await ctx.send(content=error)
        elif isinstance(error, CommandOnCooldown):
            await ctx.send(content=error)
        else:
            await ctx.send("uh oh, code brokey 💥")


async def main() -> None:
    intents = Intents.default()
    intents.message_content = True
    logging.basicConfig(level=logging.INFO)

    bot = MarranBot(command_prefix="!", intents=intents)
    await bot.add_cog(DevCog(bot))
    await bot.start(os.getenv(DISCORD_TOKEN))


if __name__ == "__main__":
    load_dotenv()
    discord_token = os.getenv(DISCORD_TOKEN)

    if discord_token is None or discord_token.strip() == "":
        logging.error(f"'{DISCORD_TOKEN}' environment variable must be set")
        exit(1)

    asyncio.run(main())
