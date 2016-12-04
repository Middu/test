import discord
from discord.ext import commands
from time import sleep


me = commands.Bot(command_prefix='.', self_bot=True)


@me.event
async def on_ready():
    print("----------")
    print("Logged in as:")
    print("    "+str(me.user.name))
    print("    "+str(me.user.id))
    print("----------")


def makeEmbed(*, name=None, icon=None, colour=0xDEADBF, values={}):
    '''Creates an embed messasge with specified inputs'''

    # Create an embed object with the specified colour
    embedObj = discord.Embed(colour=colour)

    # Set the author and URL
    embedObj.set_author(name=name, icon_url=icon)

    # Create all of the fields
    for i in values:
        if values[i] == '':
            values[i] = 'None'
        embedObj.add_field(name=i, value='{}'.format(values[i]))

    # Return to user
    return embedObj


@me.event 
async def on_message(message):
    if message.author.id == me.user.id and message.server.id == '140847179043569664':
        if len(message.embeds) > 0:
            return
        pass
    else:
        return

    actualDict = {}
    name = message.clean_content

    actualObj = makeEmbed(name=name, icon=me.user.avatar_url, values=actualDict)
    sleep(0.4)
    await me.edit_message(message, '  ', embed=actualObj)



token = "UserToken"
me.run(token, bot=False)
