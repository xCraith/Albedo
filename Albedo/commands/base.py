import naff
from naff import Client, Intents, slash_command, InteractionContext, OptionTypes, slash_option, Extension, \
    slash_default_member_permission, Permissions, prefixed_command, PrefixedContext
import mysql.connector

async def ConnectQuery():
    db = mysql.connector.connect(
        host="localhost",
        user="main",
        password="vT69Ij9KiDlpfL6R",
        database="albedo",
    )
    cursor = db.cursor()
    return db





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


    @slash_command(name="nickname", description="Set your Nickname")
    @slash_option(name="name", description="Your nickname", required=True, opt_type = OptionTypes.STRING)
    async def set_nickname(self, ctx:InteractionContext, name):
        db = await ConnectQuery()
        cursor = db.cursor()
        await ctx.author.edit_nickname(new_nickname=f"{name}")
        await ctx.send("Sucessfully changed your nickname!")
        sql = "INSERT INTO autorole (discordid, nick) VALUES (%s, %s)"
        val = (ctx.author.id, name)
        cursor.execute(sql, val)
        db.commit()
        db.close()


    @prefixed_command(name="readfirst")
    async def readfirst(self, ctx: PrefixedContext):
        channel = await self.bot.fetch_channel(1009960972468891781)
        embed = naff.Embed(title="Informations",
                           description="Welcome everyone to the Great Tomb of Nazarick! \n"
                                       "In here you will find some useful informations about us and the game! \n"
                                       "Please do /nickname in <#1007597562791993347> and set your name so you automatically get the prefix accordingly to your current rank in the crew \n"
                                       "Make sure to read the rules after you read through this post. \n"
                                       "In <#1007597562607452191> you can get yourself some roles!",
                           color="#800080")
        embed.add_field(name="About us", value="The Crew 'Ainz Ooal Gown' was founded right after the release of the game with the goal to provide a small, friendly, nice and chill community to find some players to play with \n"
                                                     "The theme of our crew is based on the anime overlord, so is also the discord server")
        embed.add_field(name="Helpful resources", value="In <#1009961108670529666> You can find some resources like tier lists, guides and much more!")
        embed.add_field(name="Tips and Tricks", value="In <#1009961188559429642> You will find some useful tricks and some tips to make your life easier.")
        embed.add_field(name="Commands", value="/nickname | Set your nickname and add yourself to the database \n"
                                               "/tierlist | To get a tier list of the best SSRs currently available in the game \n"
                                               "/teams | To get a list of the best team currently available")
        embed.set_footer(text="The Great Tomb of Nazarick")
        await channel.send(embeds=embed)
        await ctx.reply("Done")

    @prefixed_command(name="resources")
    async def resources(self, ctx: InteractionContext):
        channel = await self.bot.fetch_channel(1009961108670529666)
        embed = naff.Embed(title="Helpful resources",
                           description="In here you will find helpful resources to make your life in ToF easier!",
                           color="#800080")
        embed.add_field(name="Interactive Maps", value="To make sure you will find everything on the map we recommend using a interactive map\n"
                                                       "https://genshin.gg/tof/map/ \n"
                                                       "https://toweroffantasy.interactivemap.app/?map=1")
        embed.add_field(name="How to unlock more vehicles", value="https://genshin.gg/tof/mounts/")
        embed.add_field(name="Farming guide", value="https://genshin.gg/tof/farming/")
        embed.add_field(name="Gifting guide", value="https://genshin.gg/tof/gifts/")
        embed.add_field(name="---------------------", value="If you want to add some stuff, feel free to send a DM to <@447000659871662081>")
        embed.set_footer(text="The Great Tomb of Nazarick")
        await channel.send(embeds=embed)
        await ctx.reply("Done")
#



def setup(bot):
    BaseCommands(bot)