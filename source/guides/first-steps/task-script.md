Your First Task Script
----------------------

<!-- **TODO: Write-up that guides the user through writing a basic task script (just a task with a narrate line) using VS-Code, emphasizing things like file extension and placement. Also run it in-game with `/ex run`.** -->

```eval_rst
.. contents:: Table of Contents
    :local:
```

## Task script basics

A task script is a stand-alone script that can be run either via in-game command with the `/ex` command, as explained in [the guide to the /ex command](https://guide.denizenscript.com/guides/first-steps/ex-command.html).

Task scripts will run all of the Denizen commands that they include. A task script can be simple, it can be complicated, and it can even run other task scripts. This is useful to create logic-based script chains, like dialogue options or random content.

## Task script syntax

Here's an example of a basic task script.

```dscript_green
example_task:
    type: task
    script:
    - narrate "This is a basic task script!"
```

This script will narrate the text:

```
This is a basic task script!
```

to the player attached to the script. If you use the `/ex` command to run this script - specifically, by running `/ex run example_task` in-game, *you* will be the attached player.

You can also run a task script and manually specify the attached player. For example, to run this script for the player named `mcmonkey`, you would run this command: `/ex run example_task player:<server.match_player[mcmonkey]>`

The player is found by their username with the `<server.match_player[]>` tag, which returns a PlayerTag of the player whose username matches the text you put between the `[]` brackets. If this is confusing, don't worry! We'll talk more about tags later on - this is just an explanatory preview to give you an idea of what's coming. You can also return to it later on once you understand more about these concepts.

# Building your first task script in VS Code

Previously, you've learned how to create an environment in VS Code, the editor that we recommend for writing Denizen scripts.

## Creating the file

To create your first task script, start by opening your scripts folder in VS Code.

TKTK SCREENSHOT (open scripts folder)

From there, right click the scripts folder in the explorer menu and click the "New File" option.

TKTK SCREENSHOT (new file highlighted)

Once your file has been created, you can name it something like `MyTask.dsc`. Make sure to use the `.dsc` extension so VS Code recognizes it as a Denizen script, but the *name* of the file can be whatever you like. Usually, it's helpful to name the file something relevant to the script(s) that it contains.

From here, double-click the file to open it in VS Code.

TKTK SCREENSHOT (opened file)

Now you can begin writing your first task script!

## Writing the script

Let's start with the core of the script:

```dscript_blue
myfirsttask:
    type: task
    script:
    - narrate (sometext)
```

This example should look familiar - it's very similar to the example above.

### Script names

The name of the script here is `myfirsttask`. It's at the top of the indentation. Each top-level indentation entry is a separate script. Here is an example of two different scripts:

```dscript_green
myfirsttask:
    type: task
    script:
    - narrate "This is is task number one!"

mysecondtask:
    type: task
    script:
    - narratee "This is task number two!"
```

This example demonstrates what having two different scripts in the same file looks like. `myfirsttask` and `mysecondtask` are two different scripts, and each is a fully self-contained script that can be run with the `run` command, either via the `/ex` command in-game or in a Denizen script.

### Script types

Below the script name - on the second level of indentation - you'll see the `type` and `script` entries.

The `type` option is where you specify which `type` of Denizen script you're writing. In this case, we're writing a `task` script. You may have seen `world` scripts, `item` scripts, `inventory` scripts, and *maybe* even a `procedure` script. For now, let's focus on `task` scripts. Make sure you write `type: task` in your script on the second level of indentation, below the script name, like this:

```dscript_blue
myfirsttask:
    type: task
```

### Script commands

Below the `type` entry, you'll see the `script` entry. This is where you'll be doing most of your work in Denizen! Under the `script` entry is where you write the content of the script - no matter which kind of script it is, the `script` entry is where you tell Denizen what to do.

Let's look at another example script:

```dscript_green
myfirsttask:
    type: task
    script:
    - narrate "This is a valid task script!"
```

This script only has one `command` in it, the `narrate` command. As a reminder, `narrate` will display the specified text to the attached player. You can also specify a custom list of targets to `narrate` to if you want to `narrate` to multiple players!

Notice how the text we want to narrate - `This is a valid task script!` - is enclosed in `""` double quotes. Because the message we want to narrate has ` ` spaces in it, we enclose it in double quotes to make sure that the command only has one `argument`. Denizen `commands` have `arguments` that are separated by ` ` spaces. For example, `run one two three` has arguments `one`, `two`, and `three`, but `run "one two three"` only has one argument, `one two three`.

# Completed product

At this point, you should have a task script that's ready to run! Go on, give it a try - use the `/ex run (YourTaskName)` command to run the task in-game. For example, the in-game command to run the above script would be `/ex run myfirsttask`.

If you see the text that you wrote for the `narrate` command, you've successfully written your first task script. Congratulations!

TKTK SCREENSHOT (in-game script successfully run)