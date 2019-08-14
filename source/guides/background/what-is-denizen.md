What is Denizen?
----------------

```eval_rst
.. contents:: Table of Contents
    :local:
```

### So, What Is Denizen?

In short: Denizen is a scripting language!

A bit longer: Denizen is a plugin for Spigot servers that loads and runs user-written scripts automatically, allowing server owners to quickly and easily customize their server however they please, in a manner similar to developing your own plugins, but ten times faster and ten times easier!

### Let's Be Semi-Formal About It

Denizen scripts are contained within a YAML-like structuring, for the sake of ease and familiarity - have you ever edited some YAML configs for a plugin on your server? Imagine that kind of simple YAML config editing but you can do *anything you want* with it!

The actual syntax, within the script sections, is a command-tag syntax...

- **Command:** Again a very familiar concept to most server owners - you use commands all the time, like `/gamemode creative` or `/tp player`. It's the same thing, just a `-` instead of a `/`.
- **Tag:** This is one that's a mix of familiar and strange - if you look at the *documentation* for a command, it might say something like `/tp <player>`, indicating that you should put the name of the player into that first argument when actually using it. A **tag** in Denizen is essentially one of those "fill me in" placeholders, except it fills itself in. When you type `<player>` in a Denizen script, the system will fill in the correct player automatically for you. This is the magic trick that turns some simple commands into dynamic powerful scripts.

### What Does It Look Like?

Here's an example of a simple Denizen script:

```dscript_green
my_example_script:
    type: task
    script:
    - narrate "Hello there, <player.name>!"
    - wait 5s
    - hurt <player> 1
```

That simple script, when ran, will: Greet the player by name (automatically filled in), wait 5 seconds, then the hurt the player for one hitpoint.

### So, It's Like Programming?

For those familiar with programming in other languages, a lot of Denizen can be analogized into terms of those programming languages (if statements, foreach loops, etc. are basically equivalent), though it's important to note that there's a lot of very key differences between Denizen and languages like JavaScript, C#, or most other common languages. If you've learned one of those languages, you'll have a pretty easy time picking up Denizen - just be careful not to try to write Denizen scripts the way you would write code in common programming languages, as it just isn't the same. Depending on your preferences with programming languages, you might be surprised at how much easier Denizen is to work with than the languages you've used before.

If you're not familiar with any programming languages, don't worry - Denizen is designed at its heart to be friendly and easy to learn for those without experience. There's piles and piles of tools and helpers present to make Denizen so much easier to learn and to work with than a more intimidating language like Java.

### So Denizen Is Easier To Learn And To Use... What's The Catch?

Some readers might be thinking right now "it's gotta be much less powerful, right?" ... well that's the funny part. In Denizen, you often can do *more* than you could do with a Java plugin. There are some exceptions - you can't go link into some random Java chess library or whatever for giggles in Denizen as you can in Java - but when it comes to interacting with the Minecraft server, Denizen not only provides the majority of the Bukkit API's functionality, and a massive set of extra utilities and quality-of-life-improvements on top, but in fact also provides a large set of functionalities not exposed to Bukkit, via NMS calls. As an example: Bukkit doesn't have an API to stick arrows into an entity, but Denizen can do that in a single quick command. Bukkit doesn't have an event for messages sent *to* a player, but Denizen can intercept those for you no problem. Bukkit doesn't have a way to spawn a light source without actually changing to a torch (or similar) block... but Denizen has the `light` command ready to use at any time. There's so many more features like this, several in the category of "why *doesn't* Bukkit support this?! It's so useful!"

Now the other catch that might come to mind: performance. Do scripts run as fast as pure Java code would? Well... yes and no. If you go for a hard 1-to-1 comparison, tight loop in Java vs. tight loop in Denizen... Java is going to win with ease. But in real use cases, Denizen is able to keep up to a sufficient degree that for 99% of scripts you might write, there's not going to be any noticeable performance hit. Dedicated scripters have replicated the functionality of plugins like WorldGuard and kept their servers running at full tick rate without problem.
