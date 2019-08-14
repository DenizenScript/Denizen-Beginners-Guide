What Can Denizen Do With Citizens?
----------------------------------

```eval_rst
.. contents:: Table of Contents
    :local:
```

### Two-Way Connection

The integration Denizen has with Citizens actually works in two ways:

- First, as you can guess, Denizen has a lot of scripting commands/tags/etc, specific to Citizens.

- But in addition to that, Denizen also adds a variety of additional tools directly into Citizens. For example: `/npc mirror` is a command made available by Denizen (which makes the NPC automatically mirror the viewing player's skin). Several "basic usage" commands are provided by Denizen, such as `/npc sit`, `/npc sneak`, and `/npc invisible`. Denizen also provides several basic handy traits, like the `health` trait or the `fishing` trait.

- The two ways can also work together sometimes, such as [this handy script](https://forum.denizenscript.com/viewtopic.php?f=13&t=133) that allows users to do `/npc skin --url [url here]` to set an NPC's skin from an image URL, or on a more simple level [this quick helper script](https://forum.denizenscript.com/viewtopic.php?f=13&t=149) that allows users to add commands that an NPC will execute when it's right-clicked.

### Questing

Of course, the most popular usage of the Denizen-Citizens connection is having NPCs that give and take part in RPG-style questing. Denizen has a fairly powerful set of systems dedicated to this specific task <span class="parens">(but still generic enough that it can be used for other cases)</span>.

### Conversations

The tools made available most ideally for RPG-style questing are also a great fit for anything that fits the model of players having a conversation with an NPC. This includes, for example, a conversation being the access point for an NPC's shop <span class="parens">(which would then be handled by an inventory GUI Denizen script or similar)</span>.

### Cutscenes

One neat thing that's achieved less often but always at least a thought-about-doing for many servers, is NPC-driven cutscenes. With a few careful usages of the `walk` command, perhaps the `rotate` command, and optionally the spectator functionality, it's pretty simple to write a Denizen script that uses NPCs to act out a scene in front of players.

### Uniqueness

With Citizens on your server, you have statues. If you install Sentinel, you can have some guards. With Denizen included, you can have a unique server that feels truly alive. The only limit is how much dialogue/cutscene pathing/etc. you're willing to write!
