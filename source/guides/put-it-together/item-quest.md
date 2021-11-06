An Item Quest (PARTIAL)
-------------

**TODO: Notice about required section reading before starting this.**

**TODO: Write-up guiding players from start to finish through writing an NPC-driven get-me-an-item quest.**

### Sample Script

This guide has not yet been written, however, here is a script with in-file explanation comments that demonstrates one possible implementation of an NPC-driven item quest.

This sample assumes you have a **modern Denizen configuration file**. That is, your `plugins/Denizen/config.yml` was generated after November 2021 (Release 1750 or later). If your config is older but you wish to use this script, you can either
- A: Delete your `config.yml` file and restart your server so Denizen can regenerate it.
- or B: go into your `config.yml` in your text editor, find the line `Queue speed: 0.5s` under `Interact:`, and change the `0.5s` to `instant`, then `/denizen reload config`

This script is designed such that you could copy/paste and load it in to your server, and assign it to NPCs with the commands listed at its top, and it will all work. You can then customize it and/or use it as a reference to learn from.

This may be easier to read within [the script editor](/guides/first-steps/script-editor) than on this webpage.

```dscript_green
# | To use this script:
# /npc create Questy McQuestface
# /npc assignment --set item_questgiver_assign
# Then go to the destination area
# /npc create Thiefy McThiefface
# /npc assignment --set item_quest_goal_assign
# For beginner usage, you can simply copy/paste and fill in the details (item name, chat messages, etc)
# If using multiple times, be sure to rename each script container appropriately
# If you're testing the script and want to manually reset your cooldown, you can use:
# /ex zap item_questgiver_interact *
# Don't forget to add 'debug: false' on each container when you're done testing.



# First, we define a custom item for the quest to use
my_item_quest_item:
    type: item
    # Probably make it something the player wouldn't steal
    material: golden_hoe
    # Make it look important
    display name: <&b><bold>Priceless Heirloom
    lore:
    - <&7>Questy McQuestface's priceless family heirloom.
    - <&6>[Must Return To Quest Town]
    # We can give a useless enchantment and hide it to add a glow effect to the item
    enchantments:
    - lure:1
    mechanisms:
        hides: all

# Now, we make an assignment and interact script for the quest giver - the one that needs an item brought back
item_questgiver_assign:
    type: assignment
    actions:
        on assignment:
        - trigger name:click state:true
        - trigger name:chat state:true
        - trigger name:proximity state:true radius:10
    interact scripts:
    - item_questgiver_interact

item_questgiver_interact:
    type: interact
    steps:
        # The default step will be offering the quest to any passers by
        default*:
            # First: when players walk close, say hi
            proximity trigger:
                entry:
                    script:
                    - chat "Hey! Over here! I need help!"
            click trigger:
                script:
                - chat "Hi <player.name>! Can you help me? I lost my valuable item!"
                # Use on_click to make chat triggers easier, and on_hover to make it clear that the text is clickable
                - narrate "<&7>[<element[<&b>Yes I accept].on_click[yes].on_hover[Click to start quest]> or <element[<&b>No not right now].on_click[no].on_hover[Click to refuse quest]>]"
                # Jump to the possible acceptance step, with a duration limit to be safe (if the player does nothing for 5 minutes, reset to default step again)
                - zap wait_for_accept 5m
        # After clicking the NPC, this step is used to allow the player to accept or refuse the quest
        wait_for_accept:
            # If the player doesn't speak and just clicks the NPC again...
            click trigger:
                script:
                - chat "... Well? Yes or no?!"
                # Copy/paste the narrate.
                # In some cases it might be better to move this into a task script or a data key for reuse, but copy/pasta is quick and easy for just one duplicate.
                - narrate "<&7>[<element[<&b>Yes I accept].on_click[yes].on_hover[Click to start quest]> or <element[<&b>No not right now].on_click[no].on_hover[Click to refuse quest]>]"
            chat trigger:
                1:
                    # If the player says yes...
                    trigger: /Yes/ I accept
                    script:
                    # Tell the player the quest
                    - chat "Great! Thiefy McThiefface has my item over in Destination Townshiplandplaceville."
                    - chat "It's a priceless family heirloom and I need it returned! I'll reward you well!"
                    - narrate "<&7>[Quest <&b><bold>Priceless Example Quest Of Generations<&7> accepted. Travel to Destination Townshiplandplaceville and speak to Thiefy McThiefface.]"
                    # Jump the goal NPC's script to correct step for when the quest is active
                    - zap item_quest_goal_interact can_give_item
                    # Jump this NPC to the waiting step
                    - zap wait_for_return
                2:
                    # But also the player can refuse...
                    trigger: /No/ not right now
                    script:
                    - chat "Okay. Maybe somebody more cool and heroic than you will do my quest for me."
                    - narrate "<&7>[Quest refused]"
                    - zap *
            # If the player walks away after clicking the NPC, reset to default step
            proximity trigger:
                exit:
                    script:
                    - chat "Wow! Rude! Not even a simple 'no'? :("
                    - narrate "<&7>[Quest refused]"
                    - zap *
        # This step handles when the player has the quest, but has not yet returned the item
        wait_for_return:
            click trigger:
                # If the player has the item,
                1:
                    trigger: my_item_quest_item
                    script:
                    # Thank the player and take the item
                    - chat "Wow! My heirloom!"
                    - take item:my_item_quest_item
                    - narrate "<&7>[<&b><bold>Priceless Family Heirloom<&7> removed]"
                    - chat "Thank you adventurer! Here's your reward!"
                    # Maybe show some pretty effects to make the player feel special
                    - toast "Quest Complete: <&b><bold>Priceless Example Quest Of Generations" icon:my_item_quest_item
                    # Give a reward - xp in this case, maybe instead give money or something like that
                    - give xp quantity:1000
                    - narrate "<&7>[Got <&b>1000 XP<&7>]"
                    # Jump to the idle 'on_cooldown' step for a cooldown duration. When the duration is up, the player will automatically reset to the default step.
                    - narrate "<&7>[Quest <&b><bold>Priceless Example Quest Of Generations<&7> complete. May be repeated in 3 days.]"
                    - zap on_cooldown 3d
                    # TODO: You should consider what happens if the player simply loses the item. Do you prevent this via world script events (player drops item / clicks in inventory), or add a backup time limit, or...?
                2:
                    # If the player lacks the item,
                    script:
                    - chat "Well? Where is it!?"
                    # Remind the player of their quest
                    - narrate "<&7>[Travel to Destination Townshiplandplaceville and speak to Thiefy McThiefface.]"
        # This step is idly waited on for the cooldown duration of the quest
        on_cooldown:
            click trigger:
                script:
                # Tell the player they're still on cooldown so they don't get confused
                - narrate "Thanks for returning my item :D"
                - narrate "<&7>[You may repeat this quest after <&b><script.step_expiration.from_now.formatted><&7>]"

# Now an assignment and interact for the destination - the NPC that has the item to be retrieved
item_quest_goal_assign:
    type: assignment
    actions:
        on assignment:
        - trigger name:click state:true
        - trigger name:chat state:true
    interact scripts:
    - item_quest_goal_interact

item_quest_goal_interact:
    type: interact
    steps:
        # The default step: if you're not on the quest, begone!
        default*:
            click trigger:
                script:
                - chat "Who are you? What do you want?"
        # This step is for players that are on the quest already, to initially speak with the NPC
        can_give_item:
            click trigger:
                script:
                # Give the player some interaction options
                - chat "Questy McQuestface sent you, didn't he?"
                - narrate "<&7>[<element[<&b>Yes, give me his item back now!].on_click[yes].on_hover[Click here to advance quest]> or <element[<&b>No I don't know what you're talking about].on_click[no].on_hover[Don't click this]><&7>]"
                # Note for caution: if you put a cooldown on this, it would revert to the default step, which is bad, so don't do that.
                - zap give_item
        # This step is to talk to the NPC and get the item
        give_item:
            click trigger:
                script:
                # This part, same idea as the wait_for_accept click trigger in the previous interact script above
                - narrate "<&7>[<element[<&b>Yes, give me his item back now!].on_click[yes].on_hover[Click here to advance quest]> or <element[<&b>No I don't know what you're talking about].on_click[no].on_hover[Don't click this]><&7>]"
            chat trigger:
                1:
                    trigger: /Yes/ I can take it back
                    script:
                    - chat "Oh dang okay fine take it i didn't even want it anyway"
                    - give my_item_quest_item
                    - narrate "<&7>[Return the <&b><bold>Priceless Family Heirloom<&7> to Questy McQuestface]"
                    # Jump to a waiting step in case the player tries to interact with this NPC more
                    # This can have a cooldown - after it's up, they go back to the default step, which is idly waiting
                    - zap please_return_it 1h
                2:
                    # It can sometimes be nice to have a 'no' button even if it doesn't do anything useful
                    trigger: /No/ I don't know what you're talking about
                    script:
                    - chat "... oh okay go away then"
                    - zap can_give_item
        # This step is for players that already took the item but are trying to interact with the NPC more
        please_return_it:
            click trigger:
                script:
                - chat "Well?! You got your heirloom! Go away!"
```
