FAQ For Programmers
-------------------

This page will answer some common questions from programmers learning Denizen. These topics will not necessarily make much sense to those without a programming background.

```eval_rst
.. contents:: Table of Contents
    :local:
```

### Is Denizen Similar To (Programming Language Here)?

If **(Programming Language Here)** Is C/C#/Java/JavaScript/anything else in that range, the answer is firmly "no". For the rest, consider the following common comparisons made to Denizen:

In terms of purely how it appears visually, Denizen often is said to be similar looking to Python.

In terms of logic, Denizen is very similar to Bash or other command-line scripting languages.

To understand why, it's important to know the basic categories of programming language syntax:

- Functional syntax <span class="parens">(not to be confused with functional programming, which is different)</span> is the syntax most modern programmers know. It's used in C, C++, C#, Java, JavaScript, and a whole lot of others <span class="parens">(all "C Syntax" languages are in this category)</span>. This category is characterized, naturally, by all code being inside functions <span class="parens">(or "methods")</span> and primarily consisting of calls to other functions. This is generally done with a format using parenthesis and comma-separated arguments, like `SomeFunction(arg1, arg2)`. **Python** is not "C Syntax", but is still functional syntax.
- Various other core syntax categories exist <span class="parens">(such as those used in LISP, Haskell, Ruby, etc.)</span> exist but are unimportant to this point.
- Command+Tag syntax is the syntax every sysadmin learns in one form or another. This syntax is characterized with a natural tendency to work well when typed into a command line, formed from a series of lines that have a command followed by a list of (usually space-separated) arguments, interpretting all input as raw values, but having some special character that means some subsection of the input is to be processed as some lookup call and the result replaces that spot. This is the syntax used by Bash, CommandPrompt, PowerShell <span class="parens">(mostly)</span>, and of course... Denizen.

Consider for example, the Bash line `ls -la $FOLDER` - this runs the command named `ls` <span class="parens">(list files)</span> with the first argument being the raw text `-la` <span class="parens">(that will be interpretted as list style flags)</span> and the second argument prefixed with the $ symbol indicating that it should be looked up from the environment variable list <span class="parens">(presumably some variable containing a relevant folder path)</span>. The `$FOLDER` input will be replaced with an actual path, and the executed command will end up like `ls -la mydir/`.

Denizen fits this same basic syntax category... consider for example the Denizen line `narrate "hello there!" targets:<[players]>` - this runs the command `narrate` with the first argument being the raw text `hello there!` (that will be interpretted as a message to show) and the second argument using `<>` to indicate a tag lookup, and `[]` to indicate a definition lookup <span class="parens">(presumably some list of players)</span>. The executed command will end up like `- narrate "hello there!" targets:li@p@bob|p@joe`.

### Is Denizen OOP?

Short answer: **No.**

Medium answer: Denizen is object-based, but not object-oriented-only.

Long answer: Denizen does not fit the category of 'purist OOP' <span class="parens">(like Java)</span> nor 'multi-paradigm but can be OOP' <span class="parens">(like C#)</span>.

Denizen uses objects to represent all data, which makes it object-based. Denizen also allows you to define your own object types, but actively discourages doing so.

Denizen is designed to work with very terse quick lines <span class="parens">(you can accomplish entire relatively complex goals in a script containing a single-digit number of lines, thanks to the numerous time-saver do-it-all utility commands available)</span>, and the naturally long-winded nature of OOP is inherently in opposition to this goal. Going to the trouble of rigidly defining custom object types simply doesn't carry much advantage in a language where most created methods/functions would be only 1 or 2 lines long anyway. In addition, defining long careful objects will cause you to write long, complicated scripts that, within the syntax of Denizen, will end up being much more confusing to follow than if you just wrote the imperative logic directly.

### Is Denizen Open Source?

Denizen is 100% Free-and-Open-Source-Software (FOSS), under the MIT License.

We strongly believe that publishing the full readable, hackable, and buildable source for our work is inherently beneficial to the general good: It grants near-unlimited freedom to our users, it allows anyone with skill to contribute to making Denizen be the best it can be, and it ensures that the project will last and still be available to users even if something happens that disrupts the project's normal development <span class="parens">(eg existing developers cease work on it, or if the project is taken over by anyone that wouldn't publish it under fair terms)</span>.

The Denizen implementation for Spigot is on GitHub [here](https://github.com/DenizenScript/Denizen). The core code for Denizen is [here](https://github.com/DenizenScript/Denizen-Core). You can also find the source of this very guide [here](https://github.com/DenizenScript/Denizen-Beginners-Guide). You might also be interested in the meta-doc-helper-bot for Discord [here](https://github.com/DenizenScript/DenizenMetaBot) or the VS Code extension [here](https://github.com/DenizenScript/DenizenVSCode).

### Can I Pull-Request Something To Denizen?

Sure! We've accepted a lot of pull requests from a variety of contributors over the years. We ask that you discuss what you intend to PR [on the Discord](https://discord.gg/Q6pZGSR) before making it though, to avoid wasting your time on something that is already available, or just to make sure you know how to go about the specific task properly.

When you make a Pull Request, you will be automatically asked to accept a CLA that says you agree that your contributions are given fully to the Denizen project, and that you accept that you can never prevent or restrict usage of that contribution after it's been pulled. We have this in place to help ensure that Denizen always remains free and unrestricted for everyone.
