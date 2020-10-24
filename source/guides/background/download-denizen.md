How Do I Download Denizen?
--------------------------

```eval_rst
.. contents:: Table of Contents
    :local:
```

### Requirements

Before you use Denizen at all, there is one basic requirement: You need to be running a Spigot server on a recent minecraft version.

That means a Spigot server or fork thereof (like Paper), as opposed to a vanilla server, a Forge server, or some other platform.

What constitutes a "recent version" changes with time of course, but generally that means the current version of minecraft - but if you're one or two major versions behind, that's fine. Note that you must always be on the latest *minor* version though. Minecraft versions are of the format `1.major.minor`, so in `1.15.2`, `15` is major and `2` is minor. If `1.15.2` is the current latest version, then `1.15.2` is a good version, but `1.15.1` is unsupported, and `1.15` (implied `.0`) is also unsupported. `1.14.4` (ie, latest minor version of the previous major version) is also supported. Versions older than this are also supported sometimes. At time of writing, the supported versions are `1.15.2`, `1.14.4`, `1.13.2`, and `1.12.2`. Note that these versions are just examples, and this page will not be updated with new Minecraft releases. Check the Discord's news and changelog channels for information about current version support.

### Chocolate Or Vanilla?

Denizen downloads come in two "flavors": Release, and Development.

Release builds are expected to be stable and reliable, while dev builds are expected to be unstable and potentially even have major server-breaking issues in some builds.

Generally, your main public/live server should use only the release builds. Your test/dev servers *can* use dev builds, but are often better off running release builds. If you choose to use a dev build on your test server, you are expected to update the build every few days at most - if you ask for help on our support channels while running a dev build from more than a few days ago, the first thing we'll tell you is to stop running dev builds as they're clearly not for you.

[Release Builds Can Be Downloaded Here](https://ci.citizensnpcs.co/job/Denizen/)

[Developmental Builds Can Be Downloaded Here](https://ci.citizensnpcs.co/job/Denizen_Developmental/)

### Don't Touch That Spigot Resource

We maintain a Spigot Resources [here](https://www.spigotmc.org/resources/denizen.21039/) page for the sake of public visibility, but it is not updated often and its builds should not be used. Updates are only pushed to Spigot for the purpose of keeping the resource page alive.
