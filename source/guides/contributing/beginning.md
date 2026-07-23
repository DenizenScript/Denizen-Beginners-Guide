How to Start Contributing to Denizen
---------------------------------

```eval_rst
.. contents:: Table of Contents
    :local:
```

### Do you Need to Know Java?

No! You can begin contributing to Denizen without any prior experience. You'll begin with simple contributions that will help you learn what you need for more advanced topics. You'll find that your experience with DenizenScript will help greatly in understanding Denizen's internals.


### What Do You Need to Start?

#### Software

To begin, you'll need software designed for Java development and Git, in order to bring Denizen to your own computer and submit changes. 

For the IDE<span class="parens">(code editor)</span>, we strongly recommend [IntelliJ IDEA](https://www.jetbrains.com/idea/). This editor is specifically designed for Java projects and will handle dependencies on its own.
We suggest using GitHub Desktop, as it allows you to view and manage changes much more easily than the command-line tool.

#### Spigot

You must build Spigot on your computer before you can work with Denizen. To do this, download Spigot's [BuildTools](https://www.spigotmc.org/wiki/buildtools/). Once you have it, you will build each version listed in the [project README](https://github.com/DenizenScript/Denizen#readme) one at a time. You can use the tool's GUI, being sure to select `remapped` in the options menu prior, or you may use the command line with a command like `java -jar BuildTools.jar --rev 26.2 --remapped`. This will take a few minutes for each build. You don't need to keep the final jars outputted, though you may find them useful for your local test server; the building process created files in your home directory the IDE will use later.

### Getting your Project Set Up

Once you have the requisite software, you'll need to get a copy of Denizen of your very own to make changes to! You'll need to make a `fork` of Denizen. It's generally easiest to do this on the GitHub website. You can find [Denizen's Repository](https://github.com/DenizenScript/Denizen) here to do so. From there, clone the repository to your computer. In GitHub Desktop, you can do this with the repository dropdown in the top left. This will copy all the files to your computer. You can then open the whole folder you just made with IntelliJ and browse the files. Don't worry if it's confusing right now!