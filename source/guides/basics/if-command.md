Changing The Path: The If Command
---------------------------------

```eval_rst
.. contents:: Table of Contents
    :local:
```

### Required Reading

Before starting this section, you should already understand everything in the [Your First Steps](/guides/first-steps/index) category.

### What Is The 'If' Command?

You learned how to use events to run a set of commands whenever a situation occurs on your server. You learned how to use tags to change what any command does based on the details of the situation.
Now it's time to use the `if` command to combine the two concepts: choosing a set of commands to run based on the details of the situation.

The `if` command does exactly what it says on the tin: it says "*if* something is true, then run these commands. Otherwise, don't run them."

### So What Does An If Look Like?

Don't worry, `if` commands are pretty easy to write, and look just like anything else in a Denizen script does.

Here's the basic format:
```dscript_blue
- if (some condition here):
    - (some commands)
    - (go here)
```

As you can see, `if` is a command <span class="parens">(written just like any other at the start, with some condition(s) as its input arguments)</span>
but with a `:` on the end <span class="parens">(just like you would have on an event line)</span>,
and some commands spaced out and placed within. The thing to be extra careful about here is the spacing on the commands within.
If the commands within don't get spaced out a step, Denizen won't know that they were meant to be in the `if`, and just run them regardless of the condition you give.

Let's see how this might look in a real script...
```dscript_green
magic_healing_bell:
    type: world
    events:
        on player right clicks bell:
        - if <player.health.percentage> < 25:
            - heal
            - actionbar "<green>The bell has healed you!"
```

This handy sample script will instantly heal a player that clicks on it, but *only if* their health is dangerously low.
<span class="parens">(When we get to the [Flags](flags) section we'll revisit this sample script to add a rate limit, so players can only heal once every few minutes).</span>

### Conditions

There's a few different ways to make a condition in an `if` command.
At its simplest, the condition could be a boolean tag <span class="parens">(one that returns 'true' or 'false')</span>, and that's enough right there. <span class="parens">(For example, `- if <player.on_fire>:`)</span>.
The `if` sub-commands will run when the tag returns `true`, and won't when it returns `false`.

It could also be some value tag <span class="parens">(a tag that returns anything more complicated than a boolean)</span>, in which case it will be compared to some other value.
The basic format of an `if` command that compares two values is `- if (first value) (comparison) (second value):` <span class="parens">(for example, `- if <player.name> == mcmonkey4eva:`)</span>.
One or both values can be a tag. <span class="parens">(Technically, both values can also be static text, but that would mean the `if` command either always runs its sub-commands, or never does... that's not a very useful `if` command)</span>.

There are a few different comparison types available:
- `==` to test equality <span class="parens">(`- if 3 == 3:` will run its commands, but `- if 3 == 4:` will not)</span> - you can read this as "if three is equal to three, then run some commands".
- `!=` to test equality but expect the opposite result <span class="parens">(so, `- if 3 != 3:` will **not** run its commands, and `- if 3 != 4:` **will** run its commands)</span> - the `!` is read as "not",
so you can read this like "if three **is not** equal to three, then run some commands." Of course in real usage, one or both of the values would be from a tag.
- `>` (is greater than), `>=` (is greater than or equal to), `<` (is less than), and `<=` (is less than or equal to) to test numeric comparisons.
- `matches` to test if a value fits a mold <span class="parens">(this will be explained later)</span>.
- `contains` to test if a list contains an entry <span class="parens">(this will be explained later)</span>.

### The Most Common Usage of 'If'

**TODO: `stop` command usage**

### TODO

**TODO: else if commands, explanation of matches and contains, discussion of the idea that you can put an if inside another if...**
