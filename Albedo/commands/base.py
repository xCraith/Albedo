import naff
from naff import Client, Intents, slash_command, InteractionContext, OptionTypes, slash_option, Extension, \
    slash_default_member_permission, Permissions

"""async def ConnectQuery():
    db = mysql.connector.connect(
        host="localhost",
        user="main",
        password="vT69Ij9KiDlpfL6R",
        database="bot",
    )
    cursor = db.cursor()
    return db"""





bot = Client(intents=Intents.ALL)
# intents are what events we want to receive from discord, `DEFAULT` is usually fine

class BaseCommands(Extension):
    @slash_command(name="addrole", description="Add a Role to someone ")
    @slash_option(
        name = "user",
        description = "User angeben",
        required = True,
        opt_type = OptionTypes.USER

    )
    @slash_option(
        name = "role",
        description = "Rolle angeben",
        required = True,
        opt_type = OptionTypes.ROLE

    )
    @slash_default_member_permission(Permissions.BAN_MEMBERS)
    async def add_role(self, ctx: InteractionContext, user, role):
        rollenliste = [923791176312705104, 711530678994599946, 923821659012616192, 989669817176952893, 923801431511822366, 780016923852144680]
        if role.id in rollenliste:
            await ctx.send("Du kannst diese Rolle nicht über diesen Command hinzufügen")
        else:
            embed = naff.Embed(
            title="Addrole",
            color="#800080",
            description=f"<@{user.id}> was added the role <@&{role.id}>"

        )
            embed.set_footer(text="The Great Tomb of Nazarick")
            await user.add_role(role)
            await ctx.send(embeds=embed)
            channel = await self.bot.fetch_channel(1008146242800468089)
            eb = naff.Embed(
            title="Addrole Logs",
            color="#800080",
            description=f"<@{ctx.author.id}> has added <@{user.id}> the role <@&{role.id}>"
            )
            embed.set_footer(text="The Great Tomb of Nazarick")
            await channel.send(embeds=eb)


def setup(bot):
    BaseCommands(bot)