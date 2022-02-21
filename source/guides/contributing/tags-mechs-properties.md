Tags, Mechs, and Properties
---------------------------

```eval_rst
.. contents:: Table of Contents
    :local:
```

You should already be familiar with tags and mechanisms and how to use them. This page will walk you through creating your own custom tags.

### Registering Tags

Tags that don't belong to properties are registered in the class definition of the object type, specifically in the `registerTags` static method. Take a look at the `PlayerTag` class located in the `objects` package.

Every tag type has a **tag processor**, which is defined as a static member of the type's class as `tagProcessor`. To register a tag, you'll need to call `registerTag` on this object. This method takes three parameters: the return type's class, the name of the tag, and a lambda expression that takes two parameters of its own.

```java
tagProcessor.registerTag(ElementTag.class, "tag_name", (attribute, object) -> {
    return new ElementTag("Hello, world!");
});
```

Let's explain that lambda in more detail. The `attribute` parameter represents the tag itself. For example, you can access the parameter with `attribute.getParam()`. When things go wrong, you'll call `attribute.echoError("...")` and return null.

The `object` parameter is just the instance of the current class. This means that in the `PlayerTag` class, `object` would be a `PlayerTag`.

Using this information, let's make a tag called `uuid_uppercase` which returns the player's UUID and capitalizes every letter. This doesn't have a genuine use; it's just for demonstration and practice purposes. If it did have a use, then the author of this guide page would have already contributed it.

We want to a return a single string, so our return type will be ElementTag. Additionally, we can use the `getUUID()` method on `object` to get the player's UUID. `UUID` is a Java utility class that has a `toString()` method, so we can use that alongside `toUpperCase()` to get what we want.

The `ElementTag` class has many constructors, including one that can take a single `String`, so we'll use that.

```java
tagProcessor.registerTag(ElementTag.class, "uuid_uppercase", (attribute, object) -> {
    return new ElementTag(object.getUUID().toString().toUpperCase());
});
```

Put this into the `registerTags` method, build Denizen, and put the jar into your `plugins` folder. Now, if you start the server and run `/ex narrate <player.uuid_uppercase>` in-game, it'll display your UUID in uppercase.

![](images/uuid_uppercase.png)

### Taking Tag Input

Let's mess with the player's UUID a bit more. We'll be editing our `uuid_uppercase` tag to take a boolean input that represents whether the UUID should be repeated once with a space in between.

We can use the `attribute` parameter, which is an instance of the `Attribute` class, to check if the tag has input with `hasParam()`. If so, we can get the input as an element with `getParamElement()`. The `ElementTag` class has a variety of methods for returning different primitive values depending on its internal value; we can get the boolean input by calling `asBoolean()`.

The above logic can be turned into one if statement like so:

```java
if (attribute.hasParam() && attribute.getParamElement().asBoolean()) {
    // ...
}
```

We can then move our UUID string to a variable and modify it if the condition passes <span class="parens">(concatenation is fine)</span>. After that, we just return it as an element like before.

```java
tagProcessor.registerTag(ElementTag.class, "uuid_uppercase", (attribute, object) -> {
    String uuid = object.getUUID().toString().toUpperCase();
    if (attribute.hasParam() && attribute.getParamElement().asBoolean()) {
        uuid = uuid + " " + uuid;
    }
    return new ElementTag(uuid);
});
```

With this setup, the tag input is optional; you don't even need to use `[]`. If you test it and input `true`, however, it should return two uppercase UUIDs separated by a space.

### Documenting Tags: Meta Entries

We have a complete and functional tag, but there's one more thing we're missing: documentation! If you've ever wondered how the [meta documentation site](https://meta.denizenscript.com/) works, it actually looks through all the Denizen code and finds custom comments to parse. We call these comments **meta entries**, and for tags, they look like this:

```java
// <--[tag]
// @attribute <ObjectTag.tag_name>
// @returns ObjectTag
// @mechanism ObjectTag.mech_name
// @description
// This is the description of the tag.
// -->
```

Note that "attribute" is just a legacy term for tag. Keep in mind that this needs to display exactly how the tag should be used, so if the tag takes input, you'll need to account for it. The `@mechanism` key is optional; if present, it means that the supplied mechanism is the direct counterpart to the tag.

The `@returns` key is the tag type of the returned value. In our case, it's just `ElementTag`, since we're returning a piece of text. However, you'll need to be more specific at times; ElementTags can contain booleans, integers, and decimals. For those cases, we denote the specific type in parentheses: `ElementTag(Boolean)`, `ElementTag(Number)`, and `ElementTag(Decimal)` respectively. This specification also applies to ListTags: for example, if you had a list of locations, you'd denote the type as `ListTag(LocationTag)`.

Meta entries are stuck directly above the tag code. Here's what it would look like on our tag:

```java
// <--[tag]
// @attribute <Player.uuid_uppercase[(<repeat>)]>
// @returns ElementTag
// @description
// Returns the UUID of the player in uppercase.
// Optionally specify whether the UUID should be repeated once.
// -->
tagProcessor.registerTag(ElementTag.class, "uuid_uppercase", (attribute, object) -> {
    String uuid = object.getUUID().toString().toUpperCase();
    if (attribute.hasParam() && attribute.getParamElement().asBoolean()) {
        uuid = uuid + " " + uuid;
    }
    return new ElementTag(uuid);
});
```

### Creating Mechanisms

**NOTE**: This section could be subject to change in the near future. The tag registry system has proved to be very capable, and the mechanism matching system could be replaced with a registry of its own.

Unlike tags, mechanisms undergo a series of checks to "match" the mechanism. This is done in the class definition's `adjust` method, which takes a `mechanism` parameter. Mechanisms have a variety of methods to match and check input, which we'll see shortly.

To match a mechanism, use the `matches(String)` method and provide the mechanism name. To require a specific input type, you can make use of the methods starting with `require`, such as `requireBoolean()` and `requireObject(Object)`. Wrap these methods in an if statement to start a mechanism block.

```java
if (mechanism.matches("some_mechanism") && mechanism.requireBoolean()) {
    // do stuff
}
```

Let's make a mechanism for an ItemTag called `wrap_brackets` that takes an integer as input. It'll wrap its display name in brackets with the specified amount of spaces in between. We can make use of the `requireInteger()` method for the input.

The `ItemTag` class has an `Item` instance variable named `item`. Since `adjust` isn't a static method, we can use instance variables directly inside of mechanism code. The display name, lore, enchantments, etc. all fall under "item meta," which we can check exists with `hasItemMeta()` and get with `getItemMeta()`. In the case there isn't any existing item meta, we'll throw an error. 

If you remember the "Don't Trust Users" speech, it *especially* applies here. You should account for every reasonable possibility when implementing features in Denizen. As you might expect, errors are quite common. 

There is an `echoError("...")` method for both `attribute` in tags and `mechanism` in mechanisms. That doesn't stop the code, however, so you'll need to return in both cases. Since you need to return something in a tag, you'll return `null`, as that's the default errored value.

```java
if (mechanism.matches("wrap_brackets") && mechanism.requireInteger()) {
    if (!item.hasItemMeta()) {
        mechanism.echoError("This item doesn't have meta!");
        return;
    }
}
```

Now that we're free of errors, we can use the `getValue()` method, which returns the input as an ElementTag. Building off of the [Taking Tag Input](#taking-tag-input) section, we can use `asInt()` for the amount of brackets. After that, we can use some basic `StringBuilder` logic to repeat spaces.

```java
if (mechanism.matches("wrap_brackets") && mechanism.requireInteger()) {
    // ...
    int amount = mechanism.getValue().asInt();
    StringBuilder spaces = new StringBuilder(amount);
    for (int i = 0; i < amount; i++) {
        spaces.append(" ");
    }
}
```

It's time we talk about **NMS**, or net.minecraft.server. Denizen supports multiple Minecraft versions, and in order to keep code compatible, different methods are implemented via NMS helpers in their respective version module. The class we want to access is `ItemHelper`, which can be accessed via `NMSHandler.getItemHelper()`. We can then use `setDisplayName(ItemTag, String)` to achieve what we want.

Going back to the item meta - it's a simple call to `getDisplayName()` to get the display string. After that, we can just use string concatenation. Here's our final implementation:

```java
if (mechanism.matches("wrap_brackets") && mechanism.requireInteger()) {
    if (!item.hasItemMeta()) {
        mechanism.echoError("This item doesn't have meta!");
        return;
    }
    int amount = mechanism.getValue().asInt();
    StringBuilder spaces = new StringBuilder(amount);
    for (int i = 0; i < amount; i++) {
        spaces.append(" ");
    }
    String newName = "[" + spaces + item.getItemMeta().getDisplayName() + spaces + "]";
    NMSHandler.getItemHelper().setDisplayName(this, newName);
}
```

Remember that you'll need to use the [`inventory`](https://meta.denizenscript.com/Docs/Commands/inventory) command to adjust an item in your inventory. The item will also need to have its `display` property set beforehand <span class="parens">(that's what the error check is for)</span>.

Mechanisms also have meta entries! Try and fill out one on your own based on this template:

```java
// <--[mechanism]
// @object ObjectTag
// @name mech_name
// @input ObjectTag
// @description
// This is the description of the mechanism
// @tags
// <ObjectTag.tag_name>
// -->
```

### Properties?

A **Property** is a combined set of tags and mechs that contribute to one aspect of an object. For example, [`MaterialTag.mode`](https://meta.denizenscript.com/Docs/Tags/materialtag.mode) is a property: you can retrieve it in tag form and also adjust it with a valid input.

Every property is its own class that implements the `Property` interface. Tags are registered in the static `registerTags` method, and mechanisms are applied in the `adjust` method. You might recognize that this is exactly how it works in the tag type classes!

Here are the methods a property needs to implement:

- `getPropertyString` - the value returned by the tag, but as a java String. For simple properties such as boolean values, this can return `"true"` or `"false"`. However, with more complex tag outputs, you can use every tag type's `identify()` method.
- `getPropertyId` - the property's name. For example, `type` in `MaterialTag.type`.

And here are the methods commonly used within property definitions:

- `describes` - takes an ObjectTag and determines if it can be used for the property. This isn't just to check the tag type, it's also to validate the object. For example, bamboo only applies to `leaf_size`, so `MaterialLeafSize` checks if the material provided is bamboo.
- `getFrom` - a placeholder method that gets copy-pasted or generated from a template. It calls describes and then returns the property instance if it's successful, null if not.

Currently, when creating mechanisms, you need to add the mechanism name to the `handledMechs` array. There used to be the equivalent for tags, but that was deprecated in favor of the registry system. If your mechanism isn't recognized, chances are you probably forgot to put it in the array.

For a property to be recognized, it itself needs to be registered. The `properties` package holds all the packages for the different types of properties as well as the `PropertyRegistry` class. To register a property, use `PropertyParser.registerProperty()` and pass in the property class and the tag type it applies to. Make sure to place this call in alphabetical order with the other properties of the same type.

Take a look at the existing property classes for examples!