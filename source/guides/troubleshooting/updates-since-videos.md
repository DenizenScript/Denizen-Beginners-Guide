Updates Since the Tutorial Videos
---------------------------------

Denizen has had quite a number of updates over the years since the original tutorial videos were published <span class="parens">(5-6 years ago)</span>! This guide page documents the changes that you should know about for best practices.

```eval_rst
.. contents:: Table of Contents
    :local:
```

### Editor of Choice

In the tutorial videos, Notepad++ was displayed as the script editor to use. This was basically just a slightly better text editor. Since then, we've gotten an actual proper script editor, based on an extension to VS Code.

For more information, refer to the page on [Setting Up The Script Editor](/guides/first-steps/script-editor).

### We're on Discord Now

The tutorial videos showcase some interactions with a bot on IRC - if you've tried to reach this IRC, you've already seen the messages that we moved to Discord. You're probably also aware of that if you got to this guide.

But, just in case you haven't yet seen it - we're on Discord, so [join us there!](https://discord.gg/Q6pZGSR). We provide human support and bot-assisted searches/script-checking/etc. there.

### Colon Syntax

Braced syntax has been replaced with colon syntax. As documented on the page for [The If Command](/guides/basics/if-command), colon syntax allows you to use multiple commands within commands like `if` and `foreach`. Unlike braced syntax, no closing character is needed - when you return to the prior level of spacing, the script will continue as normal.

If you've written scripts using braced syntax, you can quickly convert them to colon syntax by deleting all closing brace characters (`}`), replacing the opening brace character (`{`) with a colon, and removing any extra spaces between the colon and the last other character in the line.

For example, here's a script converted from braced syntax to colon syntax:

```dscript_red
old_brace_syntax:
    type: task
    script:
    - if <player.has_flag[test]> {
        - narrate "This is an example of braced syntax!"
        }
    - narrate "This narrate will always run!"
```

```dscript_green
new_colon_syntax:
    type: task
    script:
    - if <player.has_flag[test]>:
        - narrate "This is an example of colon syntax!"
    - narrate "This narrate will always run!"
```

Colon syntax is easier to write, looks cleaner, and as an added bonus, Denizen even parses it more efficiently!

### Definition Syntax

The `define` command has had two significant changes - first, the syntax has changed for the definition tag itself, and second, the define command now supports [data actions](https://meta.denizenscript.com/Docs/Languages/data%20actions).

The videos taught two different forms of definition syntax: First, the 'ancient style' percent syntax (like `%this%`), and second, the 'old style' tag syntax (like `<def[this]>`).
Definition tags no longer look like that, but instead looks like `<[this]>` <span class="parens">(for a definition named `this`, of course)</span>. For additional details on how to use and modify definitions, please see the [Definitions](/guides/basics/definitions) page.

Note that `%name%` is considered ancient and completely unsupported, and should never be used. `<def[name]>` however is considered an older/alternative syntax for the modern `<[name]>` <span class="parens">(it's the same tag-base syntax, except the empty-name tag is now available in place of a tag named `def`)</span>.

Here's an example of the old syntax updated to the new syntax:

```dscript_red
old_definition_syntax:
    type: task
    script:
    - define name <player.name>
    # Ancient
    - narrate "Hello, %name%!"
    # Old
    - narrate "Hello, <def[name]>!"
```

```dscript_green
new_definition_syntax:
    type: task
    script:
    - define name <player.name>
    - narrate "Hello, <[name]>!"
```

### Changes To The While Command

In the past, the `while` command previously only accepted one argument, so it was necessary to use tags like `<player.health.is[>=].to[10]>]>` to evaluate expressions.

This limitation no longer exists - the `while` command now supports operators, the same as the `if` command.

The following is an example of a task script using the `while` command that will wait for a player's health to drop below 10, then narrate a warning to them, with both old and modern syntax:

```dscript_red
old_while_syntax:
    type: task
    script:
    - narrate "Challenge: don't lose too much health!"
    - while <player.health.is[>=].to[10]>:
        - wait 1s
    - narrate "Your health got too low! You lose!"
```

```dscript_green
new_while_syntax:
    type:
    script:
    - narrate "Challenge: don't lose too much health!"
    - while <player.health> >= 10:
        - wait 1s
    - narrate "Your health got too low! You lose!"
```

Note that this specific waiting-until-something style of logic has as well been replaced by a specialized command, `waituntil`, which can be used like so:

```dscript_green
new_while_syntax:
    type:
    script:
    - narrate "Challenge: don't lose too much health!"
    - waituntil rate:1s <player.health> < 10
    - narrate "Your health got too low! You lose!"
```

### Assignment Script Updates

Historically, multiple interact scripts were used on NPCs with conditions to determine which script would run. Denizen now features steps in interact scripts and the `zap` command, so only one interact script is needed (and supported). The numbers next to the interact scripts entry of an assignment script, accordingly, are no longer necessary and should be removed.

Here are examples of old and updated syntax:

```dscript_red
old_assignment_script:
    type: assignment
    interact scripts:
    - 10 my_cool_npc_interaction
```

```dscript_green
new_assignment_script:
    type: assignment
    interact scripts:
    - my_cool_npc_interaction
```

### Stop Is The New Queue Clear

`queue clear` was once used to stop a queue while it was running. That command has been updated to `stop`.

The replacement is simple:

```dscript_red
old_queue_clear:
    type: task
    script:
    - if <player.has_flag[buff]>:
        - queue clear
    - narrate "You don't have the necessary buff!"
```

```dscript_green
new_stop:
    type: task
    script:
    - if <player.has_flag[buff]>:
        - stop
    - narrate "You don't have the necessary buff!"
```

### Use .has_flag[] To Check Flag Existence

In the past, including [the Kill Quest](/guides/put-it-together/kill-quest) tutorial video, `.flag[]` was used to check both the value of a flag and whether the flag existed.

Now, the correct way to check whether a flag exists is to use `.has_flag[]`. `.flag[]` is now only for reading the value of a flag, and should only be used where the flag is known to exist <span class="parens">(or with a fallback)</span>. Here is an example:

```dscript_red
old_flag:
    type: task
    script:
    - if <player.flag[VIP]>:
        - narrate "Your VIP level is <player.flag[VIP]>!"
```

```dscript_green
new_has_flag:
    type: task
    script:
    - if <player.has_flag[VIP]>:
        - narrate "Your VIP level is <player.flag[VIP]>!"
```

### The Flag Rewrite

In addition to the `has_flag` tag, a later total internal rewrite of the flag system has taken place (December 2020).

The most relevant change from the videos in this regard is that the tag `<player.flag[NAME].expiration>` seen in the kill quest video should be changed to `<player.flag_expiration[NAME].from_now>`.

Due to the significant general changes to the flag system, more modern documentation for flags should be used than the old videos, so refer to [The Flags Page](/guides/basics/flags).

### Event Cancellation Is A Little More Advanced Now

In the tutorial video for [Inventory GUIs](/guides/put-it-together/inventory-guis), it is taught to cancel the generic clicks event, and run actions in response to the more specific event.

While this is still correct, it is missing a necessary component to work well in modern Denizen.

In the past, events would just all fire, and if an event got cancelled that just means the underlying action wouldn't be performed. In modern Denizen, the system more intelligently knows to not fire more script events after the event was cancelled. While this [can be simply disabled for the relevant events](https://meta.denizenscript.com/Docs/Languages/Script%20Event%20Cancellation) a better solution is to instead guarantee that the generic event that cancels it will run *last*. This is as easy as adding a high-valued `priority` to the cancelling event line.

So, where previously you had `on player clicks in my_inventory:` you now instead have `on player clicks in my_inventory priority:100:`, and a similar change to the `drags` event line. Event priorities run in numerical order, with a default of `0`. So all the specific events, with their default priority, will run first, and then only after they're done, the generic cancellation events <span class="parens">(now at priority `100`)</span> will fire last.

### Tags With Carets Aren't Used Anymore

The videos demonstrated the tag `<^npc>` as a way to get the NPC from a queue prior to the `npc:` argument being used, and mentioned `<^player>` as a matching concept. These are considered outdated/irrelevant now, as you can and should instead just use `define`

```dscript_blue
better_npc_handler:
    type: task
    script:
    - narrate "Let's pass NPCs backwards"
    - define npc <npc>
    - run my_other_task def:<[npc]> npc:<[some_other_npc]>
```

In the above example, the `define` command and the tag `<[npc]>` are used to replace what would have otherwise been the `<^npc>` tag.

(This was removed due to a combination of been extremely rarely used, and having very complex internals weighing down the script engine even when not in use).
