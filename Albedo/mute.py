import mysql.connector
import datetime
from datetime import datetime, timedelta
from naff import Client, Intents, slash_command, InteractionContext, OptionTypes, slash_option, Extension, \
    slash_default_member_permission, Permissions, Embed, Task, IntervalTrigger, listen
import naff
import asyncio

async def ConnectQuery():
    db = mysql.connector.connect(
        host="localhost",
        user="main",
        password="vT69Ij9KiDlpfL6R",
        database="bot",
    )
    cursor = db.cursor()
    return db



class mute_system(Extension):
    @slash_command(name="mute", description="Einen User muten")
    @slash_default_member_permission(Permissions.MOVE_MEMBERS)
    @slash_option(
        name="user",
        description="User angeben",
        required=True,
        opt_type=OptionTypes.USER,
    )
    @slash_option(
        name="dauer",
        description="Grund angeben",
        required=True,
        opt_type=OptionTypes.STRING
    )
    @slash_option(
        name="grund",
        description="Grund angeben",
        required=True,
        opt_type=OptionTypes.STRING
    )
    async def mute(self, ctx:InteractionContext, user, dauer, grund=None):
        guild = ctx.guild
        rolle = await ctx.guild.fetch_role(993305749763661875)
        time_convert = {"s":1, "m":60, "h":3600, "d":86400, "w":604800, "mo":18144000, "y":31536000}
        tempmute= int(dauer[:-1]) * time_convert[dauer[-1]]
        channel = await self.bot.fetch_channel(993306264346050672)
        dbmute = datetime.now() + timedelta(seconds=tempmute)
        db = await ConnectQuery()

        if user.has_role(rolle):
            await ctx.send("User ist bereits gemuted")
        else:
            embed = naff.Embed(
                title="Muted",
                color="#f5b642",
                description=f"<@{user.id}> wurde für **{dauer}** gemuted",
            )
            embed.set_footer(text="NK Community")
            embed.timestamp = datetime.now()
            await ctx.send(embeds=embed)
            eb = naff.Embed(
                title="Mute Log",
                color="#f5b642",
                description=f"<@{ctx.author.id}> hat den User <@{user.id}> mit dem Grund **{grund}** für {dauer} gemuted",
            )
            eb.set_footer(text="NK Community")
            eb.timestamp = datetime.now()
            await channel.send(embeds=eb)
            cursor = db.cursor()
            sql = "INSERT INTO mute (discordid, dauer) VALUES (%s, %s)"
            val = (user.id, dbmute)
            cursor.execute(sql, val)
            db.commit()
            await user.add_role(rolle)
            #await asyncio.sleep(tempmute)
            #await user.remove_role(rolle)
            db.close()

    @listen()
    async def on_ready(self):
        self.unmute_task.start()

    @Task.create(IntervalTrigger(seconds=30))
    async def unmute_task(self):
        db = await ConnectQuery()
        guild = self.bot.get_guild(401479187694747690)
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM mute WHERE dauer <= '{datetime.now()}'")
        users = cursor.fetchall()
        rolle = await guild.fetch_role(1008150035038490625)
        for user in users:
            if user[2] is not None:
                member = await self.bot.fetch_member(user[1], 401479187694747690)
                await member.remove_role(rolle)
                dlt = "DELETE FROM mute WHERE discordid = {0}".format(user[1])
                cursor.execute(dlt)
                db.commit()
                db.close()
                channel = await self.bot.fetch_channel(993526422075347087)
                eb = naff.Embed(
                    title="Automod Log",
                    color="#f5b642",
                    description=f"<@{member.id}> Wurde entmuted \n"
                                f"**Grund:** Mute abgelaufen",
                )
                eb.set_footer(text="NK Community")
                eb.timestamp = datetime.now()
                await channel.send(embeds=eb)

    @slash_command(name="setup", description="mute setup")
    @slash_default_member_permission(Permissions.ADMINISTRATOR)
    async def setup(self, ctx:InteractionContext):
        role = await ctx.guild.fetch_role(993305749763661875)
        guild = ctx.guild
        for channel in guild.channels:
            await channel.add_permission(target=role, deny=[Permissions.SEND_MESSAGES])
        await ctx.send("done")

    @slash_command(name="unmute", description="Einen User entmuten")
    @slash_default_member_permission(Permissions.MOVE_MEMBERS)
    @slash_option(
        name="user",
        description="User angeben",
        required=True,
        opt_type=OptionTypes.USER,
    )
    @slash_option(
        name="grund",
        description="Grund angeben",
        required=True,
        opt_type=OptionTypes.STRING
    )
    async def unmute(self, ctx:InteractionContext, user, grund):
        rolle = await ctx.guild.fetch_role(993305749763661875)
        if rolle not in user.roles:
            await ctx.send("User ist nicht gemuted")
        else:
            await user.remove_role(rolle)
            await ctx.send(f"<@{user.id}> wurde erfolgreich unmuted")
            channel = await self.bot.fetch_channel(993306264346050672)
            eb = naff.Embed(
                title="Mute Log",
                color="#f5b642",
                description=f"<@{ctx.author.id}> hat den User <@{user.id}> mit dem Grund **{grund}** entmuted",
            )
            eb.set_footer(text="NK Community")
            eb.timestamp = datetime.now()
            await channel.send(embeds=eb)


def setup(bot):
    mute_system(bot)
