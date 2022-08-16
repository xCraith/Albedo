import datetime
from datetime import datetime

import naff
from naff import Client, Intents, listen, Extension, guild

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

class autorole(Extension):
    @listen()
    async def on_member_update(self, event):
        guild = self.bot.get_guild(1007597560296382475)
        db = await ConnectQuery()
        gmember = await guild.fetch_role(1007597560296382480)
        vmember = await guild.fetch_role(1007597560296382481)
        pl = await guild.fetch_role(1007597560376066129)
        go = await guild.fetch_role(1007597560376066130)
        gd = await guild.fetch_role(1007597560296382482)
        fm = await guild.fetch_role(1007597560376066131)
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM autorole WHERE discordid = '{event.after.id}'")
        users = cursor.fetchall()
        print(users)
        for user in users:
            if event.after.has_role(gmember):
                await event.after.edit_nickname(new_nickname=f"⊰Member⊱ {user[2]}")
            elif event.after.has_role(vmember):
                await event.after.edit_nickname(new_nickname=f"⊰Vet. Member⊱ {user[2]}")
            elif event.after.has_role(pl):
                await event.after.edit_nickname(new_nickname=f"⊰Pleiades⊱ {user[2]}")
            elif event.after.has_role(go):
                await event.after.edit_nickname(new_nickname=f"⊰Officer⊱ {user[2]}")
            elif event.after.has_role(gd):
                await event.after.edit_nickname(new_nickname=f"⊰Guardian⊱ {user[2]}")
            elif event.after.has_role(fm):
                await event.after.edit_nickname(new_nickname=f"⊰Fo. Member⊱ {user[2]}")


def setup(bot):
    autorole(bot)

