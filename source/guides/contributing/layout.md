Denizen's Project Layout
------------------------

```eval_rst
.. contents:: Table of Contents
    :local:
```

**Denizen** is a plugin for Minecraft servers that parses and interprets a scripting language called **DenizenScript**. The most popular implementation of Denizen is the Spigot implementation, which is the jar you've most likely downloaded many times. At the time of writing, it is the *only* maintained implementation.

### Repository Modules

Denizen uses a multi-module Maven setup. The primary directories you will encounter in the repository are:

- `plugin`: Contains the core logic, tags, commands, and script events. Most pull requests belong in `plugin/src/main/java/com/denizenscript/denizen/`.
- `paper`: Contains Paper-specific tags, events, and API features.
- `v1_17` through `v26_2`: Contain version-specific NMS code for direct server internals.
- `dist`: Bundles all modules into the final compiled jar.

### Associated Projects

Any Denizen implementation depends on **DenizenCore**, which is the main set of tools that powers every language feature. It includes all content that isn't implementation-specific, such as basic ElementTag manipulation and data script containers.

Support for other plugins within Denizen scripts is provided by **Depenizen**. It uses the tools provided by both DenizenCore and Denizen to interact with external APIs. This is also the case for **dDiscordBot**, although it focuses on a single API <span class="parens">(that being Discord)</span>.

### What to Contribute

As a new contributor, you might wonder what kind of changes you should focus on. In general:

- Adding, changing, improving, or fixing **tags, mechanisms, commands, and events** is considered the range of what anyone can contribute and is a great place to start.
- More advanced features, such as deep core functionality or things that aren't implementation-specific (like `DenizenCore`), should be avoided until you are more familiar with working in the codebase.
- Start with the "easy" stuff to gain the experience needed to tackle medium or advanced features later!

### Finding Existing Source Code

Unless you're going to be working with core language features, most of your code will be recognizably similar, and you can find numerous examples throughout these projects for each type of contribution.

**Tip:** You can easily find existing source code using the [Meta Docs](https://meta.denizenscript.com). Searching for any tag or command on the site provides a direct source link at the bottom of the page, pointing to the exact Java class and line number in the repository.
