Resource Packs - Custom Items And Sounds
-------------------

This page will answer some common questions from programmers interested in creating visually custom items and adding new sounds into a resource pack.
There are plenty of tutorials on creating your own resource pack, and less commonly how to implement custom model data and manage sounds within one.
This guide primarily, details how to correctly format your resource pack, and then implement it into Minecraft using Denizen scripts.

```eval_rst
.. contents:: Table of Contents
    :local:
```

### Inside The Root Directory

Directory: `.minecraft\resourcepacks\MyResourcePack\`

The main directory within your resource pack folder should contain both:
- The `Assets` Folder - This is where all your files are placed.
- `pack.mcmeta` - This is how Minecraft knows what format your Resource Pack is.
Optimally, you can also include `pack.png` - This is a `64x64` custom image for your pack!


#### Example File: `pack.mcmeta`

Inside the `pack.mcmeta` file, you will find this is formatted in a `json` format.
You need two named strings: `pack_format` and `description`.
Here is what it looks like inside:

```json
{
   "pack": {
      "pack_format": 5,
      "description": "My Fancy Resource Pack"
   }
}
```

##### pack.mcmeta File Key: `pack_format`

This is the indicator to Minecraft what version this pack is.
- `1` indicates versions `1.6` - `1.8`.
- `2` indicates versions `1.9` - `1.10`,
- `3` indicates versions `1.11` - `1.12`,
- `4` indicates versions `1.13` - `1.14`,
- `5` indicates versions `1.15` - `1.16`.

##### pack.mcmeta File Key: `description`

This can be blank, or you can optimally fill this with something fancy.
Unicode characters must be written pre-escaped, like this: `\uCODE`; two examples being:
 `\u2588` for `█`, and `\u00A7` for `§`, the section sign symbol which parses [valid color tags](https://minecraft.gamepedia.com/Formatting_codes) you use to parse colors in minecraft chat.
If you want red text, your text will look something like `\u00A74Dark Red!`.
*Note: Color before formatting; Formatting codes persist after a color code, Not vise-versa!*

You can find special characters in your Character Map.
If you're on a Windows operating system, `Start` > `Windows Accessories`.
If you're in Linux using GNOME and Unity, `Gucharmap character map` is a part of `GNOME desktop`.
If you run a Gnome desktop - you can access it in any of these following ways:
- Menu on the top of the screen, `(language)` > `Character Map`.
- `Gucharmap` in terminal.
- `Applications` > `Accessories` > `Character Map`.

You can also google search for unicode characters.

### Inside The Assets Folder Directory

Directory: `.minecraft\resourcepacks\MyResourcePack\assets\`

This directory should be empty except for the one folder directory: `minecraft`. 
Toss it in and leave everything else out of here.

### Inside The Minecraft Folder Directory

Directory: `.minecraft\resourcepacks\MyResourcePack\assets\minecraft\`

Depending on what content you plan on changing, you can create any of the following folders:

- blockstates - This is where each block-state of materials are saved.
- font - This is where font data is saved. This guide does not cover this.
- models - This is where the model data and files are saved.
- textures - This is where the texture image files are saved.
- fonts - This is where your font data is saved.
- sounds - This is where your sounds are saved.
- optifine - This is where your optifine data is saved. This guide does not cover this.

For Optifine support, it's recommended you join their discord and review their documentation at their [Github Source](https://github.com/sp614x/optifine/tree/master/OptiFineDoc/doc).

#### Example File: `sounds.json`
This file indexes where Minecraft should look for your sounds.
Below is an example of a setup for two custom sounds, `defence_levelup0` and `defence_levelup1`.

```json
{
  "entity.player.defence.level": {
    "sounds": [
      {
        "name": "custom/defence_levelup0"
      },
      {
        "name": "custom/defence_levelup1"
      }
    ],
    "subtitle": "Excited Trumpet Noises"
  }
}
```

The first key is the name for the sound; in this example, `entity.player.defence.level`.
The only data object within the command we need to specify are `sounds`.
Optionally, you can specify the subtitle that displays if subtitles are enabled in-game.
If you place multiple sounds within the `"sounds":[]` array, the sound will randomize between them based on their weight.
The file extension is `.ogg` - other formats are not compatible.

For each file, you will need the data: `"name":"FILEPATH/FILENAME"`, excluding the file's extension.
Optionally, you can manually adjust the following valid properties of the sound:
1) `volume` - The volume the sound will be played as. 
    - Default is `1.0`; Valid volume ranges from `0.0` to `1.0`; where `1.0` is the loudest it may be played at.
    - The Volume value accepts higher values using Denizen's PlaySound, however not by increasing the volume. It increases the audible distance the sound may be heard from. 
    - For example, volume 5 can be heard from five chunks away.
2) `pitch` - The pitch the sound plays at, altered from it's original `.ogg` form.
    - Default is `1.0`; Valid pitches range from `0.0` to `2.0`; where `1.0` is high-pitched and `0.0` will be low-pitched.
3) `weight` - The chance that this sound will be selected as opposed to randomly.
    - Default is 0; Only accepts valid integers, not adjustable within Denizen.
    - For example, putting 2 in for the value would be like placing in the name twice.
4) `stream` - Determines if the sound should be streamed from it's file.
    - Default is false.
    - Recommended to set this value as `true` if the sound is longer than two seconds to avoid lag.
    - Use this sparingly; it's not optimal to specify everything true.
    - This is used with all music disks.
5) `preload` - Determines if the sound should be loaded when loading the pack, as opposed to when the player plays the sound.
    - Default is false.
    - Used for ambient noises.
6) `attenuation_distance` - Determines the reduction rate based on distance.
    - Default is `1.0`.
    - Used by portals, beacons, conduits.
7) `type` - determines if a pre-defined event fires this sound.
    - Default is `sound`, the other option available is `event`.
    - `sound` causes the value of `name` to be interpreted as the name of a file
    - `event` causes the value of `name` to be interpreted as the name of an already defined event.
    - used for things like being under-water, in a cave, near a beacon, near a beehive.

### Inside The Blockstates Folder Directory

Directory: `.minecraft\resourcepacks\MyResourcePack\assets\minecraft\blockstates\`
To modify each individual block-state of an item, you must specify each individual blockstate.
Additional blockstates cannot be specified.
When specifying blockstate models, the relative folder directs to the `Models` directory, located at `\assets\minecraft\models\`
Adjusting these are not covered in this guide.

### Inside The Models Folder Directory

Directory: `.minecraft\resourcepacks\MyResourcePack\assets\minecraft\models\`
To "Create" new items, you will need to modify existing items within Minecraft.
This can and was previously done with Durability, but optimally utilized with `custom_model_data` that was implemented in Minecraft 1.14.
The three object model types for model data are `Block States`,`Block Models`, and `Item Models`.
Block States and Block Model data are not covered in this guide.

#### Example File: `wooden_sword.json`

Existing files such as `wooden_sword` for example, should look like this:

```json
{
    "parent": "item/handheld",
    "textures": {
        "layer0": "item/wooden_sword"
    }
}
```

The above example is `wooden_sword.json`, which is located at `\assets\minecraft\models\item\wooden_sword.json`
The `parent` key indicates the model data this file injects data for.
The data's value for parent specified are the `FILEPATH/FILENAME` from the `models` directory if specifying a model file,
and the `textures` directory if specifying a texture. 

In the above example, the `wooden_sword` utilizes the parent model located at: `\assets\minecraft\textures\item\handheld.json`
In the above example, the `wooden_sword` utilizes the texture image located at: `\assets\minecraft\textures\item\wooden_sword.png`

Note that removing `parent` keys if you are not specifying all display properties of an item will return unexpected results.
The `wooden_sword`, for example, utilizes the parent file `\assets\minecraft\textures\item\generated.json`;
which also utilizes a parent file at `\assets\minecraft\textures\builtin\generated.json`.
If these files do not exist altered in the pack, they utilize the respective existing file within Minecraft's default resource.
To add the `custom_model_data` predicate, we specify this in the `Overrides` key.
Here is an example of the override, and the `custom_model_data` specified.

```json
{
    "parent": "item/handheld",
    "textures": {
        "layer0": "item/wooden_sword"
    },
    "overrides": [
        { "predicate": { "custom_model_data": 1}, "model": "item/custom/bandos_godsword" }
    ]
}
```

*Note: Remember that objects and arrays are separated by commas.*
The above example extends the item `wooden_sword` to have an additional item model when the item in-game has the mechanism applied.
This file is located at: `\assets\minecraft\models\item\custom\bandos_godsword.json`.
Valid `custom_model_data` entries are integers, up to larger integers available as opposed to the durability predicate.
An example of this file with multiple custom model data's specified looks like this:

```json
{
    "parent": "item/handheld",
    "textures": {
        "layer0": "item/wooden_sword"
    },
    "overrides": [
        { "predicate": { "custom_model_data": 1}, "model": "item/custom/bandos_godsword" },
        { "predicate": { "custom_model_data": 2}, "model": "item/custom/zamorakian_godsword" },
        { "predicate": { "custom_model_data": 3}, "model": "item/custom/saradomin_godsword" },
        { "predicate": { "custom_model_data": 4}, "model": "item/custom/armadyl_godsword" }
    ]
}
```

#### Example File: `custom_item.json`

Your custom item's model data file is something you may or may not adjust yourself.
THere are plenty of options for modeling software available, two of which most commonly recommended are [Cubik Pro](https://cubik.studio/) and [BlockBench](https://blockbench.net/).
Note that the software you use must be able to export the model to a `.json` file format.
Cubik Pro specifically saves the model, and the respective image file, into it's correct locations and formats the model file correctly.
When you place your custom item's model data into the location you direct it to in the above example, the top of your model file should look something like this:
```json
{
	"textures": {
		"particle": "item/custom/handheld/bandos_godsword",
		"texture": "item/custom/handheld/bandos_godsword"
	},
```

where the `particle` and `texture` keys both point to the image files we will be saving at the directory: `\assets\minecraft\models\item\custom\bandos_godsword.png`

### Inside The Textures folder Directory

Directory: `.minecraft\resourcepacks\MyResourcePack\assets\minecraft\textures\`
This is where your image files are saved.
These files should be in the relative filepath specified within the model file that it corresponds to.

### Inside The Sounds folder Directory

Directory: `.minecraft\resourcepacks\MyResourcePack\assets\minecraft\sounds\`
The sound format Minecraft uses is `.ogg`.
Free converting tools can be found online, one recommended option being [Audio-Online-Convert.com.](https://audio.online-convert.com/convert-to-ogg).
For organization's sake, if you're adding new sounds, it is recommended that you place them in a folder named `Custom`. Minecraft's default resource organizes it's sounds by [category](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/SoundCategory.html).
You can find Minecraft's default resource sound index here: `\.minecraft\assets\indexes\1.15.json`; where `1.15` is the versions we're using in this guide.
All of your sound files <span class="parens">('.ogg' files)</span> should be saved in this directory.

### Putting It Together: Using Denizen With Your New Pack

#### Custom Items

Giving yourself the item is simple. If it's a one-off time you need the thing or you're just generally testing, you can use the [`/ex` command](/guides/first-steps/ex-command) like this:
`/ex give wooden_sword[custom_model_data=1]`

The item script simply looks something like this:
```dscript_green
BandosSword:
    type: item
    material: wooden_sword
    mechanisms:
        custom_model_data: 1
```

The `custom_model_data` is in-line with any other mechanisms you choose to specify with the custom item.
You can give yourself the custom item just like any other item script, `/ex give BandosSword` or in any script with the `give` or `inventory` command.

#### Custom Sounds

Playing your sound is relative to the unique custom name you gave it.
In our example, we specified the name of the sound as `entity.player.defence.level`.
You can play this sound with the `playsound` command like this: `/ex playsound <player> entity.player.defence.level custom`
In a script, this would look something like this:
```dscript_green
MyCustomSound:
    type: task
    script:
        - playsound <player> sound:entity.player.defence.level custom
```

### Tips, Tricks And Notes While You Create

A very handy trial-and-error debugging tricks for creating resource packs is that you can actively edit the pack and view your changes in-game.
One of the most common misconceptions of resource packs is that you need to have it saved as a `.ZIP`.
FALSE! You can save this directly in your resource packs folder, edit and just reload!
The default hotkey to reload your resource packs is `F3 + T`

If you run across a flat purple and black square texture, this is the default Minecraft missing data replacement. 
- if your item is flat with the purple/black texture, your item's model file path is misconfigured or is missing.
- If your item has shape but no texture, your model file's image path is misconfigured or you're missing the image file.
- if your item is normal, your resource pack is not registering any changes made to the item.

THere is an incredibly handy JSON formatter and Validator you can find [Here](https://jsonformatter.curiousconcept.com/) for checking your JSON data.
Minecraft will give no indicators excluding broken texture images and models if your files are wrongly formatted.

Custom textures, models and sounds can be placed within as many sub-folders as you would like. Remember to abide the lowercase sensitivity.

Your default Resource Packs folder is located in your default minecraft directory, and looks something like this:
`C:\Users\username\AppData\Roaming\.minecraft\resourcepacks` on Windows, or `/home/[username]/.minecraft` on Linux.
Optimally, you can directly open the folder directory with the `Open Resource Pack Folder` button in the `Resource Packs...` section of your in-game menu.

The best template for modifying existing models and textures for Minecraft is the default resource,
which can be found in your Version Jar directly located in the directory: `\.minecraft\versions\`.
You can extract this to it's respective file and locate the `Assets` folder within.
Note that if you copy the entire `assets` folder as a template, you may consider removing material you don't change,
as it's extra file storage you don't need to contribute to the resource pack.

### Related Technical Docs And Links

* [Playsound Command Meta](https://one.denizenscript.com/denizen/cmds/playsound)
* [JSON Formatter and Validator](https://jsonformatter.curiousconcept.com/)
* [Online-Convert.com | Convert Audio to OGG Format](https://audio.online-convert.com/convert-to-ogg)
