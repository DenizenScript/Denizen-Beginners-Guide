A Kill Quest (PLACEHOLDER ONLY)
------------

**TODO: Notice about required section reading before starting this.**

**TODO: Write-up guiding players from start to finish through writing an NPC-driven kill quest.**

### For Those Coming From The Video

As a placeholder for those coming from the [old tutorial video here](https://one.denizenscript.com/denizen/vids/Putting%20It%20Together:%20A%20Kill%20Quest), the following is an updated version of the script shown in the video.

```dscript_green
npc_killquest:
    type: assignment
    actions:
        on assignment:
        - trigger name:click state:true
        - trigger name:chat state:true
    interact scripts:
    - npc_killquest_interact

cchat:
    type: format
    format: "<&b><npc.name> <&f>to you<&co> <&2><text>"

npc_killquest_interact:
    type: interact
    steps:
        1:
            click trigger:
                script:
                - if <player.has_flag[npc_engaged]>:
                    - stop
                - if <player.has_flag[kill_zombie_quest_cooldown]>:
                    - narrate "You can repeat this quest in <player.flag[kill_zombie_quest_cooldown].expiration.formatted>."
                    - stop
                - if <player.has_flag[kill_zombie_quest]>:
                    - stop
                - flag player npc_engaged
                # - engage
                - if <player.flag[kill_zombie_quest_count]> == 5:
                    - narrate format:cchat "Great work! Here's your reward!"
                    - give diamond
                    - flag player kill_zombie_quest_count:!
                    - flag player kill_zombie_quest_cooldown duration:24h
                    - flag player npc_engaged:!
                    # - disengage
                    - stop
                - narrate format:cchat "Hello there. Would you care for a special prize?"
                - wait 5t
                - narrate format:cchat "If so, you can kill 5 zombies for me."
                - wait 5t
                - narrate format:cchat "Will you accept this request?"
                - wait 5t
                - narrate "[<&o>Type <&b><&o>Yes<&f><&o> or <&b><&o>No<&f>]"
                - flag player npc_engaged:!
                # - disengage
            chat trigger:
                1:
                    trigger: "/Yes/ I accept the quest"
                    script:
                    - if <player.has_flag[kill_zombie_quest_cooldown]>:
                        - stop
                    - if <player.has_flag[kill_zombie_quest]>:
                        - stop
                    - flag player npc_engaged
                    # - engage
                    - narrate format:cchat "Okay great!"
                    - wait 5t
                    - narrate "[Kill 5 zombies!]"
                    - flag player kill_zombie_quest
                    - flag player kill_zombie_quest_count:0
                    - flag player npc_engaged:!
                    # - disengage
                2:
                    trigger: "/No/ I don't"
                    script:
                    - if <player.has_flag[kill_zombie_quest]>:
                        - stop
                    - random:
                        - narrate format:cchat "Okay screw off!"
                        - narrate format:cchat "Okay then."
                        - narrate format:cchat "Screw you then!"

killquest_zombie_world:
    type: world
    events:
        on player kills zombie flagged:kill_zombie_quest:
        - flag player kill_zombie_quest_count:++
        - if <player.flag[kill_zombie_quest_count]> == 5:
            - narrate "[Return to the NPC]"
            - flag player kill_zombie_quest:!
```
