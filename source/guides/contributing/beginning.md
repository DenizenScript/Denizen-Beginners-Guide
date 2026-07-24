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

You must build Spigot on your computer before you can work with Denizen. To do this, download Spigot's [BuildTools](https://www.spigotmc.org/wiki/buildtools/). Once you have it, you will build each version listed in the [project README](https://github.com/DenizenScript/Denizen#readme) one at a time. You can use the tool's GUI, being sure to select `remapped` in the options menu prior, or you may use the command line with a command like `java -jar BuildTools.jar --rev 26.2 --remapped`. This will take a few minutes for each build. You don't need to keep the final jars outputted, though you may find them useful for your local test server; the building process creates files in your home directory the IDE will use later.

### Getting your Project Set Up

Once you have the requisite software, you'll need to get a copy of Denizen of your very own to make changes to! You'll need to make a `fork` of Denizen. It's generally easiest to do this on the GitHub website. You can find [Denizen's Repository](https://github.com/DenizenScript/Denizen) here to do so. From there, clone the repository to your computer. In GitHub Desktop, you can do this with the repository dropdown in the top left. This will copy all the files to your computer. You can then open the whole folder you just made with IntelliJ and browse the files. Don't worry if it's confusing right now!

### What Do You Start With?

Now that you have Denizen's file in front of you, you'll need to decide what you want to work on! If you don't have any prior experience working in Java, we suggest that you begin by adding or changing a tag, mechanism, or event. These components are designed to be easy to build on and there are lots of examples for you to look at or even copy as a starting place. The best place to start is in the Denizen Discord server's Denizen channel, where you can select the `Easy PR` tag to filter for posts that the helpers believe would be good for newer contributors! Once you have one in mind, you can use that thread to either mention that you'll be starting work on it, or to ask questions if you need. You may find [this page on properties](https://guide.denizenscript.com/guides/contributing/property-dev.html) useful if you're starting with a tag or mechanism.

### Your First PR

Once you know what you'll be doing, you need to create a new branch in your git repository. Name it something related to what you're working on, but the specific name doesn't matter. You're then set to start editing code. You'll find some of the other pages of this guide helpful for implementing and testing the change, but this page focuses on the process, so we'll assume that you've finished successfully and are ready to submit it for review. You need to commit and push your changes. Once you've done that, GitHub desktop or web make it easy to submit a pull request to the main Denizen repository. Make sure to name it descriptively with what you changed, and include a reference to the thread originally requesting it. It's nice to also make another comment in the original thread with a link to your new PR. 

### What to Expect Now

After you submit your PR, it will appear for review by existing contributors. Depending on circumstance, this review could take anywhere from minutes to a few days. Most likely, you'll get one or more comments on your pull request. You can review these on GitHub and respond to them. We try to be extra thorough with newer contributors to help you learn good practices and improve your abilities, so don't be discouraged if it seems like you're getting a lot of feedback; we want to help! Also, don't take initial comments as law. If you disagree, feel free to share why you did it one way instead of another. Once you've resolved all the comments, your pull request can be merged and incorporated into Denizen. You'll likely get a mention later in the Discord and everyone will be able to use your change! You may get the ability to chat in the contribution channel as well, which you can use to discuss your PRs in the future or ask questions.
