from discord.ext.commands import Cog, Context, hybrid_command


class DevCog(Cog):
    def __init__(self, bot):
        self.bot = bot

    @hybrid_command(name="ping", description="Pong!")
    async def ping(self, ctx: Context):
        await ctx.send("Pong!")
