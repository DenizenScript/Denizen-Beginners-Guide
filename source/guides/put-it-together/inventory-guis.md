An Inventory GUI Menu (PLACEHOLDER ONLY)
---------------------

**TODO: Notice about required section reading before starting this.**

**TODO: Write-up guiding players from start to finish through writing an inventory GUI menu script.**

### Placeholder

Until this page is written, you can view the [old tutorial video here](https://one.denizenscript.com/denizen/vids/Inventory%20GUIs).

### Update Notice

In the tutorial video, it is taught to cancel the generic clicks event, and run actions in response to the more specific event.

While this is still correct, it is missing a necessary component to work well in modern Denizen.

In the past, events would just all fire, and if an event got cancelled that just means the underlying action wouldn't be performed. In modern Denizen, the system more intelligently knows to not fire more script events after the event was cancelled. While this [can be simply disabled for the relevant events](https://one.denizenscript.com/denizen/lngs/Script%20Event%20Cancellation) a better solution is to instead guarantee that the generic event that cancels it will run *last*. This is as easy as adding a high-valued `priority` to the cancelling event line.

So, where previously you had `on player clicks in my_inventory:` you now instead have `on player clicks in my_inventory priority:100:`, and a similar change to the `drags` event line. Event priorities run in numerical order, with a default of `0`. So all the specific events, with their default priority, will run first, and then only after they're done, the generic cancellation events <span class="parens">(now at priority `100`)</span> will fire last.


### Related Technical Docs

If you want to read some more about tools used for Inventory GUIs, here are a few technical guides you might consider...

- [Inventory script containers doc](https://one.denizenscript.com/denizen/lngs/inventory%20script%20containers)
- [Priority language doc](https://one.denizenscript.com/denizen/lngs/script%20event%20priority)
