from enum import Enum

from discord.ext.commands import Cog, Context, hybrid_command


class Language(Enum):
    SWEDISH = "swedish"
    ENGLISH = "english"


def get_sentence(words: int, language: Language) -> str:
    return ""


class TypeCog(Cog):
    def __init__(self, bot):
        self.bot = bot

    @hybrid_command(name="type", description="Type race!")
    async def ping(self, ctx: Context):
        await ctx.send("Pong!")
