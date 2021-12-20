Handling Player Commands
------------------------

```eval_rst
.. contents:: Table of Contents
    :local:
```

### What Are Player Commands?

A player command is a command that a player types in chat to perform some unique task. This can range from fun user interactions to moderating tools and are found all over Minecraft. Denizen allows you to create custom player commands of your own to further enhance your server. This page will walk through making a basic warp command, a command that allows a user to set up points for others to teleport to. This is to illustrate how to make custom player commands as well as point out various features one should think about when making player commands.

### The Basic Structure

To start off, all custom commands in Denizen require the same basic structure. This is similar to the `task` scripts you have been seeing up until now, however with a few more required details:

```dscript_blue
ScriptContainerName:
    type: command
    name: [commandName]
    description: [a short description of your command]
    usage: [a description of the usage]
    script:
    - (commands here)
```

In addition to specifying the type of this script is `command`, you also need to provide the name of the command. This is what the user will be typing in chat to run the command. In addition you need to provide a description and a usage text. These are solely for the Spigot provided help command and otherwise have no functional use.

So let us start our command script by filling out the required fields:
```dscript_green
WarpCommand:
    type: command
    name: warp
    description: Warps you to magical places
    usage: /warp
    script:
    - narrate "This is where my command will go!"
```
Try it out in game by running `/warp`. This should just narrate out `This is where my command will go!`. Far from what we have set out to do, but our custom command does work in the sense it does something.

### Handling Player Arguments

A command is often much more than just the initial name. While some basic ones can be, often a command expects more details from the player. In our case with the warp command, we want to make warp points as well as travel to those points. For instance I might want to use `/warp create spawn` to make a new warp point called spawn. In this case `create` and `spawn` would be the arguments.

Similar to events, the command script has a few `context` tags that store some information about how the player used the command. One of these is `<context.args>` which contains a list of all the arguments the player used.

Let us give our command some functionality, namely creating new warp points and also being able to warp to those points:
```dscript_green
WarpCommand:
    type: command
    name: warp
    description: Warps you to magical places
    usage: /warp create|goto destination
    script:
    - define arg1 <context.args.get[1]>
    - if <[arg1]> == create:
        - define name <context.args.get[2]>
        - flag server warps.<[name]>:<player.location>
        - narrate "created warp <[name]>!"
    - else if <[arg1]> == goto:
        - define name <context.args.get[2]>
        - teleport <player> <server.flag[warps.<[name]>]>
        - narrate "warped to <[name]>!"
```
Try this out by doing `/warp create test` move away a bit and then `/warp goto test`. You will find yourself at that location you set the warp at.

To break down what's going on:
- We take a look at the first argument passed in
- If this argument is `create` create a flag on the server based on the second argument passed in
- Otherwise if that first argument is `goto` teleport the player to the location stored in the flag specified by the second argument

Notice we have now also updated the `usage` text. While this still doesn't provide any actual purpose to the script, it is good to keep the documentation accurate.

### Handling Player Player Arguments

A common feature of many commands is being able to do something to someone else, and as such you would need to pass in their name. For instance with our warp command we may want the functionality of being able to warp someone else instead of just yourself.

Let us say we want the command to look like `/warp player (player name) (destination)`. The resulting script would now look something like this:
```dscript_green
WarpCommand:
    type: command
    name: warp
    description: Warps you to magical places
    usage: /warp [(create|goto) destination] | [player name destination]
    script:
    - define arg1 <context.args.get[1]>
    - if <[arg1]> == create:
        - define destination <context.args.get[2]>
        - flag server warps.<[destination]>:<player.location>
        - narrate "created warp <[destination]>!"
    - else if <[arg1]> == goto:
        - define destination <context.args.get[2]>
        - teleport <player> <server.flag[warps.<[destination]>]>
        - narrate "warped to <[destination]>!"
    - else if <[arg1]> == player:
        - define playerName <context.args.get[2]>
        - define destination <context.args.get[3]>
        - define playerToWarp <server.match_player[<[playerName]>]>
        - teleport <[playerToWarp]> <server.flag[warps.<[destination]>]>
        - narrate "warped <[playerToWarp].name> to <[destination]>!"
```
Try this out on someone else on the server, or if this is local host you can test it by passing in your own name.

Notice we don't use the argument passed in directly for the teleport command, we instead used the tag `<server.match_player[]>` to find the player object of the given name. This is an important step - while there are some smart converts in denizen where you can just give the name of the thing and it will get the correct object (such as materials) this does not work with players. In addition, `<server.match_player[]>` allows for imprecise inputs, such as if there is someone named `bobby` on the server `<server.match_player[bob]>` would work <span class="parens">(assuming there was no one actually named `bob`)</span>.

### Adding Tab Completions

A nice way to enhance your command scripts is by adding tab completions, a way for Minecraft a method of auto-completing arguments. In order to accomplish this you would add the following:
```dscript_green
WarpCommand:
    type: command
    name: warp
    description: Warps you to magical places
    usage: /warp [(create|goto) destination] | [player name destination]
    tab completions:
        1: create|goto|player
        2: <context.args.get[1].equals[goto].if_true[<server.flag[warps].keys>].if_false[]>
        3: <context.args.get[1].equals[player].if_true[<server.flag[warps].keys>].if_false[]>
    script:
    #...nothing changed here
```
Try this out, while typing in the command see the Minecraft tab-complete menu pop up and see it in action.

What will happen is that while the player is typing the first argument, the suggestions `create`, `goto`, and `player` will be shown, with the one that is closely matched being highlighted.

While the player is typing the second argument, if the first argument is `goto` it will fetch all the keys stored in the warp flag, otherwise nothing will be suggested. A similar thing is done for the third argument, but checking if the first argument is `player`.

Something to keep in mind, tab completions does not provide any additional functionality to your script other than give suggestions to the player. You still need to write the rest of the script out to handle any arguments passed in.

### Don't Trust The Player

The script as is technically works fine, assuming everyone uses it properly - However, there is no grantee of that happening. This comes to an important topic: *never trust the player*. Do not assume the player will always do what you want them to do or expect them to do. There are a number of issues that can rise up from our simple command here such as:
- What if someone tries to goto a warp that doesn't exist?
- What if someone tries to create a warp that already exists?
- What if someone forgot to put in arguments?
- What if someone put in too many arguments?
- What if someone gives an invalid argument?
- What if the player you specified doesn't exist?

While some issues may simply be mostly harmless <span class="parens">(such as providing too many arguments)</span>, some may cause errors in the script <span class="parens">(such as the warp not existing)</span>, or ruin something else <span class="parens">(such as creating a warp that already existed)</span>. For all of these cases, it is important that you catch these player errors to make sure everything is as smooth as possible for everyone.

Let us now see what our script would look like with having error checking
```dscript_green
WarpCommand:
    type: command
    name: warp
    description: Warps you to magical places
    usage: /warp [(create|goto) destination] | [player name destination]
    tab completions:
        1: create|goto|player
        2: <context.args.get[1].equals[goto].if_true[<server.flag[warps].keys.if_null[]>].if_false[]>
        3: <context.args.get[1].equals[player].if_true[<server.flag[warps].keys.if_null[]>].if_false[]>
    script:
    - if <context.args.is_empty>:
        - narrate "you didn't give any arguments!"
        - stop

    - define arg1 <context.args.get[1]>
    - if <[arg1]> == create:
        - if <context.args.size> < 2:
            - narrate "you need to give the warp a name"
            - stop
        - else if <context.args.size> > 2:
            - narrate "you provided too many arguments"
            - stop
        - define name <context.args.get[2]>
        - if <server.has_flag[warps.<[name]>]>:
            - narrate "A warp already exists with the name of <[name]>!"
            - stop
        - flag server warps.<[name]>:<player.location>
        - narrate "created warp <[name]>!"
    - else if <[arg1]> == goto:
        - if <context.args.size> < 2:
            - narrate "you need to specify where to warp to"
            - stop
        - else if <context.args.size> > 2:
            - narrate "you provided too many arguments"
            - stop
        - define name <context.args.get[2]>
        - if !<server.has_flag[warps.<[name]>]>:
            - narrate "No warp by <[name]> exists!"
            - stop
        - teleport <player> <server.flag[warps.<[name]>]>
        - narrate "warped to <[name]>!"
    - else if <[arg1]> == player:
        - if <context.args.size> < 3:
            - narrate "you need to specify a player and where to warp to"
            - stop
        - else if <context.args.size> > 3:
            - narrate "you provided too many arguments"
            - stop
        - define playerName <context.args.get[2]>
        - define destination <context.args.get[3]>
        - define playerToWarp <server.match_player[<[playerName]>].if_null[null]>
        - if <[playerToWarp]> == null:
            - narrate "Can't find player by name <[playerName]>"
            - stop
        - teleport <[playerToWarp]> <server.flag[warps.<[destination]>]>
        - narrate "warped <[playerToWarp].name> to <[destination]>!"
    - else:
        - narrate "Unknown argument <[arg1]>"
```
Try this out now with intentionally providing bad inputs and watch the command stop you.

Some safety measurements that are used here:
- Checking the size of the argument list to verify that the player actually typed in that argument
- Checking to see if the server does or does not have the flag to make sure there are no conflicts
- Stopping the script if any issue is detected as well as letting the user know what's wrong
- Added a null check to the tab completions for the case there is no warps denizen will not display errors
- Added a null check to the match_player tag to verify if that player actually exists

While the size of the script has greatly increased, this is a necessary step for commands and for player interfaces in general.
You can read more about this in [the Common Mistakes page](/guides/troubleshooting/common-mistakes.html#don-t-trust-players).

### Wait, Can I See Your Permissions?

In addition to simply verifying whether or not the player has inputted the argument correctly, you also want to make sure that the player has permission to use the command. By default Minecraft doesn't have a permission system (beyond setting players to op), however there are a number of permission plugins that exist to help manage these.

A simple way to add permission checking is by locking the whole command with a permission, letting Spigot handle it at that step. Adding this permission would look something like this:
```dscript_green
WarpCommand:
    type: command
    name: warp
    description: Warps you to magical places
    usage: /warp [(create|goto) destination] | [player name destination]
    permission: warps.use
    tab completions:
        1: create|goto|player
        2: <context.args.get[1].equals[goto].if_true[<server.flag[warps].keys.if_null[]>].if_false[]>
        3: <context.args.get[1].equals[player].if_true[<server.flag[warps].keys.if_null[]>].if_false[]>
    script:
    #...nothing changed here
```

In the example here, if the player does not have the `warps.use` permission Spigot will stop them from using the command. It is generally recommended to add such a permission to any custom command, even if you plan for it to be used by anyone.

However, sometimes you need a bit more permission testing in the script - for instance we may want people in general to use the warps but not make any new ones or force other players to warp. Adding such a permission check may look something like:
```dscript_green
WarpCommand:
    type: command
    name: warp
    description: Warps you to magical places
    usage: /warp [(create|goto) destination] | [player name destination]
    permission: warps.use
    tab completions:
        1: create|goto|player
        2: <context.args.get[1].equals[goto].if_true[<server.flag[warps].keys.if_null[]>].if_false[]>
        3: <context.args.get[1].equals[player].if_true[<server.flag[warps].keys.if_null[]>].if_false[]>
    script:
    - if <context.args.is_empty>:
        - narrate "you didn't give any arguments!"
        - stop

    - define arg1 <context.args.get[1]>
    - if <[arg1]> == create:
        - if !<player.has_permission[warps.admin]>:
            - narrate "You don't have permission to use this!"
            - stop
        - if <context.args.size> < 2:
            - narrate "you need to give the warp a name"
            - stop
        - else if <context.args.size> > 2:
            - narrate "you provided too many arguments"
            - stop
        - define name <context.args.get[2]>
        - if <server.has_flag[warps.<[name]>]>:
            - narrate "A warp already exists with the name of <[name]>!"
            - stop
        - flag server warps.<[name]>:<player.location>
        - narrate "created warp <[name]>!"
    - else if <[arg1]> == goto:
        - if <context.args.size> < 2:
            - narrate "you need to specify where to warp to"
            - stop
        - else if <context.args.size> > 2:
            - narrate "you provided too many arguments"
            - stop
        - define name <context.args.get[2]>
        - if !<server.has_flag[warps.<[name]>]>:
            - narrate "No warp by <[name]> exists!"
            - stop
        - teleport <player> <server.flag[warps.<[name]>]>
        - narrate "warped to <[name]>!"
    - else if <[arg1]> == player:
        - if !<player.has_permission[warps.admin]>:
            - narrate "You don't have permission to use this!"
            - stop
        - if <context.args.size> < 3:
            - narrate "you need to specify a player and where to warp to"
            - stop
        - else if <context.args.size> > 3:
            - narrate "you provided too many arguments"
            - stop
        - define playerName <context.args.get[2]>
        - define destination <context.args.get[3]>
        - define playerToWarp <server.match_player[<[playerName]>].if_null[null]>
        - if <[playerToWarp]> == null:
            - narrate "Can't find player by name <[playerName]>"
            - stop
        - teleport <[playerToWarp]> <server.flag[warps.<[destination]>]>
        - narrate "warped <[playerToWarp].name> to <[destination]>!"
    - else:
        - narrate "Unknown argument <[arg1]>"
```

Notice now the extra `if` check when the player is trying to create a warp and for warping other players using the tag `has_permission`.
Try testing this out, either with someone else or if you are on localhost remove permissions from yourself.

### Related Technical Docs

If you want to read a lot more about player commands, here are a few technical guides you might consider...

Note: most users, especially those learning from the Denizen for the first time, should just continue on to the next guides page. These references might be of interest to later come back to after you've learned Denizen as far as this guide teaches.

- [Command script containers doc](https://meta.denizenscript.com/Docs/Languages/command%20script%20containers)
- [Match_player tag doc](https://meta.denizenscript.com/Docs/Tags/server.match_player)
- [Match_offline_player tag doc](https://meta.denizenscript.com/Docs/Tags/server.match_offline_player)