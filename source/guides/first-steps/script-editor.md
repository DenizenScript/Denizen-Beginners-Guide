Setting Up Your Script Editor
-----------------------------

```eval_rst
.. contents:: Table of Contents
    :local:
```

### The Editor

![](images/scripteditor.png)

The officially recommended way to edit Denizen scripts is using VS Code, with the Denizen extension!

### Installation

- First, download and install [VS Code](https://code.visualstudio.com/). Note that this is NOT "Visual Studio" despite half of its name being that. <span class="parens">(The naming is rather confusing, unfortunately. Microsoft's doing...)</span>
- Second, after VS Code is installed, you can install the [Denizen extension](https://marketplace.visualstudio.com/items?itemName=DenizenScript.denizenscript) by clicking the green "Install" button on the linked page.
- You also need [.NET Core 3.1+](https://dotnet.microsoft.com/download/dotnet-core/3.1/runtime). This is used to power tools like automatic script checking and meta validation. <span class="parens">(Mac users, use [this link instead](https://dotnet.microsoft.com/download/dotnet-core/3.1).)</span>

### Usage

- Open your scripts folder with VS Code - that's `plugins/Denizen/scripts/` within your server directory <span class="parens">(the folder itself, not individual files - you can see the file tree on the left side of the editor)</span>.
- The Denizen extension will automatically be active on any files that have the `.dsc` file extension. <span class="parens">(note: historically, the `.yml` extension was used for scripts. This is no longer a recommended file extension, and `.yml` files will not have Denizen script highlighting. You must use `.dsc`).
- For the most part, just start editing your script files the same way you would edit any text file within VS Code.
