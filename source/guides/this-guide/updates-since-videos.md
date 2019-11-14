Updates Since the Tutorial Videos
---------------------------------

Denizen has had quite a number of updates over the years since the original tutorial videos were published! This guide page documents the changes that you should know about for best practices.

### Colon Syntax

Braced syntax has been replaced with colon syntax. As documented on the page for [The If Command](/guides/basics/if-command), colon syntax allows you to use multiple commands within an `if` command, `foreach` command, or `while` command. Unlike braced syntax, no closing character is needed - when you return to the prior level of spacing, the script will continue as normal.


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

Colon syntax is easier to write, and as an added bonus, Denizen even parses it more efficiently!

### Definition Syntax

The `define` command has had two significant changes - first, the syntax has changed for the definition tag itself, and second, the define command now supports [data actions](https://one.denizenscript.com/denizen/lngs/data%20actions).

Definition syntax no longer looks like `%this%`, but instead looks like `<[this]>` (for a definition of `this`, of course). For additional details on how to use and modify definitions, please see the [Definitions](/guides/basics/definitions) page.

Here's an example of the old syntax updated to the new syntax:

```dscript_red
old_definition_syntax:
    type: task
    script:
    - define name <player.name>
    - narrate "Hello, %name%!"
```

```dscript_green
new_definition_syntax:
    type: task
    script:
    - define name:<player.name>
    - narrate "Hello, <[name]>!"
```

### Operators Versus .is[].to[]

In the past, the `while` command previously only accepted one argument, so it was necessary to use tags like `<player.health.is[>=].to[10]>]>` to evaluate expressions.

This limitation no longer exists - the `while` command now supports operators.

The following is an example of a task script using the `while` command that will narrate to a player when their health is below 10, with both old and modern syntax:

```dscript_red
old_while_syntax:
    type: task
    script:
    - while <player.health.is[>=].to[10]>:
        - wait 1s
    - narrate "Your health is getting low!"
```

```dscript_green
new_while_syntax:
    type:
    script:
    - while <player.health> >= 10:
        - wait 1s
    - narrate "Your health is getting low!"
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

### Stop is the New Queue Clear

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

### Use .has_flag[] to Check Flag Existence

In the past, including [the Kill Quest tutorial video](https://one.denizenscript.com/denizen/vids/Putting%20It%20Together:%20A%20Kill%20Quest), `.flag[]` was used to check both the value of a flag and whether the flag existed.

Now, the correct way to check whether a flag exists is to use `.has_flag[]`. `.flag[]` is now only for checking the value of a flag, and should only be used where the flag is known to exist. Here are some examples:

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