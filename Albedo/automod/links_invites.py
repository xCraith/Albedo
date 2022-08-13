from multiprocessing.dummy import list
import datetime
from datetime import datetime
import naff
from naff import Client, Intents, listen, Extension, slash_command, slash_option, slash_default_member_permission, Permissions, InteractionContext, OptionTypes
import mysql.connector

bot = Client(intents=Intents.ALL)

with open("./automod/blacklist.txt", "r", encoding="utf-8") as bl:
    content = bl.read()
    blacklist = content.split()

"""with open("./automod/whitelist.txt", "r") as wl:
    contentwl = wl.read()
    whitelist = contentwl.split()"""


with open("./automod/blacklistwords.txt", "r", encoding="utf-8") as blw:
    contentw = blw.read()
    blacklistwords = contentw.split()

async def ConnectQuery():
    db = mysql.connector.connect(
        host="localhost",
        user="main",
        password="vT69Ij9KiDlpfL6R",
        database="bot",
    )
    cursor = db.cursor()
    return db


class Blacklist(Extension):
    @listen()  # Message Create Log
    async def on_message_create(self, event):
        # username = event.message.author.id
        msg = event.message.content

        for bword in blacklistwords:
            if bword in msg:
                if event.message.author.bot:
                    return
                else:
                    await event.message.delete()
                    await event.message.channel.send(f" {event.message.author.mention} Your message contains one or multiple words which are on our Blacklist \n"
                                                     f"If you continue to violate our rules, you will either be banished or muted.")
                    channel = await self.bot.fetch_channel(1008150891033002095)
                    embed = naff.Embed(
                        title="Automod Logs",
                        color="#800080",
                        description=f"A message by <@{event.message.author.id}> in <#{event.message.channel.id}> got blocked."
                    )
                    embed.add_field(name="Nachrichteninhalt", value=f"```{event.message.content}```")
                    embed.timestamp = datetime.now()
                    embed.set_footer(text="The Great Tomb of Nazarick")
                    await channel.send(embeds = embed)

        for word in blacklist:
            if event.message.author.bot:
                return
            elif word in msg:
                if "cdn.discordapp.com" in event.message.content:
                    return
                else:
                    await event.message.delete()
                    await event.message.author.add_role(1008150035038490625)
                    await event.message.channel.send(f" {event.message.author.mention} Our Chat Monitoring System detected that your message either contains a Scam-, Phising-, or Invitelink. \n"
                                                     f"After you managed to fix your account, please send a DM to the leadership")
                    channel = await self.bot.fetch_channel(1008150891033002095)
                    embed = naff.Embed(
                        title="Automod Logs",
                        color="#800080",
                        description=f"A message by <@{event.message.author.id}> was blocked in <#{event.message.channel.id}>"
                    )
                    embed.add_field(name="Message Content", value=f"```{event.message.content}```")
                    embed.timestamp = datetime.now()
                    embed.set_footer(text="The Great Tomb of Nazarick")
                    await channel.send(embeds = embed)

    @slash_command(name="blacklist", description="Write a word on the blacklist")
    @slash_option(name="word", description="The word", required=True, opt_type=OptionTypes.STRING)
    @slash_default_member_permission(Permissions.BAN_MEMBERS)
    async def wblacklist(self, ctx:InteractionContext, word):
        f = open("./automod/blacklistwords.txt", encoding="utf-8")
        if word in blacklistwords:
            await ctx.send(f"**{word}** Is already on the blacklist")
        else:
            f = open("./automod/blacklistwords.txt", "a", encoding="utf-8")
            f.write(f"\n{word.title()}")
            f.write(f"\n{word}")
            await ctx.send(f"**{word}** was sucessfully added to the blacklist")







def setup(bot):
    Blacklist(bot),



def setup(bot):
    Blacklist(bot),
