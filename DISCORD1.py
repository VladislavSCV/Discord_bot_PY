import disnake

from disnake.ext import commands

bot = commands.Bot(command_prefix="!", intents=disnake.Intents.all())


@bot.slash_command()
async def test(interaction: disnake.AppCmdInter):
    await interaction.send("Привет, меня зовут Anton!")

bot.run("MTAzMDg2Njg1MzI2MzgzOTM5Mw.Gbu_hZ.-bbYygtV4eNNI2S5w9gG13mjLZ6A08_WSu4yLw")