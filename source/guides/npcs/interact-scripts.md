What Do I Do: Interact Scripts (PARTIAL)
------------------------------

**TODO: Write-up explaining the basics of interact scripts, including listing the 4 basic triggers, the concept of steps (and the zap command), and how to enable an interact script on the relevant assignment script. Demonstrate a click trigger.**

### Placeholder

Until this page is written, you can view the [old tutorial video here](https://one.denizenscript.com/denizen/vids/Your%20First%20Interact%20Script%20And%20Chat%20Trigger).

### Sample Script

Here's a quick sample of a modern interact script with two basic steps.

```dscript_green
my_assignment:
    type: assignment
    actions:
        on assignment:
        - trigger name:click state:true
    interact scripts:
    - my_interact

my_interact:
    type: interact
    steps:
        1:
            click trigger:
                script:
                - chat "Hello, <player.name>!"
                - zap 2
        2:
            click trigger:
                script:
                - chat "Hello part 2, <player.name>!"
                - zap *
```

This script can be assigned to your selected NPC via `/ex assignment set my_assignment`

### Related Technical Docs

If you want to read a lot more about interact scripts, here are a few technical guides you might consider...

Note: most users, especially those learning from the Denizen for the first time, should just continue on to the next guides page. These references might be of interest to later come back to after you've learned Denizen as far as this guide teaches.

- [Interact script containers doc](https://meta.denizenscript.com/Docs/Languages/interact%20script%20containers)
- [Trigger command doc](https://meta.denizenscript.com/Docs/Commands/trigger)
- [Interact script triggers language doc](https://meta.denizenscript.com/Docs/Languages/Interact%20Script%20Triggers)
