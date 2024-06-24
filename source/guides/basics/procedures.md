Blurring The Line Between Commands And Tags: Procedure Scripts
--------------------------------------------------------------

```eval_rst
.. contents:: Table of Contents
    :local:
```

### Procedure Basics

You may be working on a project and find that there is a section of script that you write often, that you'd like to be able to neatly package up and reuse. Maybe you have some math that you don't want to copy/paste, or you have a script that generates a custom name for items or NPCs. You've already learned about using `task` scripts for reusable sections of script that can be called in one line with the `run` command, but what about something even smaller and easier to use? Meet: **Procedure** scripts!

They can be broken down into two pieces:

#### The Procedure Script Container

A procedure script is where you lay out your logic. Using the examples from before, this is where you'd write the math equation, or where the random name generation code would go.

A procedure script usually has one or more input definitions <span class="parens">(just like the inputs to a `task`)</span>, but doesn't have to. A procedure must, however, always `determine` an output.

The following is an example script that will get a list of 9 locations, centered on the one that was given to the script.

```dscript_green
surrounding_blocks:
    type: procedure
    definitions: center
    script:
    - repeat 3 as:x from:-1:
        - repeat 3 as:z from:-1:
            - define blocks:->:<[center].add[<[x]>,0,<[z]>]>
    # A procedure script MUST determine something.
    - determine <[blocks]>
```

#### Procedure Tag

A `proc` tag is what to use to get the result from a procedure script. Continuing with our math and name generating example, when I want the answer from my math equation, or I want to generate a name, I would use the procedure tag the same way I would use any other tag in Denizen. The following example uses the `surrounding_blocks` procedure script shown above in some other script.

```dscript_green
some_script:
    type: task
    script:
    # Get a 3x3 at the player's feet location
    - define locations <player.location.proc[surrounding_blocks]>
    # turn them into fake stone for a couple seconds
    - showfake <[locations]> stone d:2s
```

Procedure tags give scripters a way to break up their code into more manageable chunks, and to keep themselves from having to repeat their code too often. We've managed to make a neat fake-platform spawning mechanic with only a few lines of code, and we've neatly packaged away our some of the more confusing parts. Rather than having to think about the specifics of how to accomplish our task, we can focus more broadly on what we want to do instead!

There a couple different ways to use a procedure tag, with some differences that are worth being aware of.

This first one is the simplest way of getting a value from a procedure script with no extra inputs<span class="parens">(the `proc` form)</span>:

```dscript_blue
# This assumes 'my_procedure_script' has no input 'definitions' at all
- define my_value <proc[my_procedure_script]>
```

If you wanted to pass something into your procedure script, you can use the `.context` portion of the tag, which might look something like this<span class="parens">(the `proc.context` form)</span>:

```dscript_blue
# This assumes 'my_procedure_script' has 3 simple input 'definitions'
- define my_value <proc[my_procedure_script].context[apple|orange|lasagna]>
```

That will pass three values (`apple`, `orange` and `lasagna`) into the procedure script, and assign them whatever definitions were written in the `definitions` key. You can pass virtually anything into a procedure script.

If you only have a single value to pass in, you may also find it easier to use this shortened version of the tag <span class="parens">(the `ObjectTag.proc` form)</span>:

```dscript_blue
# This assumes 'my_procedure_script' has 1 simple input definition
- define fruit apple
- define my_value <[fruit].proc[my_procedure_script]>
```

This will pass `apple` into the procedure script, and it will be the first definition in the `definitions` key. You can also combine the shorter version and the context, if you so choose.

It's important to note that the context key may not function exactly like you expect it to, when it comes to passing in a list. If we were to use the short version of the procedure script, and pass in a list, it would function as one might expect; setting the first definition from the `definitions` key to the list. However, if you were to place the list into the context key, it will not pass the whole list in as one value, but as separate, individual values. The following are two visual examples of this. Assuming that `colors` is a list with `red`, `brown` and `green`:

```dscript_blue
# Our three definitions will be the colors list, 'apple', and '14'
- define my_value <[colors].proc[my_procedure_script].context[apple|14]>
```

```dscript_red
# Our three definitions will be the three colors in the list, while 'apple' and '14' will be ignored or corrupted
- define my_value <proc[my_procedure_script].context[<[colors]>|apple|14]>
```

There are ways around this, such as wrapping your lists with `list_single`, or turning your list into a comma separated element, then splitting the list back apart, or just having one map argument that contains all the different definitions you want. Ultimately it's up to you to determine what is best for your use case.

For more on this potential issue, refer to the [common mistakes section on Object Hacking](/guides/troubleshooting/common-mistakes#object-hacking-is-a-bad-idea).

### Tasks vs Procedures

Procedures are not dissimilar from tasks, but there a few important differences to be aware of.

#### Side Effects

Procedure scripts can **not** change external state. That is, a procedure script cannot change anything at all, only determine a value. Things that count as a side effect are things like placing a block, removing/adding a mob, loading files from your computer, setting a flag, and so on. It's important that when you run a procedure tag, that it does not affect anything; it can and most likely will read values, but should *not* be writing any values. That means, ultimately, there are very few commands that can be used in a procedure tag. `define` and `determine`, control flow commands like `if` and `foreach`, and debug are just about all you can use in a procedure tag.

This is the same limitation that applies to all **tags** in Denizen. It applies to procedures because that's exactly what a procedure script is: a custom tag!

#### Returning Values

While task scripts *can* optionally return a value when it's done running, a procedure tag **has** to return a value. Tasks are like a thing that needs to be done, while a procedure is more like a question that is being asked. If you were needed to mow the lawn, you'd do the **task** of mowing the lawn, but once you were done, you could go on doing something else. You *might* let them know that you finished, or tell them how long it took, but those are *NOT* required to do the task of mowing the lawn. However, if you were asked a question by a teacher, then giving an answer is not only expected, it's **required**.

While task scripts do have the ability to return values, it is more cumbersome than using a procedure. In the following examples, there is a procedure and a task, and they both find all the fruits in a sentence, and give them back to us in a list. We're going to pick one at random and narrate it back to the player.

Here's the task version:

```dscript_yellow
get_fruits:
    type: task
    definitions: message
    script:
    - determine <[message].split.filter[is_in[orange|apple|banana]]>

task_example:
    type: world
    events:
        on player chats:
        # run the task, and save the result. We also need to specify waiting for the task to finish
        - ~run get_fruits def:<context.message> save:fruit_list
        # get the saved list, get the queue, then the determined list, and a random entry from that determination
        - narrate "No way, I like <entry[fruit_list].created_queue.determination.first.random.if_null[nothing]> too!"
```

And here's the procedure version:

```dscript_green
get_fruits:
    type: procedure
    definitions: message
    script:
    - determine <[message].split.filter[is_in[orange|apple|banana]]>

proc_example:
    type: world
    events:
        on player chats:
        # read out the sentence
        - narrate "No way, I like <context.message.proc[get_fruits].random.if_null[nothing]> too!"
```

Notice that the `get_fruits` is basically the same, but the `proc_example` event is much simpler.

#### Order of Operations

While both tasks and procedures have a script component, and a way to run that component, tasks are run with a command like `inject` or `run`, and can run in parallel with other code. Procedures, on the other hand, are run whenever their tag is processed, which can be more or less than you might think, or at times that you didn't expect. A procedure can't wait: it must be able to fill its tag immediately, and will freeze the server if it takes too long to do so.

Ultimately, this means that you will have to be more aware of scripts that could cause lag on the server. The following is an example that wouldn't cause a problem with a task script, but *would* cause a problem with a procedure script.

This task usage should be quite smooth:

```dscript_blue
smooth_example:
    type: task
    script:
    - narrate "What's the millionth digit of pi? Hmm..."
    # Get the millionth digit of pi. Using the wait operator will wait for the task to finish,
    # but other things on the server will keep processing, so there won't be any lag.
    - ~run digit_of_pi def:1000000 save:digit
    - narrate "Ya, the millionth digit is <entry[digit].queue.determination.first>."
```

This procedure usage however might freeze up the server a bit:

```dscript_red
laggy_example:
    type: task
    script:
    - narrate "What's the millionth digit of pi? Hmm..."
    # The server will hang as it is busy processing this procedure script so it can run the narrate.
    - narrate "Ya, the millionth digit is <proc[digit_of_pi].context[1000000]>."
```

### When To Use

While tasks and procedures are similar, they both have things they are useful for.

A task script is usually better if you have something that:

- doesn't need a response
- might take a long time to get an answer
- affects the world in some way

And a procedure script is usually better if you have something that:

- doesn't affect the world
- is always going to give you an answer
- needs to be used from inside a tag

### Related Technical Docs

If you want to read a lot more about procedure scripts, the procedure tag, and its options, here are a few technical guides you might consider...

Note: most users, especially those learning from the Denizen for the first time, should just continue on to the next guides page. These references might be of interest to later come back to after you've learned Denizen as far as this guide teaches.

- [Procedure script doc](https://meta.denizenscript.com/Docs/Languages/procedure%20script%20containers)
- [Proc tag doc](https://meta.denizenscript.com/Docs/Tags/proc)
- [Proc.context tag doc](https://meta.denizenscript.com/Docs/Tags/proc.context)
- [ObjectTag.proc tag doc](https://meta.denizenscript.com/Docs/Tags/objecttag.proc)
- [Determine command doc](https://meta.denizenscript.com/Docs/Commands/determine)
