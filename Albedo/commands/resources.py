import naff
from naff import Client, Intents, slash_command, InteractionContext, OptionTypes, slash_option, Extension, \
    slash_default_member_permission, Permissions, prefixed_command, PrefixedContext
import mysql.connector

class rsc(Extension):
    @prefixed_command(name="tlist")
    async def tierlist(self, ctx: PrefixedContext):
        channel = await self.bot.fetch_channel(1009961108670529666)
        embed = naff.Embed(title="Current SSR tier list",
                           description="Here you will find a SSR tier list collected from various sources",
                           color="#800080")
        embed.add_field(name="S-Tier | Currently Meta", value="Nemesis | Utility (Very important, 1* Mandatory), King | Shieldbreaker (1* Important, Will be replaced later by Claudia), Samir | DPS")
        embed.add_field(name="A-Tier | Need atleast 1*", value="Cocoritter | Utility, Meryl | Shieldbreaker / Tank, Tsubasa | DPS, Huma | Tank")
        embed.add_field(name="B-Tier | Need high investment", value="Crow(3 Star) | DPS, Shiro(3 Star) | Sub DPS, Zero(3 Star | Utility")
        embed.add_field(name="---------------------", value="If you disagree with this tier list, feel free to DM <@447000659871662081>")
        embed.set_footer(text="The Great Tomb of Nazarick")
        await channel.send(embeds=embed)
        await ctx.reply("Done")

    @slash_command(name="tierlist", description="Get the current tier list")
    async def tier_list(self, ctx: InteractionContext):
        embed = naff.Embed(title="Current SSR tier list",
                           description="Here you will find a SSR tier list collected from various sources",
                           color="#800080")
        embed.add_field(name="S-Tier | Currently Meta", value="Nemesis | Utility (Very important, 1* Mandatory), King | Shieldbreaker (1* Important, Will be replaced later by Claudia), Samir | DPS")
        embed.add_field(name="A-Tier | Need atleast 1*", value="Cocoritter | Utility, Meryl | Shieldbreaker / Tank, Tsubasa | DPS, Huma | Tank")
        embed.add_field(name="B-Tier | Need high investment", value="Crow(3 Star) | DPS, Shiro(3 Star) | Sub DPS, Zero(3 Star | Utility")
        embed.add_field(name="---------------------", value="If you disagree with this tier list, feel free to DM <@447000659871662081>")
        embed.set_footer(text="The Great Tomb of Nazarick")
        await ctx.send(embeds=embed)


    @prefixed_command(name="teams")
    async def teams(self, ctx: PrefixedContext):
        channel = await self.bot.fetch_channel(1009961108670529666)
        embed = naff.Embed(title="Current Best Teams",
                           description="Here you will find the best teams currently available",
                           color="#800080")
        embed.add_field(name="DPS Team", value="Samir, King, Nemesis\n"
                                               "Optionals: Crow / Tsubasa -> Samir")
        embed.add_field(name="Support Teams", value="Nemesis or Cocoritter, Zero, Samir or Shiro\n")
        embed.add_field(name="Tank Team", value="Huma, Meryl, Nemesis or King\n")
        embed.set_footer(text="The Great Tomb of Nazarick")
        await channel.send(embeds=embed)
        await ctx.reply("Done")


def setup(bot):
    rsc(bot)