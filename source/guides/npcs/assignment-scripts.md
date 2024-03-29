Who Am I: Assignment Scripts (PARTIAL)
----------------------------

**TODO: Write-up explaining the basics of assignment scripts, including the `on assignment` action.**

### Placeholder

Until this page is written, you can view the [old tutorial video here](https://one.denizenscript.com/denizen/vids/NPCs%20And%20You:%20Your%20First%20Assignment%20Script).

### Sample Script

Here's a quick sample of a modern assignment script.

```dscript_green
my_assignment:
    type: assignment
    actions:
        on assignment:
        - trigger name:click state:true
        on click:
        - chat "Hello <player.name>!"
```

This script can be assigned to your selected NPC via `/ex assignment set my_assignment`

### Related Technical Docs

If you want to read a lot more about assignment scripts, here are a few technical guides you might consider...

Note: most users, especially those learning from the Denizen for the first time, should just continue on to the next guides page. These references might be of interest to later come back to after you've learned Denizen as far as this guide teaches.

- [Assignment script containers doc](https://meta.denizenscript.com/Docs/Languages/assignment%20script%20containers)
- [On Assignment action doc](https://meta.denizenscript.com/Docs/Actions/assignment)
- [List of all assignment script actions](https://meta.denizenscript.com/Docs/Actions)
