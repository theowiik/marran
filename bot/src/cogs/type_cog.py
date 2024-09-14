from discord.ext.commands import Cog, Context, hybrid_command

from services.language_service import Language, get_sentence


class TypeCog(Cog):
    def __init__(self, bot):
        self.bot = bot

    @hybrid_command(name="type", description="Type race!")
    async def ping(self, ctx: Context):
        msg = get_sentence(10, Language.SWEDISH)
        await ctx.send(msg)
