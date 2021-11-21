Do That Again: Loops
--------------------

```eval_rst
.. contents:: Table of Contents
    :local:
```

### What Is A 'Loop'?

All the scripts up until now had a single directional flow from top to bottom. An exact order was listed and were executed one after the other, with maybe skipping a few if you had an `if` command. However, what if you wanted to do that script you just wrote again? Well you have a few options. The most straightforward approach would simply be writing that same bit of script again. While this may work if you only wanted it repeated twice, or if there is only one line you want repeated, this can get out of hand really quickly.

Luckily you don't have to do this, Denizen has 3 different loop commands that repeat a block of script:
- `repeat` to repeat a block a set amount of times
- `foreach` to repeat a block based on a list input
- `while` keep repeating a block until a condition is met

### The Repeat Command

The most basic use of a loop is to simply run a block of commands again, which the repeat command is best suited for.
The basic format of a repeat command is
```dscript_blue
- repeat (number of times):
    - (commands here)
    - (will loop number of times)
```

This structure is similar to the `if` command, where you end the `repeat` command with a `:`. The commands that get looped need to also be indented in to let Denizen know that these are the commands you want to be looped.

Here is what it would look like in a real script...
```dscript_green
my_lightning_task:
    type: task
    script:
    - repeat 5:
        - strike <player.location>
        - narrate "you have been struck by lightning!"
        - wait 1s
    - narrate "no more lightning"
```

This would loop 5 times, wherein the player would be struck by lightning as well as be told "you have been struck by lightning!"
There is also a `wait` command at the end of the block. This pauses the script for a certain amount of time (in this example 1 second). This is important in many cases so that the commands don't run instantly after one another. In this example, it would seem as if the lightning strikes happened all at once.

Once the loop is done, the script continues, ending with "no more lightning."

What if you wanted to let the player know how many times they have been struck? You could add a definition that tracks the amount of loops, but `repeat` already does that for you. All you need to add is the `as:` argument to the repeat command like so:

```dscript_green
my_lightning_task:
    type: task
    script:
    - repeat 5 as:count:
        - strike <player.location>
        - narrate "you have been struck by lightning <[count]> times!"
        - wait 1s
    - narrate "no more lightning"
```

The narrate would now say "you have been struck by lightning 1 times!", "you have been struck by lightning 2 times!", etc... up to 5.

You can try these examples in-game via `/ex run my_lightning_task`.

### The Foreach Command

While the repeat command is handy, you'll often find yourself wanting to loop over the contents of a list and do something with each item in it.

Let's say we want to tell the player where all the cows around them are located.
With the repeat command, you might do something like this:
```dscript_red
my_cow_task:
    type: task
    script:
    - define cows <player.location.find_entities[cow].within[30]>
    - repeat <[cows].size> as:index:
        - define cow <[cows].get[<[index]>]>
        - narrate "There's a cow just <[cow].location.distance[<player.location>].round> blocks away!"
        - playeffect effect:fireworks_spark at:<[cow].location> visibility:50 quantity:100 data:0 offset:3
```

However, there is a much better way using the `foreach` command.

`foreach` has the same structure as repeat
```dscript_blue
- foreach (some list) as:(definition to store item):
    - (commands here)
    - (will loop per item in list)
```

Here's how we can simplify that script with a `foreach` loop:

```dscript_green
my_cow_task:
    type: task
    script:
    - foreach <player.location.find_entities[cow].within[30]> as:cow:
        - narrate "There's a cow just <[cow].location.distance[<player.location>].round> blocks away!"
        - playeffect effect:fireworks_spark at:<[cow].location> visibility:50 quantity:100 data:0 offset:3
```

Much better. Most notably, we don't have have to get the item `cow` from the list: it's already defined.
Additionally, foreach has a built-in definition of `<[loop_index]>` that keeps track of how many times it has looped.

For instance...
```dscript_green
my_cow_task:
    type: task
    script:
    - foreach <player.location.find_entities[cow].within[30]> as:cow:
        - narrate "<[loop_index]> - There's a cow just <[cow].location.distance[<player.location>].round> blocks away!"
        - playeffect effect:fireworks_spark at:<[cow].location> visibility:50 quantity:100 data:0 offset:3
```

The narrate would now be prefaced with a "1 - ", "2 - ", etc... as the loop goes on.

You can try these examples in-game via `/ex run my_cow_task` while standing near some cows.

### The While Command

You might encounter a situation where you don't know how many times you're going to loop, but you know when to stop. You can achieve this with a while loop. It's like an `if` command that runs the block below it as long as the condition is true.
```dscript_blue
- while (condition):
    - (commands here)
    - (will loop while condition is true)
```
The condition format is the same as the `if` command; [see that guide page](/guides/basics/if-command) for more details on its structure.

Now, lets see an example of a `while` loop...

```dscript_green
my_move_task:
    type: task
    script:
    - define location <player.location>
    - while <player.is_online> && <[location].distance[<player.location>]> < 3:
        - narrate "You're too close, move away!"
        - wait 2s
```

You can try this in-game via `/ex run my_move_task`. This task, when run, will repeatedly tell you to move away until you have moved 3 blocks from where you first were.

Just like the `repeat` command, we have a `wait` command at the end of the loop. While it's only useful in some cases with `repeat` loops, you should almost always use it with `while` loops. Without one, it will try to check the condition as often as possible all at the same time, which can cause the server to crash.

A word of warning: `while` loops should be avoided if possible. It is very easy to make what is known as an "infinite loop", as in a loop that never has a chance to stop. Once it's running, it's difficult to force it to stop beyond just stopping the server.

### Stop The Loop

Sometimes in loops you only want to keep looping until you reach a certain point. However, you may not want to stop the script entirely. While `stop` is used to stop scripts, `repeat/foreach/while stop` is used to stop the relevant loop.

For instance, in the first example, if we wanted to stop striking lightning if the player had less than 5 health, we would do as follows:

```dscript_green
my_lightning_task:
    type: task
    script:
    - repeat 5 as:count:
        - strike <player.location>
        - narrate "you have been struck by lightning <[count]> times!"
        - if <player.health> < 5:
            - repeat stop
        - wait 1s
    - narrate "no more lightning"
```
Since we're using `repeat stop`, only the loop ends; the end `narrate` line still runs.

It can also be used in `foreach` loops. For instance, if we wanted to stop looping if we found a baby cow in the example above

```dscript_green
my_cow_task:
    type: task
    script:
    - foreach <player.location.find_entities[cow].within[30]> as:cow:
        - narrate "<[loop_index]> - There's a cow just <[cow].location.distance[<player.location>].round> blocks away!"
        - playeffect effect:fireworks_spark at:<[cow].location> visibility:50 quantity:100 data:0 offset:3
        - if <[cow].is_baby>:
            - narrate "omg its a baby!!"
            - foreach stop
```

### Next Please

There are times when you want to skip to the next loop without finishing the current iteration. For this, you would use `repeat/foreach/while next`.

Take the `foreach` example we had, lets say we want to skip over all baby cows. While you can put the whole block inside an `if` command like so...
```dscript_green
my_cow_task:
    type: task
    script:
    - foreach <player.location.find_entities[cow].within[30]> as:cow:
        - if !<[cow].is_baby>:
            - narrate "<[loop_index]> - There's a cow just <[cow].location.distance[<player.location>].round> blocks away!"
            - playeffect effect:fireworks_spark at:<[cow].location> visibility:50 quantity:100 data:0 offset:3
```

You could instead use `next`

```dscript_green
my_cow_task:
    type: task
    script:
    - foreach <player.location.find_entities[cow].within[30]> as:cow:
        - if <[cow].is_baby>:
            - foreach next
        - narrate "<[loop_index]> - There's a cow just <[cow].location.distance[<player.location>].round> blocks away!"
        - playeffect effect:fireworks_spark at:<[cow].location> visibility:50 quantity:100 data:0 offset:3
```


### Related Technical Docs

If you want to read a lot more about loops, here are a few technical guides you might consider...

Note: most users, especially those learning from the Denizen for the first time, should just continue on to the next guides page. These references might be of interest to later come back to after you've learned Denizen as far as this guide teaches.

- [Foreach command doc](https://meta.denizenscript.com/Docs/Commands/foreach)
- [Repeat command doc](https://meta.denizenscript.com/Docs/Commands/repeat)
- [While command doc](https://meta.denizenscript.com/Docs/Commands/while)
