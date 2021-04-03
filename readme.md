# minecraft-bot

Telegram bot for Minecraft Bedrock edition hosted on a dedicated server for delivering messages when player connects or disconnects from the server

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
sudo pip install -r requirements.txt
```

Clone the repository to Minecraft Bedrock Dedicated server. This only supports the [Ubuntu](https://www.minecraft.net/en-us/download/server/bedrock/) server.

```bash
git clone https://github.com/v3se/minecraft_bot.git
```

## Usage

Add your Telegram bot token to minebot.py. If you haven't created a bot before, take a look at this [documentation](https://core.telegram.org/bots#6-botfather)

```python
updater = Updater(token='<add-token>')
```

You will need to redirect the server stdout and stderr to a file to use this bot. If you are running the server in a [screen](https://linux.die.net/man/1/screen), you can redirect these to a file using the -L switch. If you are running in docker container then logs can be found from _/var/lib/docker/containers/<container_id>/<container_id>-json.log_

Run the script

```bash
python3 minebot.py <logfile_name>
```

Issue the /start command to the bot in Telegram and try to login to the server. You should see a message:

```bash
Player connected: <player_name>, xuid: <xuid>
```
