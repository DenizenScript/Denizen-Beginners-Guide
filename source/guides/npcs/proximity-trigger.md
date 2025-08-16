Proximity Triggers (PARTIAL)
------------------

**TODO: Write-up explaining proximity triggers, including entry, exit, and move triggers. Remind the user to activate it with `trigger` in `on assignment`.**

### Placeholder

Until this page is written, you can view the [old tutorial video here](https://one.denizenscript.com/denizen/vids/Proximity%20Triggers).

### Sample Script

Here's a quick sample of a modern interact script with some basic proximity triggers.

```dscript_green
my_assignment:
    type: assignment
    actions:
        on assignment:
        - trigger name:proximity state:true radius:10
    interact scripts:
    - my_interact

my_interact:
    type: interact
    steps:
        1:
            proximity trigger:
                entry:
                    script:
                    - chat "Hello, <player.name>!"
                exit:
                    script:
                    - chat "Farewell, <player.name>!"
                move:
                    script:
                    - ratelimit <player> 10s
                    - chat "Still hanging around, <player.name>?"
```

This script can be assigned to your selected NPC via `/ex assignment set script:my_assignment`

### Related Technical Docs

If you want to read a lot more about proximity triggers, here are a few technical guides you might consider...

Note: most users, especially those learning from the Denizen for the first time, should just continue on to the next guides page. These references might be of interest to later come back to after you've learned Denizen as far as this guide teaches.

- [Proximity triggers language doc](https://meta.denizenscript.com/Docs/Languages/proximity%20triggers)
