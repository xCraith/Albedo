from naff import Client, Intents, slash_command, InteractionContext, OptionTypes, slash_option, Extension, \
    slash_default_member_permission, Permissions, Embed, prefixed_command, PrefixedContext, listen, Guild, Button, \
    ButtonStyles, ActionRow
import naff
from naff.api.events import Component
import datetime
from datetime import datetime


class selfroles(Extension):
    @slash_command(name="pronouns", description="Pronouns Selfroles")
    @slash_default_member_permission(Permissions.ADMINISTRATOR)
    async def ps(self, ctx: InteractionContext):
        channel = await self.bot.fetch_channel(1007597562607452191)
        embed = naff.Embed(
            title=f"Pronouns",
            color="#800080",
            description=f"Choose your preferred pronouns."
        )
        embed.set_footer(text="The Great Tomb of Nazarick")
        components: list[ActionRow] = [
            Button(
                style=ButtonStyles.PRIMARY,
                label="He/Him",
                custom_id="mal",
                emoji="<:male:1009173150598168616>"
            ),
            Button(
                style=ButtonStyles.DANGER,
                label="She/Her",
                custom_id="fem",
                emoji="<:female:1009173046013198397>"
            ),
            Button(
                style=ButtonStyles.SECONDARY,
                label="They/Them",
                custom_id="nog",
                emoji="<:trans:1009171590128349184>"
            )
        ]
        msg = await channel.send(embeds=embed, components=components)
        await ctx.send("done", ephemeral=True)

    @slash_command(name="combatroles", description="Combat Roles")
    @slash_default_member_permission(Permissions.ADMINISTRATOR)
    async def cr(self, ctx: InteractionContext):
        channel = await self.bot.fetch_channel(1007597562607452191)
        embed = naff.Embed(
            title=f"Combat Roles",
            color="#800080",
            description=f"Choose your preferred Combat Role."
        )
        embed.set_footer(text="The Great Tomb of Nazarick")
        components: list[ActionRow] = [
            Button(
                style=ButtonStyles.DANGER,
                label="DPS",
                custom_id="dps",
                emoji="<:dps:1009174674841817158>"
            ),
            Button(
                style=ButtonStyles.GREEN,
                label="Support",
                custom_id="sup",
                emoji="<:support:1009174673667407985>"
            ),
            Button(
                style=ButtonStyles.PRIMARY,
                label="Tank",
                custom_id="tank",
                emoji="<:tank:513823699431063574>"
            )
        ]
        msg = await channel.send(embeds=embed, components=components)
        await ctx.send("done", ephemeral=True)

    @listen()
    async def on_component(self, event: Component):
        guild = self.bot.get_guild(1007597560296382475)
        ctx = event.context
        if not ctx.author.has_role(1009164916323778624):
            await ctx.author.add_role(1009164916323778624)
        else:
            match ctx.custom_id:
                case "mal":
                    role = guild.get_role(role_id=1009165004613877820)
                    if ctx.author.has_role(role):
                        await ctx.author.remove_role(role)
                        await ctx.send("done", ephemeral=True)
                    else:
                        await ctx.author.add_role(role)
                        await ctx.send("done", ephemeral=True)

                case "fem":
                    role = guild.get_role(role_id=1009165061396385872)
                    if ctx.author.has_role(role):
                        await ctx.author.remove_role(role)
                        await ctx.send("Done", empehmeral=True)
                    else:
                        await ctx.author.add_role(role)
                        await ctx.send("done", ephemeral=True)

                case "dps":
                    role = guild.get_role(role_id=1009175620372136057)
                    if ctx.author.has_role(role):
                        await ctx.author.remove_role(role)
                        await ctx.send("done", ephemeral=True)
                    else:
                        await ctx.author.add_role(role)
                        await ctx.send("done", ephemeral=True)

                case "tank":
                    role = guild.get_role(role_id=1009175748629770301)
                    if ctx.author.has_role(role):
                        await ctx.author.remove_role(role)
                        await ctx.send("done", ephemeral=True)
                    else:
                        await ctx.author.add_role(role)
                        await ctx.send("done", ephemeral=True)

                case "sup":
                    role = guild.get_role(role_id=1009175878657392800)
                    if ctx.author.has_role(role):
                        await ctx.author.remove_role(role)
                        await ctx.send("done", ephemeral=True)
                    else:
                        await ctx.author.add_role(role)
                        await ctx.send("done", ephemeral=True)



def setup(bot):
    selfroles(bot)
#
