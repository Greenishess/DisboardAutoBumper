import selfcord
import time
import random
import os
import glob
from colorama import *
just_fix_windows_console()

userToken = None
channelID = None

def startup():
    global userToken
    global channelID
    os.mkdir(os.path.expanduser("~/.disboardautobumper"))
    userToken = input("Please enter your USER token. " + Fore.YELLOW)
    channelID = input(Fore.RESET + "PLease enter the channelID where to auto bump. " + Fore.YELLOW)
    print(Fore.GREEN + "I will be saving this to " + os.path.abspath(os.path.expanduser("~/.disboardautobumper")) + ". If for whatever reason you need to change it, please change the contents of those files.")
    with open(os.path.expanduser("~/.disboardautobumper/token.txt"), "w") as tokentxt:
        tokentxt.write(userToken)
    with open(os.path.expanduser("~/.disboardautobumper/channel.txt"), "w") as channeltxt:
        channeltxt.write(channelID)

def useconfig():
    global userToken
    global channelID
    if os.path.exists(os.path.expanduser("~/.disboardautobumper/token.txt")) and os.path.exists(os.path.expanduser("~/.disboardautobumper/channel.txt")):
        with open(os.path.expanduser("~/.disboardautobumper/token.txt"), "r") as tokentxt:
            userToken = tokentxt.read()
        with open(os.path.expanduser("~/.disboardautobumper/channel.txt"), "r") as channeltxt:
            channelID = channeltxt.read()
    else: #this whole thing is probably anti user but idgaf at this point
        configs = glob.glob(os.path.expanduser("~/.disboardautobumper/*"))
        for config in configs:
            os.remove(config)
            startup()

if os.path.exists(os.path.expanduser("~/.disboardautobumper")):
    useconfig()
else:
    startup()

class client(selfcord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        
        if message.author.id == 735147814878969968 and self.user.mentioned_in(message): #735147814878969968 is the bump remind bot. You can add it at https://top.gg/bot/735147814878969968
            bot_was_mentioned = self.user.mentioned_in(message)
            if bot_was_mentioned:
                channel = self.get_channel(int(channelID))
                print("recived")
                commands = await channel.application_commands()
                for command in commands:
                    if command.name == "bump":
                        sleep_time = random.uniform(25, 45)
                        time.sleep(sleep_time)
                        await command(channel)

client = client()
client.run(userToken)
