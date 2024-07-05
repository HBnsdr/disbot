import discord
from discord.ext import commands


class MyBot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(command_prefix="!", intents=discord.Intents.all())

    async def setup_hook(self) -> None:
        await self.tree.sync()

    async def on_ready(self) -> None:
        print("Je suis en ligne")

bot = MyBot()

@bot.tree.command(name="commande_test", description="Un exemple de commande slash")
async def test_command(interaction : discord.Interaction):
    author = interaction.user
    await interaction.response.send_message("Oui ? Que puis-je faire pour toi ?")

if __name__ == "__main__":
    bot.run("MjQ1NTg2NTg5MjQ4NTIwMTky.Gh7hNl.O17f4Ei6FLsSaVV4S8YfqlRBgQYfqb3XO1k-7s")



