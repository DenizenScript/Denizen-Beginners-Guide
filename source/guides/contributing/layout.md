Denizen's Project Layout
------------------------

```eval_rst
.. contents:: Table of Contents
    :local:
```

**DenizenScript** is a language run by **Denizen**. The most popular implementation of Denizen is the Spigot implementation, which is the jar you've most likely downloaded many times. As of the time of writing, it is the *only* maintained impl.

Any Denizen implementation depends on **DenizenCore**, which is the main set of tools that powers every language feature. It does include some content that isn't specific to Minecraft implementations, such as basic ElementTag manipulation and data script containers.

Support for other plugins within Denizen scripts is provided by **Depenizen**. It uses the tools provided by both DenizenCore and Denizen to interact with external APIs. This is also the case for **dDiscordBot**, although it focuses on a single API <span class="parens">(that being Discord)</span>.

Unless you're going to be working with core language features, most of your code will be recognizably similar, and you can find numerous examples throughout these projects for each type of contribution.