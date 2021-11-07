Fancier Sticks: Making Custom Items (PLACEHOLDER ONLY)
-----------------------------------

**TODO: Write-up that introduces item script containers, and the general ideas of making custom items, mentioning recipes, name/lore, mechanisms, item flags, etc.**

### Placeholder

Until this page is written, you can view the [old tutorial video here](https://one.denizenscript.com/denizen/vids/Custom%20Items).

### Sample Script

Here's a quick sample of a modern item script.

```dscript_green
my_item:
    type: item
    material: stick
    display name: <&b><bold>Fancy stick!
    lore:
    - <&7>So fancy.
```

You can get this item in-game by typing `/ex give my_item`

### Related Technical Docs

If you want to read a lot more about the custom items, here are a few technical guides you might consider...

Note: most users, especially those learning from the Denizen for the first time, should just continue on to the next guides page. These references might be of interest to later come back to after you've learned Denizen as far as this guide teaches.

- [Item script containers doc](https://meta.denizenscript.com/Docs/Languages/item%20script%20containers)
- [Book script containers doc](https://meta.denizenscript.com/Docs/Languages/book%20script%20containers)
