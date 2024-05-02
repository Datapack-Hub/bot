<!-- # Datapack Helper
repo for the datapack helper discord bot :)
readme placholder -->

# 🤖 Datapack Hub Helper Bot

[![GitHub License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE.md)
[![Discord Server](https://img.shields.io/discord/935560260725379143?color=7289DA&label=Discord&logo=discord)](https://discord.datapackhub.net/)
[![GitHub Issues](https://img.shields.io/github/issues/Datapack-Hub/bot)](https://github.com/Datapack-Hub/bot/issues)

## Contributing

Contributions to this project are welcome! If you have ideas for new features, improvements, or bug fixes, please feel free to create a pull request. Be sure to review our contribution guidelines before getting started.

### Develop Locally

1. Clone the repo and navigate to it using a terminal
2. Install the dependencies using:
   ```bash
   pip install -r requirements.txt
   ```
   > You may need to use `pip3` instead of `pip`
3. Go to https://discord.com/developers/applications, create and set up a bot and invite it to a server
4. Create a file in the root directory called `bot_token.py` and fill in your token:
   ```py
   token = "<DISCORD_BOT_TOKEN>"
   ```
5. Create a file in the root directory called `variables.py` and fill it with ids of your bot and channels:
   ```py
   full_path = "<file path to folder with bot>"
   bot_id = <bot's discord id>

   # GUILDS
   main_guild = <main guild the bot will be active in>

   # CHANNELS
   logs_channel = <log channel id>

   # ROLES
   special_commands_roles = [<ids of roles that can run `>.<` commands>]
   ```
6. Start the bot using:
   ```bash
   python main.py
   ```
   > You may need to use `python3` instead of `python`

## Support and Issues

If you encounter any issues or have questions about using the Datapack Hub Helper Bot, please check our [FAQ](https://discord.datapackhub.net/faq) for common solutions. If your issue persists or you need further assistance, you can open an issue on our [GitHub repository](https://github.com/Datapack-Hub/bot/issues).

## License

This project is licensed under the [MIT License](LICENSE.md).
