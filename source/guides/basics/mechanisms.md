Mechanisms And Properties
-------------------------

```eval_rst
.. contents:: Table of Contents
    :local:
```

### What's a Mechanism?

If you've made it this far, you've learned about [definitions](/guides/basics/definitions) and [flags](/guides/basics/flags), the two most common ways to read and write stored data for use in your scripts. **Mechanisms** are a way to set a value on an object. They're kind of like mini-commands that work within the properties system. Here are a few examples of their use in script containers:

```dscript_green
monkey_wrench:
    type: item
    display name: Monkey Wrench
    material: iron_hoe
    lore:
    - A monkey wrench.
    - Not actually usable on monkeys.
    mechanisms:
        unbreakable: true
```

This item script, using the `mechanisms` key and the `unbreakable` mechanism with a value of `true`, makes the item unbreakable.

```dscript_green
undead_golden_swordsman:
    type: entity
    entity_type: zombie
    item_in_hand: golden_sword
    item_in_offhand: golden_sword
    health_data: 80/80
```

This entity script creates a zombie and uses the `item_in_hand` and `item_in_offhand` mechanisms to put golden swords in both hands. It also spawns with 80 health, and has 80 health at maximum, using the `health_data` mechanism.

### The Adjust Command

Mechanisms can be used in more than just script containers! If you need to alter the value of a mechanism, the `adjust` command is the way to go.

For example, if we want to write a script that changes the color of a sheep when right-clicked:

```dscript_green
random_sheep_colors:
    type: world
    events:
        on player right clicks sheep:
        - define random_color <list[black|blue|brown|cyan|gray|green|light_blue|light_gray|lime|magenta|orange|pink|purple|red|white|yellow].random>
        - adjust <context.entity> color:<[random_color]>
```

This script will pick a random color from the list and change the color of the sheep to the randomized color.

#### The AdjustBlock command

The `adjustblock` command is a variant of the normal `adjust` command. It's built specifically to adjust `material` mechanisms on blocks <span class="parens">([a list of which can be found here](https://one.denizenscript.com/denizen/mecs/materialtag))</span>.

While the applicability of `adjustblock` is more niche, it can still be quite useful. For a quick usage example, you can use this script to force the plant block you are looking at to immediately change to its maximum age <span class="parens">(i.e. to cause newly-planted wheat to fully grow)</span>:

```dscript_green
grow_plant:
    type: task
    script:
    - if <player.cursor_on.material.is_ageable>:
        - adjustblock <player.cursor_on> age:<player.cursor_on.material.maximum_age>
```

As before, you can use this script by typing `/ex run grow_plant` in-game.

#### How To Adjust Items

You can also adjust the properties of items in inventories. Doing so uses the `inventory` command with the `adjust` argument.

You might think that the correct way to modify an item held by a player is by adjusting the item itself:

```dscript_red
magical_flint_bad:
    type: world
    events:
        on player right clicks block with:flint:
        - adjust <player.item_in_hand> "display:dFlint"
        - adjust <player.item_in_Hand> "lore:Built with Denizen!"
```

However, this will only adjust the *generic concept* of the item in the player's hand. The tag `<player.item_in_hand>` will just return flint - any flint, not the specific instance of the flint being used by the player that exists in their inventory. If you're not adjusting a specific item that exists in the world somehow, nothing is going to change in the world! Instead, you need to use the `adjust` argument of the `inventory` command to adjust the specific item that you want to change.

The below example will *correctly* transform a player's flint into a diamond when they right click with it:

```dscript_green
magical_flint:
    type: world
    events:
        on player right clicks block with:flint:
        - inventory adjust slot:<player.held_item_slot> "display:dFlint"
        - inventory adjust slot:<player.held_item_slot> "lore:Built with Denizen!"
```

The `inventory adjust` command will specifically change the item at issue, because that's what it is designed to do! Because you identify the unique object of the item as it exists in the player's inventory, the `inventory adjust` command is therefore able to modify it as desired.

#### Adjusting Definitions

The `adjust` command can also be used to modify an object stored in a definition. For example:

```dscript_green
random_sheep_colors_definition:
    type: world
    events:
        on player right clicks sheep:
        - define sheep <context.entity>
        - define random_color <list[black|blue|brown|cyan|gray|green|light_blue|light_gray|lime|magenta|orange|pink|purple|red|white|yellow].random>
        - adjust def:<[sheep]> color:<[random_color]>
```

This script is similar to the rainbow sheep script above, but modifies the sheep saved in the `sheep` definition as an example of how to adjust definitions. Like with regular definition usage, adjusting definitions is most useful in more complicated scripts, or scripts where the object you're adjusting is retrived from a complicated and lengthy tag.

### Properties

"Properties" are a system to track the details of an object that doesn't have a unique identity of its own.

#### Item Properties

The most common place that properties are seen in use is with items. In Denizen, an item is a material and a series of mechanisms that compose its properties. For example, if you hit an entity with a freshly-crafted diamond sword in survival mode and then run `/ex narrate <player.item_in_hand>` to view the Denizen construction of that item, you'll see it return `i@diamond_sword[durability=1]`. In this case, `durability` is the only property of the item, and its value is `1`, the amount of durability the item has lost thus far. Multiple properties are separated by semicolons. For example, `i@diamond_sword[durability=1;display_name=Skullbuster]`. <span class="parens">(Remember, [never use raw object notation](/guides/troubleshooting/common-mistakes#don-t-type-raw-object-notation) - these examples are for demonstrative purposes only!)</span>

Items are, fundamentally, their material and their properties. Any item a player has in their inventory can be parsed in this manner, and an item's properties can be read and modified as desired.

#### Material Properties

Materials, like items, lack unique identities. A stone block is just a material at a location. A wheat block is only slightly more complicated - it's a material at a location with an `age` property. As you saw above in the `adjustblock` example, using the `age` mechanism allows you to modify that property for a block in the world. When you read block materials from locations, they will return any associated properties. This could be used, for example, to check whether a campfire is sending up smoke signals, or various redstone properties, or even the faces of a mushroom block.

Materials with properties, when parsed by a tag like `<player.cursor_on.material>`, will return an output like `m@wheat[age=7]` for a fully-grown wheat block. In this case, the `age` of the wheat is `7`.

#### Entity Properties

Entities have properties too! Entity properties can be read and modified just like material properties, and you can see a list of all of an entity's properties with the `<EntityTag.describe>` tag. For example, here's a sample output of `/ex narrate <player.target.describe>` when targeting a sheep modified by our color script:

```
e@sheep[age=0;has_ai=true;attributes=li@el@GENERIC_MAX_HEALTH/8.0|el@GENERIC_FOLLOW_RANGE/16.0/Random spawn bonus/0.023546975882180802/ADD_SCALAR/any|el@GENERIC_KNOCKBACK_RESISTANCE/0.0|el@GENERIC_MOVEMENT_SPEED/0.23000000417232513|el@GENERIC_ATTACK_KNOCKBACK/0.0|el@GENERIC_ARMOR/0.0|el@GENERIC_ARMOR_TOUGHNESS/0.0|;is_aware=true;color=orange;equipment=li@i@air|i@air|i@air|i@air|;health_data=8.0/8.0;speed=0.23000000417232513]
```

As you can see above, all of the data about the sheep is captured by Denizen and output in the format of an EntityTag with various properites. Each property is separated by a semicolon, and the data stored in each property varies based on the nature of the property. 

These properties can be adjusted using the `adjust` command or read by using their corresponding tags. For example, `<EntityTag.color>` is the tag associated with the `color` EntityTag mechanism. `/ex narrate "The <player.target.entity_type.to_lowercase> you're looking at is colored <player.target.color>"` will narrate, for example, `The sheep you're looking at is colored orange` based on the data above.

### Related Technical Docs

If you want to read a lot more about mechanisms, here are a few technical guides you might consider...

Note: Most users, especially those learning from the Denizen for the first time, should just continue on to the next guide page. These references might be of interest to later come back to after you've learned Denizen as far as this guide teaches.

- [List of all mechanisms](https://one.denizenscript.com/denizen/mecs/)
