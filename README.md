# DisboardAutoBumper
A Discord self bot that uses Fibo (Bump Remind bot) to know when to run /bump

> [!CAUTION]
> This uses a self bot. Self bots are against the TOS of Discord. Furthermore, auto bumping is against the TOS of Disboard.

# How to setup
First, add Fibo. This is the Bump Remind bot. https://top.gg/bot/735147814878969968
## Fibo commands
Take note of the channel you want to use /bump in. In said channel, do the following commands:

%setup add #channel-to-bump-in

#setup ping @YourSelfBot

I suggest you use a private channel due to the rules regarding this operation.

## Aquire the Discord User Token and Channel ID
Get the Discord token. There are many ways to do it, one of the easier ways is [this](https://www.geeksforgeeks.org/how-to-get-discord-token/). Once you do this, save the token for later.

Then get the channel ID of where you setup Fibo to remind in. You must [enable developer mode](https://www.howtogeek.com/714348/how-to-enable-or-disable-developer-mode-on-discord/) to do this. Once you enable developer mode, right click the channel that you setup Fibo to remind in and click Copy Channel ID, then save that for later.

## Running the self bot
I suggest you use the script on a computer running 24/7 for maximum bumping. Anywho, how to run:
```
pip install -r requirements.txt
python main.py
```
It will then ask you for the channel ID and the Discord token. We saved this from earlier, just paste it in. Once you do that, it will save both of that to ~/.disboardautobumper/ so you won't need to enter in the channel ID and Discord token again. If for whatever reason you must change the Discord token and/or channel ID, you can do that by editing the respective txt file in ~/.disboardautobumper

## More info
The self bot shouldn't bump right away, it should bump within 25-45 seconds after the bump remind ping goes through. This is on purpose, in attempt to not set off any alarms.
