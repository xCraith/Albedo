import datetime
from datetime import datetime

import naff
from naff import Client, Intents, listen, Extension

bot = Client(intents=Intents.ALL)


"""class LogsCrMsg(Extension):
    @listen()  # Message Create Log
    async def on_message_create(self, event):
        # This event is called when a message is sent in a channel the bot can see
        if event.message.author.id == 978575631019290625 or event.message.author.id == 978561957097512980 or event.message.author.id == 989845254322659328 or event.message.channel.id == 989900677931225170 or event.message.channel.id == 989899336819310632 or event.message.channel.id == 989899149300355132 or event.message.channel.id == 989899103678906368:
            return
        channel = await self.bot.fetch_channel(989899336819310632)
        icon = event.message.author.avatar.url
        wo = event.message.channel.id
        embed = naff.Embed(
            title="{}".format(event.message.author),
            color="#f5b642",
            description=f"Hat eine Nachricht in <#{wo}> geschrieben"
        )

        embed.add_field(name="Nachricht:", value=f"```{event.message.content}```")
        embed.add_field(name="DiscordID:", value=f"```{event.message.author.id}```")
        embed.set_thumbnail(url=icon)
        embed.set_footer(text="NK Community")
        embed.timestamp = embed.timestamp = datetime.now()
        await channel.send(embeds=embed)"""


class LogsDelMsg(Extension):
    @listen()  # Message delete Log
    async def on_message_delete(self, event):
        if event.message.author.id == 1008146330612416632 or event.message.author.id == 978561957097512980 or event.message.channel.id == 989900677931225170 or event.message.channel.id == 989899336819310632 or event.message.channel.id == 989899336819310632 or event.message.channel.id == 989899149300355132 or event.message.channel.id == 989899103678906368:
            return
        channel = await self.bot.fetch_channel(1008146330612416632)
        wo = event.message.channel.id
        embed = naff.Embed(
            title="{}".format(event.message.author),
            color="#800080",
            description=f"A message in <#{wo}> got deleted"
        )
        icon = event.message.author.avatar.url
        embed.add_field(name="Message:", value=f"```{event.message.content}```")
        embed.add_field(name="DiscordID:", value=f"```{event.message.author.id}```")
        embed.set_thumbnail(url=icon)
        embed.set_footer(text="The Great Tomb of Nazarick")
        embed.timestamp = datetime.now()
        # await channel.send(f"Nachricht: {event.message.content} von [ {event.message.author.display_name} ] ID: [ {
        # event.message.author.id} ]")
        await channel.send(embeds=embed)


class LogsEditMsg(Extension):
    @listen()  # Message edit log
    async def on_message_update(self, event):
        if event.before.author.id == 1008142827764592652 or event.before.author.id == 989845254322659328:
            return
        else:
            try:
                old = event.before.content
                new = event.after.content
            except AttributeError:
                return
            wo = event.before.channel.id
            channel = await self.bot.fetch_channel(1008146330612416632)
            embed = naff.Embed(
                title="{}".format(event.before.author),
                color="#800080",
                description=f"Has edited a message in <#{wo}>"
            )
            icon = event.before.author.avatar.url
            embed.add_field(name="Old Message", value=f"```{old}```")
            embed.add_field(name="New Message", value=f"```{new}```")
            embed.add_field(name="DiscordID:", value=f"```{event.before.author.id}```")
            embed.set_thumbnail(url=icon)
            embed.set_footer(text="The Great Tomb of Nazarick")
            embed.timestamp = datetime.now()
            # await channel.send(f"Nachricht: {event.message.content} von [ {event.message.author.display_name} ] ID: [ {
            # event.message.author.id} ]")
            await channel.send(embeds=embed)

            print(new)
            print(old)


def setup(bot):
    #LogsCrMsg(bot),
    LogsDelMsg(bot),
    LogsEditMsg(bot)
