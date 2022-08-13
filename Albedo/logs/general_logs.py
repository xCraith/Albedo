import datetime
from datetime import datetime

import naff
from naff import Client, Intents, listen, Extension

bot = Client(intents=Intents.ALL)

class general_logs(Extension):
    @listen()
    async def on_voice_state_update(self, event):
        if event.after:
            channel = await self.bot.fetch_channel(1008147785784242276)
            embed = naff.Embed(
                title="Voice Logs",
                color="#800080",
                description=f"<@{event.after.user_id}> has left <#{event.after.channel.id}>"
            )
            embed.set_footer(text="The Great Tomb of Nazarick")
            embed.timestamp = datetime.now()
            await channel.send(embeds=embed)

        if event.before:
            channel = await self.bot.fetch_channel(1008147785784242276)
            embed = naff.Embed(
                title="Voice Logs",
                color="#800080",
                description=f"<@{event.before.user_id}> has left <#{event.before.channel.id}>"
            )
            embed.set_footer(text="The Great Tomb of Nazarick")
            embed.timestamp = datetime.now()
            await channel.send(embeds=embed)

    @listen()
    async def on_member_add(self, event):
        channel = await self.bot.fetch_channel(1008146266577969172)
        embed = naff.Embed(
            title="Join-Leave Logs",
            color="#800080",
            description=f"<@{event.member.id}> joined the server"
        )
        embed.set_footer(text="The Great Tomb of Nazarick")
        embed.timestamp = datetime.now()
        await channel.send(embeds=embed)

    @listen()
    async def on_member_remove(self, event):
        channel = await self.bot.fetch_channel(1008146266577969172)
        embed = naff.Embed(
            title="Join-Leave Logs",
            color="#800080",
            description=f"<@{event.member.id}> left the server"
        )
        embed.set_footer(text="NK Community")
        embed.timestamp = datetime.now()
        await channel.send(embeds=embed)

    @listen()
    async def on_ban_create(self, event):
        channel = await self.bot.fetch_channel(1008147709590515814)
        embed = naff.Embed(
            title="Ban Logs",
            color="#800080",
            description=f"<@{event.user.id}> got banned from the Great Tomb of Nazarick"
        )
        embed.set_footer(text="The Great Tomb of Nazarick")
        embed.timestamp = datetime.now()
        await channel.send(embeds=embed)


    @listen()
    async def on_ban_remove(self, event):
        channel = await self.bot.fetch_channel(1008147709590515814)
        embed = naff.Embed(
            title="Ban Logs",
            color="#800080",
            description=f"<@{event.user.id}> got unbanned"
        )
        embed.set_footer(text="The Great Tomb of Nazarick")
        embed.timestamp = datetime.now()
        await channel.send(embeds=embed)


def setup(bot):
    general_logs(bot)