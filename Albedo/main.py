from naff import Client, Intents, Permissions, InteractionContext, OptionTypes, listen, const, Activity, ActivityType, slash_command, slash_option, slash_default_member_permission
import logging
import os
import config
import naff
bot = Client(intents=Intents.ALL, sync_interactions=True, asyncio_debug=True, default_prefix=("!"))


logging.basicConfig()
cls_log = logging.getLogger(naff.const.logger_name)
cls_log.setLevel(logging.DEBUG)



@listen()  # this decorator tells snek that it needs to listen for the corresponding event, and run this coroutine
async def on_ready():
    # This event is called when the bot is ready to respond to commands
    print("Ready")
    print(f"This bot is owned by {bot.owner}")
    await bot.change_presence(activity=Activity(type=ActivityType.WATCHING, name=f"The Great Tomb of Nazarick"))
@listen()
async def on_member_add(event):
    channel = await bot.fetch_channel(1007597562607452190)
    await channel.send(f"Welcome {event.member.mention} to the Great Tomb of Nazarick!")
    await event.member.add_role(1007597560296382478)

"""@listen()
async def on_member_remove(event):
    channel = await bot.fetch_channel(488299594762027008)
    await channel.send(f"{event.member.mention} uns verlassen")"""

for file in os.listdir("./logs"):
    if file.endswith(".py"):
        bot.load_extension(f'logs.{file[:-3]}')

for file in os.listdir("./commands"):
    if file.endswith(".py"):
        bot.load_extension(f'commands.{file[:-3]}')

for file in os.listdir("./automod"):
    if file.endswith(".py"):
        bot.load_extension(f'automod.{file[:-3]}')

for file in os.listdir("./moderation"):
    if file.endswith(".py"):
        bot.load_extension(f'moderation.{file[:-3]}')

@slash_command(name="reload", description="Reload a Cog")
@slash_default_member_permission(Permissions.ADMINISTRATOR)
@slash_option(
    name = "cog",
    description = "Cog",
    required = True,
    opt_type = OptionTypes.STRING

)
async def reload(ctx: InteractionContext, cog):
    if ctx.author.id == 447000659871662081:
        for file in os.listdir(f"./{cog}"):
            if file.endswith(".py"):
                bot.reload_extension(f'{cog}.{file[:-3]}')
        await ctx.send(f"{cog} sucessfully reloaded")
    else:
        await ctx.send("You have no permissions to run this command.")

bot.start(config.token)