Blurring The Line Between Commands And Tags: Procedure Scripts (PARTIAL)
--------------------------------------------------------------

**TODO: Write-up that introduces procedure scripts, how they work, what they do, how to use contexts, gives examples of when they would be useful, and explains the limits (procedural commands)**

### Placeholder

Until this page is written, you can view the [old tutorial video here](https://one.denizenscript.com/denizen/vids/Procedure%20Scripts).

### Sample Script

Here's a few quick samples of procedure scripts in action.

```dscript_green
pretty_name:
    type: procedure
    script:
    - determine <player.name.hex_rainbow>
```

You can get this item in-game by typing `/ex narrate <proc[pretty_name]>`. It will show your name in rainbow colors.

```dscript_green
prettifier:
    type: procedure
    definitions: text
    script:
    - determine <[text].strip_color.to_titlecase.hex_rainbow>
```

You can get this item in-game by typing `/ex narrate <player.name.proc[prettifier]>`. It will show your name in rainbow colors and title case. You can also try `/ex narrate "<element[this is some sample text here].proc[prettifier]>"`. It will automatically rainbow + titlecase that entire piece of sample text.

### Related Technical Docs

If you want to read a lot more about the run command and its options, here are a few technical guides you might consider...

Note: most users, especially those learning from the Denizen for the first time, should just continue on to the next guides page. These references might be of interest to later come back to after you've learned Denizen as far as this guide teaches.

- [Procedure script doc](https://meta.denizenscript.com/Docs/Languages/procedure%20script%20containers)
- [Proc tag doc](https://meta.denizenscript.com/Docs/Tags/proc)
- [Proc.Context tag doc](https://meta.denizenscript.com/Docs/Tags/proc.context)
