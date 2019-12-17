Common Mistakes
---------------

There are a few common mistakes and not-very-obvious expectations about how to handle things that we've seen while helping new Denizen users. To help you master Denizen more quickly, we've listed a few of these issues and what to do about them below.

```eval_rst
.. contents:: Table of Contents
    :local:
```

### Players Are Not Their Names

Historically in Minecraft, players were unique based on their name. This meant that "Steve" was theoretically always going to be "Steve". There was one true "Steve", nobody else could be "Steve" and "Steve" could never take on another name. This changed around the era of Minecraft 1.7, when UUIDs became the unique identifier of a player, and players were from there on allowed to change their names.

Never track a player's name internally. The `<player.name>` tag should exclusively be used for outputting a clean name in a `narrate` command or similar output meant to be read by players. As that's all a name is meant for: human reading. It is not meant for any internal tracking. It is not unique nor reliable.

### So, A Player Is Their UUID?

A player is **not** just their UUID. A player isn't a name, a UUID, a location, or anything else. A player is a player.

Similarly, an NPC is **not** just their ID. An NPC is an NPC.

In fact, nothing is *just* that little piece of information that uniquely identifies it.

#### The Object System

An important part of the way Denizen functions is the **object system**.

An "object" in the world of software is a representation of something specific that can be tracked by a **lookup** identifier, that exists as more than just that lookup data. That's a bit confusing, so what does that mean in real usage? That means an "entity object" is a real full entity, with its AI and its health and its name and its specific place in the world and everything else that makes it what it is. The entity can be quickly looked up if you use the UUID, but the true entity itself is so much more than just a short set of numbers and letters. <span class="parens">(Note for the curious: in most software programming languages, the unique identifier of an object is its memory address)</span>.

In Denizen, whenever you look at an object in debug or with a `narrate` command <span class="parens">(or wherever else in text)</span>, the unique identifier is visible, with a prefix identifying what type of object it is (that's called **Object Notation**). This is **not** meant to be the object itself, but rather a lookup identifier so you or the system can read it and figure out what object was being referred to.

It's important when writing scripts to make sure you work with *the actual object* and not with some text that contains the lookup identifier.

A few examples of where this might come into play:
- A player object is placed into a line of text. Say for example `"Player:<player>"` is stored somewhere. When you read that text out, you may assume that `<[THAT_TEXT].after[:]>` is going to return the player object - but it won't. It will return plain text of the unique player identifier. You would have to convert it into a player object again, either use `<player[<[THAT_TEXT].after[:]>]>` or `<[THAT_TEXT].after[:].as_player>`.
- In some cases, reading directly from data storage <span class="parens">(YAML, Flags, SQL, etc.)</span> might return the plain text identifier of whatever object was inserted into it. When this happens, you again have to convert it back into the real object using the relevant conversion tags.
- Generally when user input is given (in for example a command script). A unique identifier or even a non-unique one may be used, and you will have to do more complex real-object-finding. As a particular example of this, when a command script has a player input option, generally you can trust that users aren't going to type out the exact perfect object identifier. The tag `server.match_player` is useful for converting the human-input player name into a real player object.

### Don't Compare Raw Objects

**TODO**
