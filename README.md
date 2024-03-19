# Repost-Telegram-Bot

Repost-Telegram-Bot is a Python-based tool for messages reposting in Telegram groups and channels.
Simplify content sharing with its easy-to-use interface and customizable features.

### How to get special `.env` keys

In the `.env.template` file you can find these keys:

```dotenv
BOT_TOKEN=

VK_APP_ACCESS_TOKEN=
VK_GROUP_ACCESS_TOKEN=

VK_GROUP_TAG=
VK_GROUP_ID=

TG_CHANNEL_ID=
```

- `BOT_TOKEN` - token of your Telegram bot.
- `VK_APP_ACCESS_TOKEN` - access token of your VK App.

  Open https://vk.com/dev, create the app and copy the id of your app.

- `VK_GROUP_ACCESS_TOKEN` - access token from your VK community.

  Just open your community page -> "Settings" -> "Working with the API".

  There you need open "Access keys" tab and create access token with necessary permissions.

  There you need open "Long Poll API" tab and configure Long Polling.

- `VK_GROUP_TAG` - tag of your VK community.

  Just open your community page and copy the last in url,
  e.g. `https://vk.com/example_commmunity`, the `example_commmunity` is the tag.

- `VK_GROUP_ID` - id of your VK community.

  Open this link below:
  ```url
  https://api.vk.com/method/groups.getById?group_id=<your_group_tag>&access_token=<vk_community_access_token>&v=<api_version>
  ```
  Replace `<your_group_tag>` with your community tag,
  `<vk_community_access_token>` with your access token from VK community,
  and `<api_version>` with API version that you selected in "Long Poll API" tab in VK community.

- `TG_CHANNEL_ID` - id of your Telegram channel of group.

  Open `@LeadConverterToolkitBot` bot and forward there any message from your channel or group,
  and you'll get id of your channel or group.

### How to Use:

1. Clone the repository to your local machine.
2. Install the necessary dependencies by running `make install`.
3. Create the `.env` file in the root of project and set all what are presented in the `.env.template` file.
4. Run the bot using `make run` and start interacting with it on Telegram.

### Docker

To run the repository using Docker and docker-compose,
run the following command to start the application using docker-compose:

```bash
docker-compose up -d
```
