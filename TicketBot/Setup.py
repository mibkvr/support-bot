import discord

from TicketBot import TicketConfig


class Setup:
    client = None
    config: TicketConfig = None

    def __init__(self, client, config: TicketConfig):
        self.client = client
        self.config = config

    async def on_message(self, message: discord.Message):
        arg = message.content.split(" ")[1]

        if not message.author.guild_permissions.administrator:
            return

        if arg == "support_category":
            self.config.support_category_id = message.channel.category_id
            self.config.updateConfig()
            await message.delete()

        elif arg == "support_channel":
            support_message = await message.channel.send(self.config.support_channel_message_text)
            self.config.support_message_id = support_message.id
            await support_message.add_reaction('❓')
            await message.delete()

        elif arg == "team_id":
            id = message.content.split(" ")[2]
            self.config.team_role_id = int(id)
            self.config.updateConfig()
            await message.delete()
