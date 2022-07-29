Blurring The Line Between Commands And Tags: Procedure Scripts
--------------------------------------------------------------

```eval_rst
.. contents:: Table of Contents
    :local:
```
### Procedure Basics

You may be working on a project and find that there is a piece of code that you write often, that you'd like to be able to neatly package up into a single tag. Maybe you have some math that you don't want to copy paste, or you have a script that generates a custom name for items or NPCs.  They can be broken down into two pieces:

#### Procedure Script

A procedure script is where you lay out your logic. Using the examples from before, this is where you'd write the math equation, or where the random name generation code would go. The following is an example script that will get a list of 9 locations, centered on the one that was given to the script.

```dscript_green
# This is the name of the procedure script. When it is being used, it is referenced via this name.
surrounding_blocks:
    # type is required, so that Denizen knows what sort of script this is
    type: procedure
    # debug is optional, and allows you to turn the debug on or off for a this specific script
    debug: false
    # definitions are optional; if you need to pass something in, you can specify the name of the
    # definitions here, and seperate them using pipes, if you want to pass in more than one thing.
    # Here, we are passing in a single value, called "center".
    definitions: center
    # All of our logic falls under the script tag
    script:
    - repeat 3 as:x:
        - repeat 3 as:z:
            - define blocks:->:<[center].add[<[x].sub[1]>,0,<[z].sub[1]>]>
    # A procedure script MUST determine something.
    - determine <[blocks]>
```

#### Procedure Tag

This is what to use to get the result from a procedure script. Continuing with our math and name generating example, when I want the answer from my math equation, or I want to generate a name, I would use the procedure tag the same way I would use any other tag in Denizen. The following example is one use case using the `surrounding_blocks` procedure that from before.

```dscript_green
# Get a 3x3 at the players feet location
- define locations <player.location.proc[surrounding_blocks]>
# save the materials that were there
- define old_blocks <[locations].parse[material]>
# turn them into stone
- modifyblock <[locations]> stone
- wait 3s
# turn them back into whatever materials they were before
- modifyblock <[locations]> <[old_blocks]>
```

Procedure tags give scripters a way to break up their code into more managable chunks, and to keep themselves from having to repeat their code too often. We've managed to make a neat platform spawning mechanic with only a few lines of code, and we've neatly packaged away our some of the more confusing parts. Rather than having to think about the specifics of how to accomplish our task, we can focus more broadly on what we want to do instead!

There a couple different ways to use a procedure tag, with some differences that are worth being aware of. This first one is the most simple way of getting a value from a procedure script.

```dscript_green
- define my_value <proc[my_procedure_script]>
```

If you wanted to pass something into your procedure script, you can use the `.context` portion of the tag, which might look something like this:

```dscript_green
- define my_value <proc[my_procedure_script].context[apple|orange|lasanga]>
```

That will pass in three three values, `apple`, `orange` and `lasanga` into the procedure script, and assign them whatever definitions were written in the `defintions` key. You can pass virtually anything into a procedure script. If you only have a single value to pass in, you may also find it easier to use this shortened version of the tag:

```dscript_green
- define fruit apple
- define my_value <[fruit].proc[my_procedure_script]>
```

This will pass `apple` into the procedure script, and it will be the first definition in the `definitions` key. You can also combine the shorter version and the context, if you so choose.

It's important to note that the context key may not function exactly like you expect it to, when it comes to passing in a list. If we were to use the short version of the procedure script, and passed in the list, it would function as one might expect; setting the first definition from the `defintions` key to the list. However, if you were to place the list into the context key, it will not pass the whole list in as one value, but as seperate, individual values. The following are two visual examples of this. Assuming that `colors` is a list with `red`, `brown` and `green`:

```dscript_green
# Our three definitions will be the colors list, apple, and 14
- define my_value <[colors].proc[my_procedure_script].context[apple|14]>
```

```dscript_yellow
# Our three definitions will be the three colors in the list
- define my_value <proc[my_procedure_script].context[<[colors]>|apple|14]>
```

There are ways around this, such as double wrapping your lists with list_single and unwrapping it in the procedure script, or turning your list in to a comma separated element, then splitting the list back apart, or just having one map argument that contains all the different definitions you want. Ultimately it's up to you to determine what is best for your use case. 
### Tasks vs Procedures

Procedures are not dissimilar from tasks, but there a few important differences to be aware of.

#### Side Effects

Procedure scripts can **not** change external state. That is, a procedure script cannot change anything at all, only determine a value. Things that count as a side effect are things like placing a block, removing/adding a mob, loading files from your computer, setting a flag, and so on. It's important that when you run a procedure tag, that it does not affect anything; it can and most likely will read values, but should *not* be writing any values. That means, ultimately, there are very few commands that can be used in a procedure tag. `define` and `determine`, control flow commands like `if` and `foreach`, and debug are just about all you can use in a procedure tag.

#### Returning Values

While task scripts *can* optionally return a value when it's done running, a procedure tag **has** to return a value. Tasks are like a thing that needs to be done, while a procedure is more like a question that is being asked. If you were needed to mow the lawn, you'd do the **task** of mowing the lawn, but once you were done, you could go on doing something else. You *might* let them know that you finished, or tell them how long it took, but those are *NOT* required to do the task of mowing the lawn. However, if you were asked a question by a teacher, then giving an answer is not only expected, it's **required**.

While task scripts do have the ability to return values, it is more cumbersome than using a procedure. In the following examples, there is a procedure and a task, and they both find all the fruits in a sentence, and give them back to us in a list. We're going to pick one at random and narrate it back to the player.

```dscript_yellow
# run the task, and save the result. We also need to specify waiting for the task to finish
- ~run get_fruits def:<context.message> save:fruit_list
# get the saved list, get the queue, then the determination, and a random entry from that determination
- narrate "No way, I like <entry[fruit_list].queue.determination.random> too!"
```

```dscript_green
# read out the sentence
- narrate "No way, I like <context.message.proc[get_fruits].random> too!"
```

#### Order of Operations

While both tasks and procedures have a script component, and a way to run that component, tasks are run with a command; either the `inject` or `run` command, and can run in parallel with other code. Procedures, on the other hand, are run whenever their tag is processed, which can be more or less than you might think, or at times that you didn't expect.

Ultimately, this means that you will have to be more aware of scripts that could cause lag on the server. The following is an example that wouldn't cause a problem with a task script, but *would* cause a problem with a procedure script.

```dscript_green
- narrate "What's the millionth digit of pi? Hmm..."
# Get the millionth digit of pi. Using the wait operator will wait for the task to finish,
# but other things on the server will keep processing, so there won't be any lag.
- ~run digit_of_pi def:1000000 save:digit
- narrate "Ya, the millionth digit is <entry[fruit_list].queue.determination.first>."
```

```dscript_red
- narrate "What's the millionth digit of pi? Hmm..."
# The server will hang as it is busy processing this procedure script so it can run the narrate.
- narrate "Ya, the millionth digit is <proc[digit_of_pi].context[1000000]>."
```
### When To Use

While tasks and procedures are similar, they both have things they are useful for. So, if you are:

- trying to write something that doesn't need a response
- Want to write something that might take a long time to get an answer
- Have code you want to package up that affects the world in some way

then you should use a task script. But if you want:

- something that doesn't affect the world, but has lots of logic that you want to package up
- Want to have something to keep your code short and neat
- Something that is always going to give you an answer

Then you should use a procedure. 
### Related Technical Docs

If you want to read a lot more about procedure scripts, the procedure tag, and its options, here are a few technical guides you might consider...

Note: most users, especially those learning from the Denizen for the first time, should just continue on to the next guides page. These references might be of interest to later come back to after you've learned Denizen as far as this guide teaches.

- [Procedure script doc](https://meta.denizenscript.com/Docs/Languages/procedure%20script%20containers)
- [Proc tag doc](https://meta.denizenscript.com/Docs/Tags/proc)
- [Proc.context tag doc](https://meta.denizenscript.com/Docs/Tags/proc.context)
