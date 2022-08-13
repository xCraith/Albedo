import datetime
from datetime import datetime

import naff
from naff import Client, Intents, listen, Extension

bot = Client(intents=Intents.ALL)

class member_updates(Extension):
    @listen()
    async def on_member_update(self, event):
        for role in event.after.roles:
            if role not in event.before.roles:
                channel = await self.bot.fetch_channel(1008146242800468089)
                embed = naff.Embed(
                    title="Role Logs",
                    color="#800080",
                    description=f"<@{event.after.id}> was added the role <@&{role.id}>"
                )
                embed.set_footer(text="The Great Tomb of Nazarick")
                embed.timestamp = datetime.now()
                await channel.send(embeds=embed)

        for role in event.before.roles:
            if role not in event.after.roles:
                channel = await self.bot.fetch_channel(1008146242800468089)
                embed = naff.Embed(
                    title="Role Logs",
                    color="#800080",
                    description=f"<@{event.after.id}> was removed the role <@&{role.id}>"
                )
                embed.set_footer(text="NK Community")
                embed.timestamp = datetime.now()
                await channel.send(embeds=embed)

        if event.after.nick != event.before.nick:
            channel = await self.bot.fetch_channel(1008147275345834065)
            embed = naff.Embed(
                title="Name Logs",
                color="#800080",
                description=f"<@{event.before.id}> Has changed his/her name"
            )
            embed.add_field(name="Old Nickname:", value=f"```{event.before.nick}```")
            embed.set_footer(text="The Great Tomb of Nazarick")
            embed.timestamp = datetime.now()
            await channel.send(embeds=embed)


def setup(bot):
    member_updates(bot)