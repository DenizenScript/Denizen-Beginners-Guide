Short Term Memory: Definitions
------------------------------

```eval_rst
.. contents:: Table of Contents
    :local:
```

### What Are Definitions?

So, you know how to write basic scripts. You've learned the basic ideas of script types, commands, and tags.

If you've been following along and thinking about things, you've probably figured out by now that you can cause the value of a tag to change by modifying the real in-game value the tag is based on.

For example, you can modify the value `<player.health>` via the `hurt` or `heal` commands. If `<player.health>` returns 20, and you want it to be 10, you can just `- hurt 10`. Pretty straight-forward.

But what if you want a value that you can read from a tag or change at will, but that isn't locked to some real in-game value.

Enter **definitions**.

Definitions <span class="parens">(often called just 'defs')</span> are a simple form of short-term memory within a Denizen script. In mathematics, these would be called *variables*.

### How Do You Use Definitions?

Definitions are created or changed by the `define` command, and read by the definition tag.

Any definition has a name and a value. The name is usually static <span class="parens">(but can be dynamic)</span> and is written directly into scripts. The value is dynamic and handled entirely in memory.

#### The Definition Tag

The definition tag is a special tag. While it's technically labeled `<definition[<name>]>` <span class="parens">(where `name` is the name of the definition)</span>, it is written in scripts like `<[<name>]>`.

For example, the definition named `target` can be read with the `<[target]>`.

If the definition named `target` holds a value of type `EntityTag`, then the tag `<EntityTag.health>` can be used like `<[target].health>`.

If you recall the [basic format of a tag](/guides/first-steps/tags), a tag starts with a base tag, and can sometimes take an input. For example, `<element[hi]>` is the base tag named `element` with input `hi`. This might surprise you, but the definition tag actually follows this format exactly. You're probably asking "what's the base tag here?", and the answer is: nothing. The base tag of nothing is the definition base tag. That is, the base tag with a name zero letters long is interpreted as a shorthand for `definition`.

#### The Define Command

The `define` command is how you create or change a definition.

The standard input format for `define` is: `- define <name> <value>`.

So, for example:
- `- define target <player.target>` sets the definition named `target` to the value of whatever entity the player is currently looking at.
- `- define count 10` sets a definition named `count` to the value `10`.
- `- define goal <player.health.mul[2]>` sets a definition named `goal` to the value of the player's current health, multiplied by two.

### Basic Usage Example

Here's a simple task script that shows `define` commands and definition tags in use.

```dscript_green
def_sample:
    type: task
    script:
    - define current <player.health>
    - define goal <util.random.int[2].to[10]>
    - narrate "Your health is <[current]>. Let's heal you to <[current].add[<[goal]>]>!"
    - heal <[goal]>
```

If you `/ex run def_sample` in-game, you will be shown your health and a randomly chosen higher value, and then be healed to reach that higher value <span class="parens">(or reach max health)</span>.

### Defs, Huh, What Are They Good For?

If you look at the `def_sample` script above, you'll see a very common example of where definitions are very useful: random values! If you tried to use that `util.random` tag in both the `narrate` and `heal` lines, you would be shown one value in chat and then healed for a different one. That's not good! Using a definition means you can randomize the value once, and then use the chosen value multiple times.

In addition to random/complex values, the other primary use case for definitions is values that change. For example, consider the following script:

```dscript_red
this_needs_defs:
    type: world
    events:
        after player breaks *_ore:
        - ratelimit <player> 30s
        - if <player.health> < 5:
            - narrate "You mined a <context.material.name>! Pretty impressive."
            - wait 2s
            - narrate "But shouldn't you be healing, not mining shiny things, <player.name>?"
            - wait 2s
            - narrate "You only have <player.health> health left."
```

This might seem fine at first glance, and probably will work as expected while testing. When a player is badly injured and gets distracted by ore mining, the script will send annoying chat messages telling them to heal, no more often than every 30 seconds.

A lot of scripts make use of `wait` commands, especially ones like this that are meant to work like dialogue, and thus have delay between messages. Unfortunately, that delay adds a potential problem to the script: what if the player heals <span class="parens">(or for that matter, dies)</span> in the 4 seconds between breaking the block and that final message showing? You'll see a message like `You only have 20 health left!`, and that's a bit silly.

Definitions allow us to salvage this silly script idea, by predefining the health value, we make sure the final message shows the low value we expected.

```dscript_green
better_with_defs:
    type: world
    events:
        after player breaks *_ore:
        - ratelimit <player> 30s
        - define health <player.health>
        - if <[health]> < 5:
            - narrate "You mined a <context.material.name>! Pretty impressive."
            - wait 2s
            - narrate "But shouldn't you be healing, not mining shiny things, <player.name>?"
            - wait 2s
            - narrate "You only have <[health]> health left."
```

Now the final message is guaranteed to show that below-5 health value from when the player first broke the block, as expected.

As the last common use case for definitions: cleanliness. Sometimes a line gets really long from complicated tags, so sticking a complicated tag into a definition lets you fit it into the original line with just a short definition tag, making things a bit cleaner.

### Lifetime

Definitions, as the title of the page says, are *short term* memory. What does that 'short term' mean?

Formally speaking, a definition is linked to the queue in which it was created, and exists for only so long as that queue does <span class="parens">(you'll learn more about [queues later in this guide](/guides/basics/queues))</span>.

What this means in normal usage is: each time a script runs, it has its own set of definitions. If you set a definition in one event, or one firing of an event, it will not be available in the next event firing.

Here are a few examples of how definitions **do NOT** work.

```dscript_red
cant_go_between_scripts:
    type: world
    events:
        after player breaks iron_ore:
        - define health <player.health>
        after player breaks stone:
        - narrate "You had <[health]> health when you broke iron."
```

The above example will not work, because the definition was set in a different script path than where it was read.

```dscript_red
no_queue_persistence:
    type: world
    events:
        after player breaks iron_ore:
        - narrate "You had <[next_health]> health when you broke that last bit of iron."
        - define next_health <player.health>
```

The above example will obviously not work first of all because the first time you break iron_ore, that define command never ran in the first place. However, even after that first run, the definition will continue to not work, as the definition from the *last time* the event fired is not still available the *next time* that event fires.

To be clear, this isn't just for events: any time you `run` a `task` script, it has a different set of definitions <span class="parens">(you'll learn how to change this in a [later part of this guide](/guides/basics/run-options))</span>.

On [the next page](/guides/basics/flags), you'll learn about an option for long-term memory.

### Advanced Definition Changes

If you want to change a definition you already set, you can of course just do another define command. For example, the following is fine:

```dscript_green
def_sample:
    type: task
    script:
    - define current <player.health>
    - define goal 1
    - if <player.inventory.contains.scriptname[healing_tool]>:
        - define goal 20
    - narrate "Your health is <[current]>. Let's heal you to <[current].add[<[goal]>]>!"
    - heal <[goal]>
```

This script will heal the player for 1 HP, unless they have a custom item named 'healing_tool' in their inventory, in which case it will heal up to full. This usage of a define that overwrites a previous define of the same name is completely valid and will work as expected.

But, what if you want to modify the value in some way - for example, adding 1 to the existing value in the definition? You can, of course, simply use tags to do the work, like `- define mydef <[mydef].add[1]>`.

There is, however, a cleaner way to do these common value changes to definitions. This way is called **Data Actions**.

#### How Do You Use Data Actions?

Data actions are pretty simple to write. Here's the previous example, but using a data action instead of a tag: `- define mydef:++`. That's a lot cleaner!

The data actions that can be used like that are:
- `++` increments the value (adds one). For example: `- define mydef:++`
- `--` decrements the value (subtracts one). For example: `- define mydef:--`
- `!` clears the value (removes the definition). For example: `- define mydef:!`

There are also data actions that take an additional input value. For example, if you want to add 3 to a definition, you can do `- define mydef:+:3`.

The data actions that can be used like that are:
- `+` adds the input to the definition. For example: `- define mydef:+:3`
- `-` subtracts the input from the definition. For example: `- define mydef:-:3`
- `*` multiplies the definition by the input. For example: `- define mydef:*:3`
- `/` divides the definition by the input. For example: `- define mydef:/:3`

Definitions can of course hold ListTag values. When a definition holds a list, there are data actions available to make interacting with that list easier.

The data actions that can be used with ListTag values are:
- `->` inserts a new value to the list. For example: `- define mydef:->:new_value`
- `<-` removes an existing value from the list. For example: `- define mydef:<-:old_value`
- `|` splits the input list into the original list. For example: `- define mydef:|:a|b|c`
- `!|` clears the existing list and splits the input list into it instead <span class="parens">(a combination of `!` clear and `|` split)</span>. For example: `- define mydef:!|:a|b|c`

For the sake of ensuring you understand what each of these do, considering write a task script that performs the example changes on an existing definition and observing the result.

```dscript_blue
data_actions_test:
    type: task
    script:
    - define mydef 3
    # Change the line below to each of the example data actions and run each
    - define mydef:++
    - narrate "mydef became <[mydef]>"
```

When you run that script, it will first narrate `mydef became 4`, showing that the value 3 incremented and became 4. As you change the middle line to each of the examples, you'll see how they affect the value.

For the list data actions, change the first line to `- define mydef <list[old_value|some_other_value]>` for testing.

### Other Definition Sources

As an added note, be aware that there are some things that create definitions other than the `define` command, including [loops](/guides/basics/loops), some various commands <span class="parens">(like shoot)</span> that will say when they create a definition in the relevant command's documentation, and sometimes external plugins that hook into Denizen.

### Related Technical Docs

If you want to read a lot more about definitions, here are a few technical guides you might consider...

Note: most users, especially those learning from the Denizen for the first time, should just continue on to the next guides page. These references might be of interest to later come back to after you've learned Denizen as far as this guide teaches.

- [Define command doc](https://one.denizenscript.com/denizen/cmds/define)
- [definition tag](https://one.denizenscript.com/denizen/tags/definition)
- [definition.exists tag](https://one.denizenscript.com/denizen/tags/definition.exists)
- [data actions language doc](https://one.denizenscript.com/denizen/lngs/data%20actions)
