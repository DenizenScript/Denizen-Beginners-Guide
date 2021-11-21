Chat Triggers (PARTIAL)
-------------

**TODO: Write-up explaining chat triggers, including both standard triggers and dynamic regex triggers (particularly a catch-all). Remind the user to activate it with `trigger` in `on assignment`.**

### Placeholder

Until this page is written, you can view the [old tutorial video here](https://one.denizenscript.com/denizen/vids/Your%20First%20Interact%20Script%20And%20Chat%20Trigger).

### Sample Script

Here's a quick sample of a modern interact script with two basic chat triggers.

```dscript_green
my_assignment:
    type: assignment
    actions:
        on assignment:
        - trigger name:chat state:true
    interact scripts:
    - my_interact

my_interact:
    type: interact
    steps:
        1:
            chat trigger:
                1:
                    trigger: /Hello/ friendly NPC!
                    script:
                    - chat "Hello, <player.name>!"
                2:
                    trigger: /Goodbye/ friendly NPC!
                    script:
                    - chat "Farewell, <player.name>!"
```

This script can be assigned to your selected NPC via `/ex assignment set my_assignment`

### Related Technical Docs

If you want to read a lot more about chat triggers, here are a few technical guides you might consider...

Note: most users, especially those learning from the Denizen for the first time, should just continue on to the next guides page. These references might be of interest to later come back to after you've learned Denizen as far as this guide teaches.

- [Chat triggers language doc](https://meta.denizenscript.com/Docs/Languages/chat%20triggers)
