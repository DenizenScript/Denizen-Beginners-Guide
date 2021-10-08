Denizen and Discord: dDiscordBot
--------------------------------

```eval_rst
.. contents:: Table of Contents
    :local:
```

### Introduction

dDiscordBot is an **addon plugin** for Denizen that provides commands, script events, and tags for interacting with the Discord API. Basically, you can create a functioning Discord bot directly within Denizen!

### What Can It Do?

There are many libraries for various different programming languages for the Discord API. You might be familiar with some, such as [discord.js](https://discord.js.org), [discord.py](https://discordpy.readthedocs.io/en/stable/), and [JDA](https://github.com/DV8FromTheWorld/JDA). These libraries aim to cover **all aspects** of the API.

Denizen is for Minecraft servers. Accordingly, dDiscordBot provides utilities that would be useful for a Minecraft server to interact with Discord. Nevertheless, some of the things you can do are:

- Send, receive, and reply to messages
  - Attach files, embeds, and buttons
- Manage and reply to slash commands
- Manage roles

...and much more.

### What Can It Be Used For?

Many Minecraft servers have Discord communities. They provide a social space outside of the game itself. Discord users might want to interact with the online Minecraft players, and vice versa. 

The main uses might be an account linker, which verifies a Discord user with their player on the server, and a chat bridge between Discord and Minecraft. You might also relay announcements, host cross-platform events, and let Discord users query data from the server.

### Creating a Bot

There are enough tutorials out there for creating a bot account. [Here's a handy one](https://discordpy.readthedocs.io/en/stable/discord.html).

### Logging In

To log in using dDiscordBot, use the `discordconnect` command. **Don't hardcode your token into the script!** Use a separate tokenfile placed outside of the `scripts` folder. A common location for this is in `Denizen/data`.

The `discordconnect` command takes an `id` argument. This can be anything, and it identifies the connection to the bot user. Almost all Discord commands take this argument, and it must be the same for a specified connection.

Note that you only need to connect once after the server starts. Additionally, make sure to ~wait this command, as you should with all other Discord commands.

```dscript_green
connect_to_discord:
    type: world
    events:
        after server start:
        - ~discordconnect id:mybot tokenfile:data/tokenfile.txt
```

### Sending a Message

Now that you've logged in, you can send your first message. The `discordmessage` command has a `channel` argument, which is the Discord channel you want the bot to send the message in. It must be visible to the bot. You can use the channel's ID; if you don't know how to find it, [look here](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-).

Note that if you're going to use a channel or server's ID a lot, you should put it in a data script/flag it somewhere.

Here's how it would look in task form:

```dscript_blue
send_a_message:
    type: task
    script:
    - ~discordmessage id:mybot channel:(channel_id) "Hello, world!"
```

### Automatic Messaging

Let's make this automated! Using the `discord message received` event, you can detect when a Discord user sends a message and run commands based off the message content. You can also respond to the same channel they sent the message in! For example, if you wanted to respond to the user if their message includes "ping", you'd do:

```dscript_green
ping_pong:
    type: world
    events:
        on discord message received:
        - if <context.new_message.text.contains_text[ping]>:
            - ~discordmessage id:mybot channel:<context.new_message.channel> Pong!
```

![](https://media.discordapp.net/attachments/533123622093455362/894456615514808341/unknown.png)

### Chat Bridge

Now you've got the basic tools to make a chat bridge. In order for this to function, it needs to:

- send a message to a Discord channel when a Minecraft user chats
- narrate to the online Minecraft players when a Discord user sends a message in the channel

Let's tackle the first part. You can use the `player chats` event for this one. Then all you have to do is use the `discordmessage` command like in the first example. You should also include the Minecraft player's name in the message, otherwise the Discord users won't know who it's from.

Note that Discord text formatting uses [Markdown](https://www.markdownguide.org/cheat-sheet/) - Denizen formatting tags like `<bold>` won't work here.

```dscript_blue
chat_bridge:
    type: world
    events:
        on player chats:
        - define message "**<player.name>**: <context.message>"
        - ~discordmessage id:mybot channel:(channel_id) <[message]>
```

Great! Now for the next step. You can use the `discord message received` event like in the last example, but we only want to relay the message if it's in a certain channel. Luckily, this event comes equipped with a `channel` switch, which is exactly what we need. This time, we can use Denizen formatting tags.

Note that the received DiscordMessageTag doesn't only represent the message content: you can get the author, channel, id, and much more.

```dscript_blue
chat_bridge:
    type: world
    events:
    ...
        on discord message received channel:(channel_id):
        # ex: [Discord] <acikek> Hello!
        - define message "[<blue>Discord<&r>] <&lt><context.new_message.author.name><&gt> <context.new_message.text>"
        - announce <[message]>
```

### Slash Commands

Slash commands are Discord's new way for interacting with a bot upon request. They're builtin to the client, which means you can see the help for a command without external resources. They also show up in a list when you start a message with `/` - go ahead and try it!

![](https://media.discordapp.net/attachments/533123622093455362/894456778891333692/unknown.png)

With dDiscordBot, you can create your own slash commands. They belong to a feature set known as Interactions, along with buttons and selection menus.

**You only have to create a slash command once.** Creating a slash command of the same name updates the existing one.

When a user uses a slash command, you need to respond within just 5 seconds. However, that doesn't necessarily mean you have to send a message; instead, if you need more time, you can *defer* - or acknowledge - the request, which you can reply to later.

You can read further about slash command limitations [here](https://gist.github.com/MinnDevelopment/b883b078fdb69d0e568249cc8bf37fe9).

### Last-login Command

Let's make a slash command for a player's last login time. If the player is online, we should say that instead. First, you have to create the command. You can do so with the `discordcommand` command and the `create` argument. We want to take input from the user for the player name; this is called an option, and it needs to be attached to the command upon creation.

When creating a slash command, you can specify a server for it to be available to with the `group` argument. This is very useful for testing, even if you want it to be globally available in the future. **Registering a global command can take up to an hour!**

The `options` argument is a map of maps, where the values follow a certain format. You can view the map format on the [meta page](https://meta.denizenscript.com/Docs/Commands/discordcommand). It's recommended to use the `definemap` command for this. 

The `name` argument is required, and the `description` argument is optional, but it's useful for users. Let's throw everything into a task script:

```dscript_blue
create_lastlogin:
    type: task
    script:
    - definemap options:
        1:
            type: string
            name: player
            description: The Minecraft player's name
            required: true

    - ~discordcommand id:mybot create name:lastlogin "description:Displays a player's last login time." "group:<discord[mybot].group[My server]>" options:<[options]>
```

Once the command is created, you can use the `discord slash command` event to listen for uses. Be sure to use the `name` switch for the name of the command.

Using slash commands, buttons, and selection menus is called an interaction, and these are the things we have to acknowledge, as mentioned previously. You can handle this with the `discordinteraction` command, which has a required `interaction` argument. Note that this command **doesn't** need the `id` argument. All three corresponding events have a `<context.interaction>` tag.

It's good practice to defer the response even if the interaction isn't going to take long to respond to. Use the `defer` instruction to acknowledge, and the `reply` instruction to reply with a message. For now, just test out the usage with a Hello World:

```dscript_green
lastlogin:
    type: world
    events:
        on discord slash command name:lastlogin:
        - ~discordinteraction defer interaction:<context.interaction>
        - ~discordinteraction reply interaction:<context.interaction> "Hello, world!"
```

![](https://media.discordapp.net/attachments/533123622093455362/895888348634300456/unknown.png)

This command relies on dealing with the passed-in option. Since we set the `player` option to `required`, Discord doesn't allow the end user to use the slash command without supplying that string.

The `<context.options>` tag for the `discord slash command` event returns a MapTag of option names and their supplied values. Since you're guaranteed a `player` key in this case, you can safely get the value without any error checking.

Use this value in combination with `<server.match_offline_player>` (which does require error checking) to retrieve the player you want. If the server can't find the player, make sure to still let the Discord user know.

Next, you'll want to check if the player is online or offline, which you can do with the `PlayerTag.is_online` tag. If they are, you can just say so. If not, you can use the `PlayerTag.last_played_time` tag and format the returned TimeTag. You can use the formatting in the following script, or view the [meta doc](https://meta.denizenscript.com/Docs/Tags/timetag.format) for more info.

Make sure to include the player's name in the message! `<server.match_offline_player>` returns a *best match*, which doesn't have to be the player's actual name.

Here's the final script:

```dscript_green
lastlogin:
    type: world
    events:
        on discord slash command name:lastlogin:
        - ~discordinteraction defer interaction:<context.interaction>

        - define player <server.match_offline_player[<context.options.get[player]>].if_null[null]>

        - if <[player]> == null:
            - ~discordinteraction reply interaction:<context.interaction> "That player has never joined!"
            - stop

        - if <[player].is_online>:
            - ~discordinteraction reply interaction:<context.interaction> "**<[player].name>** is online!"
        - else:
            - define message "**<[player].name>** was last seen on **<[player].last_played_time.format[LLLL dd, yyyy]>** at **<[player].last_played_time.format[hh:mm a]>**"
            - ~discordinteraction reply interaction:<context.interaction> <[message]>
```

![](https://cdn.discordapp.com/attachments/894449781714346004/894449949708783656/Mv9QeGQ5DQ.gif)

### Buttons and Selection Menus

The rest of the interactions feature set includes buttons and selection menus, which are in their own category: *components*. Components can be attached to both interaction replies and basic messages (via the `rows` argument), and when used, return an interaction.

You can construct a `DiscordButtonTag with` `<discord_button>`. You can then attach properties using the `with[].as[]` tag. `DiscordSelectionTag` and `DiscordEmbedTag` also follow this paradigm.

You can view the supported properties for a button [here](https://meta.denizenscript.com/Docs/Tags/discordbuttontag.with.as) and for a selection menu [here](https://example.com).

The `rows` argument is a list of lists. The main lists represent the separate rows, while the lists inside represent the components on each row (similarly to columns on a grid). This argument is found on both `discordinteraction` and `discordmessage`. You can make use of `<list_single>` and `.include_single` for this. Additionally, you can mix and match components in rows as you please. However, a message is still required!

For example, sending a message with a button would look like:

```dscript_blue
buttons:
    type: task
    script:
    - define click_me "<discord_button.with[id].as[click_me].with[label].as[Click me!].with[style].as[success]>"
    - ~discordmessage id:mybot channel:(channel_id) rows:<list_single[<list_single[<[click_me]>]>]> Buttons!
```

The ID should be unique to the button: it's how you'll identify one button over another. You'll see this with the `discord button clicked` event, which has an `id` switch much like the slash command event's `name` switch. An example reply would look like:

```dscript_green
click_me:
    type: world
    events:
        on discord button clicked id:click_me:
        - ~discordinteraction defer interaction:<context.interaction>
        - ~discordinteraction reply interaction:<context.interaction> "Hello, <context.interaction.user.name>!"
```

![](https://media.discordapp.net/attachments/533123622093455362/895896247641190420/unknown.png)

Selection menus function in a similar way, although it's easier to see with an example script:

```dscript_blue
selection_menu:
    type: task
    script:
    # Similar to command options
    - definemap options:
        1:
            label: Good
            value: mood_good
            description: I'm doing well.
            emoji: 🙂
        2:
            label: Better
            value: mood_better
            description: I'm doing wonderfully!
            emoji: 😃
        3:
            label: Best
            value: mood_best
            description: I'm on top of the world!
            emoji: 🤩

    - define menu <discord_selection.with[id].as[mood_menu].with[options].as[<[options]>]>
    - ~discordmessage id:mybot channel:(channel_id) rows:<list_single[<list_single[<[menu]>]>]> "How are you today?"

mood_menu:
    type: world
    events:
        on discord selection used id:mood_menu:
        - ~discordinteraction defer interaction:<context.interaction>

        - choose <context.option.get[value]>:
            - case mood_good:
                - define message "I'm glad."
            - case mood_better:
                - define message "Wow, that's great!"
            - case mood_best:
                - define message "Downright incredible!"

        - ~discordinteraction reply interaction:<context.interaction> <[message]>
```

![](https://cdn.discordapp.com/attachments/533123622093455362/895890729530970132/eVkiFRrVa4.gif)
