Do That Again: Loops (PARTIAL)
--------------------

**TODO: Write-up that introduces loops in general, using the repeat command.**

**TODO: Write-up explaining the foreach command.**

**TODO: Write-up explaining the while command.**

### Placeholder

Until this page is written, you can view the [old tutorial video here](https://one.denizenscript.com/denizen/vids/Loops).

### Sample Script

Here's a few quick samples of loops in action.

```dscript_green
my_counter_task:
    type: task
    script:
    - repeat 10 as:num:
        - narrate "I can count! <[num]>"
```

You can try this in-game via `/ex run my_counter_task`. It will count from 1 to 10.

```dscript_green
my_cow_task:
    type: task
    script:
    - foreach <player.location.find_entities[cow].within[30]> as:cow:
        - narrate "There's a cow just <[cow].location.distance[<player.location>].round> blocks away!"
        - playeffect effect:fireworks_spark at:<[cow].location> visibility:50 quantity:100 data:0 offset:3
```

You can try this in-game via `/ex run my_cow_task` while standing near some cows. It will tell you about all the cows nearby.

```dscript_green
my_move_task:
    type: task
    script:
    - define location <player.location>
    - while <player.is_online> && <[location].distance[<player.location>]> < 3:
        - narrate "You're too close, move away!"
        - wait 2s
```

You can try this in-game via `/ex run my_move_task`. It will repeatedly ask you to move until you move at least 3 blocks away.

### Related Technical Docs

If you want to read a lot more about loops, here are a few technical guides you might consider...

Note: most users, especially those learning from the Denizen for the first time, should just continue on to the next guides page. These references might be of interest to later come back to after you've learned Denizen as far as this guide teaches.

- [Foreach command doc](https://meta.denizenscript.com/Docs/Commands/foreach)
- [Repeat command doc](https://meta.denizenscript.com/Docs/Commands/repeat)
- [While command doc](https://meta.denizenscript.com/Docs/Commands/while)
