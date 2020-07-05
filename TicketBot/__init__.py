import datetime

import discord
from discord.utils import get

from TicketBot.Config import TicketConfig


class TicketBot(discord.Client):
    config: TicketConfig = None

    async def on_ready(self):
        self.config = TicketConfig()
        print("Bot Ready")

    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        if payload.member == self.user:
            return

        if payload.message_id == TicketConfig.support_message:
            guild = self.get_guild(payload.guild_id)
            category = guild.get_channel(TicketConfig.support_category)

            ticket_channel: discord.channel.TextChannel = await guild.create_text_channel(
                "support-ticket-" + str(datetime.datetime.now().timestamp()), category=category)

            await ticket_channel.set_permissions(payload.member, send_messages=True, read_messages=True,
                                                 embed_links=True, send_tts_messages=True, attach_files=True,
                                                 read_message_history=True)

            role = get(guild.roles, id=TicketConfig.team_role_id)
            await ticket_channel.set_permissions(role, send_messages=True, read_messages=True,
                                                 embed_links=True, send_tts_messages=True, attach_files=True,
                                                 read_message_history=True)

            message = await ticket_channel.send(TicketConfig.support_channel_message_text)
            self.config.add_support_stats(message.author.id)

    async def on_message(self, message: discord.Message):
        if message.author == self.user:
            return
        elif message.content.startswith(".close_ticket"):
            for i in message.author.roles:
                if TicketConfig.team_role_id == i.id:
                    if message.channel.category_id == TicketConfig.support_category:
                        await message.channel.delete()
