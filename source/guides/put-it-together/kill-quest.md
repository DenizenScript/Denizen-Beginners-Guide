A Kill Quest (PARTIAL)
------------

**TODO: Notice about required section reading before starting this.**

**TODO: Write-up guiding players from start to finish through writing an NPC-driven kill quest.**

### Historical Version

You can still find the [old tutorial video here](https://one.denizenscript.com/denizen/vids/Putting%20It%20Together:%20A%20Kill%20Quest), however be warned that some of its techniques are outdated, notably the flag tags. Read through the list of [Updates Since The Tutorial Videos](/guides/troubleshooting/updates-since-videos) if you choose to watch the video.

### Sample Script

This guide has not yet been written, however, here is a script with in-file explanation comments that demonstrates one possible implementation of an NPC-driven kill quest.

This sample assumes you have a **modern Denizen configuration file**. That is, your `plugins/Denizen/config.yml` was generated after June 2021 (Release 1743 or later). If your config is older but you wish to use this script, you can either
- A: Delete your `config.yml` file and restart your server so Denizen can regenerate it.
- or B: go into your `config.yml` in your text editor, find the line `Queue speed: 0.5s` under `Interact:`, and change the `0.5s` to `instant`, then `/denizen reload config`

This script is designed such that you could copy/paste and load it in to your server, and assign it to an NPC with `/npc assign --set npc_killquest` or `/ex assignment set npc_killquest`, and it will all work. You can then customize it and/or use it as a reference to learn from.

This may be easier to read within [the script editor](/guides/first-steps/script-editor) than on this webpage.

```dscript_green
# Core assignment script to be given to the NPC
npc_killquest:
    type: assignment
    actions:
        on assignment:
        # Enable both triggers that will be used
        - trigger name:click state:true
        - trigger name:chat state:true
    interact scripts:
    # And link the interact script below
    - npc_killquest_interact

# Alternate chat format for the NPC if you don't like default 'chat'
# if you make multiple NPCs with this script as a template, remember that you only need the format scripts *once* (unless you have it different per NPC)
cchat:
    type: format
    format: <&b><npc.name> <&f>to you<&co> <&2><[text]>

# A clean but simple format for instructions given to the player by the script rather than by the NPC
# (The Out-Of-Character clarification of what the NPC said In-Character).
instruction_format:
    type: format
    # Light Gray + Italic
    # Can also be written like <gray><italic>
    format: <&7><&o>[<[text]><&7><&o>]

npc_killquest_interact:
    type: interact
    steps:
        # Default step: waiting for player to interact
        waiting*:
            # The player's initial interaction with this NPC is always just right clicking it
            click trigger:
                script:
                # Example of doing engage per-player with a flag
                # Engaging is a way to prevent players from spamming interactions with an NPC and glitching the scripts out as a result.
                # It just forces the player to wait on their next interaction until the current one is finished.
                # It works by using a has_flag check at the start of each interaction to stop early, and adding/removing before/after slow interactions like the narrates with waits below.
                - if <player.has_flag[npc_engaged]>:
                    - stop
                # Check for a cooldown before dealing with engage so we don't have to disengage inside the if
                - if <player.has_flag[kill_zombie_quest_cooldown]>:
                    # While a cooldown *could* be a step or a `cooldown` command, having it as a flag allows you to track and display the cooldown timer clearly, which players will appreciate.
                    - narrate format:instruction_format "You can repeat this quest in <player.flag_expiration[kill_zombie_quest_cooldown].from_now.formatted>."
                    # If we put the script *after* an engage, the disengage would go here - just before any 'stop' command.
                    - stop
                # Add the engage flag for one minute - either it will be cleared via the flag command, or if something bugs, it will clear on its own after a minute
                - flag player npc_engaged expire:1m
                # Alternately, instead of the player flags, you can use engage commands to engage per-NPC,
                # which is simpler to do (it's all in the one short command) but gets in the way of other players often
                #- engage
                - narrate format:cchat "Hello there. Would you care for a special prize?"
                - wait 5t
                - narrate format:cchat "If so, you can kill 5 zombies for me."
                - wait 5t
                - narrate format:cchat "Will you accept this request?"
                - wait 5t
                # The player can type 'yes' or 'no' into chat normally, OR click the word to automatically say it
                - narrate format:instruction_format "Type <&b><&o><element[Yes].on_click[yes]><&7><&o> or <&b><&o><element[No].on_click[no]>"
                # Zap to the step that contains the chat trigger. Add a five minute limit so if the player runs away and comes back, the NPC isn't still expecting a response.
                - zap accept_question 5m
                - flag player npc_engaged:!
                #- disengage
        # Second step: only active while waiting for a response to the question given in the click trigger
        accept_question:
            chat trigger:
                1:
                    # Simple main chat trigger: if the player says yes, they start the quest
                    trigger: "/Yes/ I accept the quest"
                    script:
                    - if <player.has_flag[npc_engaged]>:
                        - stop
                    - flag player npc_engaged expire:1m
                    #- engage
                    - narrate format:cchat "Okay great!"
                    - wait 5t
                    - narrate format:instruction_format "Kill 5 zombies!"
                    # Start a counter flag at zero (no zombies killed yet).
                    - flag player kill_zombie_quest_count:0
                    # Jump to the step for finishing the quest and lock it in (no timeout).
                    - zap finish_quest
                    - flag player npc_engaged:!
                    #- disengage
                2:
                    # Even though it's not really needed, add a 'no' response that just zaps back
                    trigger: "/No/ I don't"
                    script:
                    - if <player.has_flag[npc_engaged]>:
                        - stop
                    # More frequently shown messages can get annoying to players who have to see them constantly.
                    # Adding randomness to some messages is a little touch that makes scripts just that little bit nicer for players
                    - random:
                        - narrate format:cchat "Okay screw off!"
                        - narrate format:cchat "Okay then."
                        - narrate format:cchat "Screw you then!"
                    # They refused, so hop back to the default step and wait.
                    - zap *
        # 3rd step: only allowed interaction is click, they're stuck here til they finish the quest
        finish_quest:
            click trigger:
                script:
                # This step doesn't have delayed interactions, so no engage needed.
                # If the quest is marked as completed, give rewards.
                - if <player.has_flag[kill_zombie_quest_complete]>:
                    - narrate format:cchat "Great work! Here's your reward!"
                    - give diamond
                    # Then remove the 'complete' flag and set the cooldown
                    - flag player kill_zombie_quest_complete:!
                    - flag player kill_zombie_quest_cooldown expire:24h
                    # And zap back to the default step so they can retry the quest after the cooldown is done.
                    - zap *
                - else:
                    # Otherwise, just give idle waiting chatter.
                    - random:
                        - narrate format:cchat "You killed those zombies yet?"
                        - narrate format:cchat "I'm still waiting on the zombies."
                        - narrate format:cchat "Are you gonna kill those zombies or what?"

killquest_zombie_world:
    type: world
    events:
        # Listen to the event of a player killing zombies
        # Only listen when the counter flag is present
        after player kills zombie flagged:kill_zombie_quest_count:
        # After the kill, bump the player's kill counter
        - flag player kill_zombie_quest_count:++
        # When it hits five, you're done!
        - if <player.flag[kill_zombie_quest_count]> == 5:
            - narrate format:instruction_format "Zombie Quest Complete: Return to the NPC"
            # So remove the counter (to avoid it continuing to count up) and add a new flag indicating the quest is complete
            - flag player kill_zombie_quest_count:!
            # Alternatively to the flag, using '- zap npc_killquest_interact quest_completed' and a corresponding new step would also work.
            # The flag + if/else was chosen mostly for the sake of having examples of different methodologies.
            - flag player kill_zombie_quest_complete
```
