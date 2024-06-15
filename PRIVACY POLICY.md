# Privacy Policy
====================

Last updated: May 15, 2024

## Stored Information
The bot may automatically store the `server id` of any server it gets added to.

## Data Removal
### Automatic
A server's `id` is automatically removed from the bots storage once it gets removed from that server.

### Manual
Members with the `manage_guild` permission can manually remove a server's `id` by running the `/highlighter` Discord slash command and clicking the "Disable" button. In case that button doesn't show up, the bot isn't currently storing that server's `id`.

## Data Usage
The bot uses the stored server `id`'s to figure out whether detected messages were sent in a server with the bot's `mcfunction` syntax highlighting function enabled. No usage of data outside of the aforementioned cases will happen and the data is not shared with any 3rd-party site or service.

The bot also has access to any message sent in any discord server it is in. (As far as permissions allow it to, it can't access messages in channels it can't view.) That data is NOT stored and only used to make the `MCfunction` syntax highlighting work. This requires the message content to be acessible to the bot so it can recognise messages as using `MCfunction` as programming language within a code block and for it to resend a highlighted version of that message afterwards.
