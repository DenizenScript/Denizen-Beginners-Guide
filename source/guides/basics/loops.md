Do That Again: Loops (PARTIAL)
--------------------

### What Is A 'Loop'?

All the scripts up until now had a single directional flow from top to bottom. An exact order was listed and were executed one after the other, with maybe skipping a few if you had an `if` command. However, what if you wanted to do that script you just wrote again? Well you have a few options. The most straightforward approach would simply be writing that same bit of script again. While this may work if you only wanted it repeated twice, or if there is only one line you want repeated, this can get out of hand really quickly.

Lukcily you dont have to do this, Denizen has 3 different loop commands that repeat a block of script:
- `repeat` to repeat a block a set amount of times
- `foreach` to repeate a block based on a list input
- `while` keep repeating a block until a condition is met

### The Repeat Command

The most basic use of a loop is to simply just do a block of script again, in which the repeat command is best suited for.
The basic format of a repeat command is
```
- repeat (number of times):
    - (commands here)
    - (will loop number of times)
```

This structure is similar to the `if` command, where you end the `repeat` command with a `:`. The commands that get looped need to also be indented in to let denizen know that these are the commands you want to be looped.

Here is what it would look like in a real script...
```dscript_green
my_zap_task:
    type: task
    script:
    - repeat 5:
        - strike <player.location>
        - narrate "you have been zapped!"
    - narrate "no more zaps"
```

This would in essence loop 5 times, where the player would be striken by lightning 5 times as well as been told "you have been zapped!" 5 times. Once the loop is done, it then proceeds to continue with the rest of the script - ending with "no more zaps"

Now what if you wanted to let the player know how many times they have been zapped? Granted you could put in a definition that counts up each loop, but `repeat` already does that for you. All you need to add is the `as:` argument to the repeat command like so.

```dscript_green
my_zap_task:
    type: task
    script:
    - repeat 5 as:count:
        - strike <player.location>
        - narrate "you have been zapped <[count]> times!"
    - narrate "no more zaps"
```

The narrate would now say "you have been zapped 1 times!", "you have been zapped 2 times!", etc... up to 5.

You can try these examples in-game via `/ex run my_zap_task`.

### The Foreach Command

While the repeat command is handy, a lot of the times you would find yourself wanting to loop over the contents of a list, in that for each item in the list, do something.

Let's say we want to tell the player where all the cows are around them
Now, you can use the repeat command for this by doing this...
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
```
- foreach (some list) as:(definition to store item):
    - (commands here)
    - (will loop per item in list)
```

Now lets see how we can simplify that script with a `foreach` loop

```dscript_green
my_cow_task:
    type: task
    script:
    - foreach <player.location.find_entities[cow].within[30]> as:cow:
        - narrate "There's a cow just <[cow].location.distance[<player.location>].round> blocks away!"
        - playeffect effect:fireworks_spark at:<[cow].location> visibility:50 quantity:100 data:0 offset:3
```

Much better. Most notably, we dont have have to get the item `cow` from the list, its already defined.
In addition, foreach has a built-in definition of `<[loop_index]>` that keeps track of how many times it has looped.

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

There may be a few times where neither the repeat nor the foreach command work, because you dont know how many times it should loop, you just have a condition of when to stop.

This can be thought of as an `if` command but as a loop. The difference is that the `if` command simply runs the block if its true, the `while` command run the block as long as the condition is true 
```
- while (condition):
    - (commands here)
    - (will loop while condition is true)
```
The condition format is the same format as the `if` command, see that guide page for more details on the structure.

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

You can try this in-game via `/ex run my_move_task`. This task when run will keep telling you to move away until you have moved 3 blocks away from when you first were.

Note that there is a `wait` command here. This is a command that tells the script to pause for a certain amount of time (2 seconds in this case) and will be discussed more later. However it is important to use for while loops, without it it will try to check as much as it can all at the same time, which can cause the server to crash.

As a word of warning, `while` loops should be avoid if possible. It is very easy to make what is known as an infinite loop, in that the loop will never have a chance to stop. Once its running, it is very hard to force it to stop beyond just stopping the server.

### Stop The Loop

Sometimes in loops you only want to keep looping until you reach a certain point, however not necessarily stop the script. While `stop` is used to stop scripts entirely, `repeat/foreach/while stop` is used to stop the relevant loop

For instance in the first example we had, if we wanted to stop sending ligtning if the player had less than 5 health we would do as follows

```dscript_green
my_zap_task:
    type: task
    script:
    - repeat 5 as:count:
        - strike <player.location>
        - narrate "you have been zapped <[count]> times!"
        - if <player.health> < 5:
            - repeat stop
    - narrate "no more zaps"
```
Take note, only the loop stops, the end `narrate` line still runs.

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

There are times where you want to skip to the next loop without running the rest of the current loop. For that you use `repeat/foreach/while next`

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
