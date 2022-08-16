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
        database="albedo",
    )
    cursor = db.cursor()
    return db



class mute_system(Extension):
    @slash_command(name="mute", description="Mute a User")
    @slash_default_member_permission(Permissions.MOVE_MEMBERS)
    @slash_option(
        name="user",
        description="Use",
        required=True,
        opt_type=OptionTypes.USER,
    )
    @slash_option(
        name="dur",
        description="Duration",
        required=True,
        opt_type=OptionTypes.STRING
    )
    @slash_option(
        name="rs",
        description="Reason",
        required=True,
        opt_type=OptionTypes.STRING
    )
    async def mute(self, ctx:InteractionContext, user, dur, rs=None):
        guild = ctx.guild
        rolle = await ctx.guild.fetch_role(1008150035038490625)
        time_convert = {"s":1, "m":60, "h":3600, "d":86400, "w":604800, "mo":18144000, "y":31536000}
        tempmute= int(dur[:-1]) * time_convert[dur[-1]]
        channel = await self.bot.fetch_channel(1008146194024898620)
        dbmute = datetime.now() + timedelta(seconds=tempmute)
        db = await ConnectQuery()

        if user.has_role(rolle):
            await ctx.send("User is already muted")
        else:
            embed = naff.Embed(
                title="Muted",
                color="#f5b642",
                description=f"<@{user.id}> got muted for **{dur}**",
            )
            embed.set_footer(text="NK Community")
            embed.timestamp = datetime.now()
            await ctx.send(embeds=embed)
            eb = naff.Embed(
                title="Mute Log",
                color="#f5b642",
                description=f"<@{ctx.author.id}> muted the user <@{user.id}> because **{rs}** for {dur}",
            )
            eb.set_footer(text="The Great Tomb of Nazarick")
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
        guild = self.bot.get_guild(1007597560296382475)
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM mute WHERE dauer <= '{datetime.now()}'")
        users = cursor.fetchall()
        rolle = await guild.fetch_role(1008150035038490625)
        for user in users:
            if user[2] is not None:
                usr = await self.bot.fetch_member(user[1], 1007597560296382475)
                await usr.remove_role(rolle)
                dlt = "DELETE FROM mute WHERE discordid = {0}".format(user[1])
                cursor.execute(dlt)
                db.commit()
                db.close()
                channel = await self.bot.fetch_channel(1008150891033002095)
                eb = naff.Embed(
                    title="Automod Log",
                    color="#800080",
                    description=f"<@{usr.id}> was unmuted \n"
                                f"**Reason:** Mute expired",
                )
                eb.set_footer(text="The Great Tomb of Nazarick")
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

    @slash_command(name="unmute", description="Unmute a User")
    @slash_default_member_permission(Permissions.MOVE_MEMBERS)
    @slash_option(
        name="user",
        description="User",
        required=True,
        opt_type=OptionTypes.USER,
    )
    @slash_option(
        name="rs",
        description="Reason",
        required=True,
        opt_type=OptionTypes.STRING
    )
    async def unmute(self, ctx:InteractionContext, user, rs):
        rolle = await ctx.guild.fetch_role(1008150035038490625)
        if rolle not in user.roles:
            await ctx.send("User is not muted")
        else:
            await user.remove_role(rolle)
            await ctx.send(f"<@{user.id}> sucessfully got unmuted")
            channel = await self.bot.fetch_channel(1008146194024898620)
            eb = naff.Embed(
                title="Mute Log",
                color="#800080",
                description=f"<@{ctx.author.id}> unmuted the User <@{user.id}> \n"
                            f"Reason: **{rs}**",
            )
            eb.set_footer(text="The Great Tomb of Nazarick")
            eb.timestamp = datetime.now()
            await channel.send(embeds=eb)


def setup(bot):
    mute_system(bot)
