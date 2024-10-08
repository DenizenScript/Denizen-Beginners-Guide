Working With and Building Denizen
---------------------------------

```eval_rst
.. contents:: Table of Contents
    :local:
```

### Prerequisites

Make sure you have the following tools installed on your machine:

- Some form of git. We recommend [GitHub Desktop](https://desktop.github.com/) <span class="parens">(if you're using Linux, don't worry, there's probably a package for your distro)</span>.
- [IntelliJ IDEA](https://www.jetbrains.com/idea/). This editor is specifically designed for Java projects and will handle dependencies on its own.

### Building Spigot

To build Denizen, you'll also need to build the supported versions of Spigot, which you can find on the [project README](https://github.com/DenizenScript/Denizen#readme). To do this, Spigot provides a tool called [BuildTools](https://www.spigotmc.org/wiki/buildtools/). This cannot be substituted with prebuilt jars or forks, as it must be built into your local maven repo.

Follow the setup instructions and then run the BuildTools jar for each version supported by Denizen. This should be a command like `java -jar BuildTools.jar --rev 1.21.1 --remapped`.

### Building Denizen

1. Clone the Denizen repository: https://github.com/DenizenScript/Denizen
2. Open the cloned folder with IntelliJ.
3. Open the Maven tab, select `denizen-parent`, and click "Run Maven Build" <span class="parens">(the green arrow)</span>.

After building, the jar will be available in the `target` folder. You can stick this into your test server's plugins folder and all of Denizen should be available. You can repeat step 3 to build the project after making any desired changes.
