Sample Scripts
--------------

When you see a sample script anywhere in this guide, it wil be categorized into one of three color-coded types: Good, Needs-Change, or Bad.

### Good Scripts

```dscript_green
my_good_script:
    type: task
    script:
    - narrate "This script can be dropped in!"
```

Good scripts have a green outline. These scripts are good enough to be put into a server as-is and will work (though won't necessarily have much use).

### Needs-Change Scripts

```dscript_blue
my_changeable_script:
    type: task
    script:
    - narrate "You'll have to fill this in"
    - wait (Put your delay here)
    - (put more commands here)
```

Scripts that are good but need changes to work have a blue outline. These scripts usually demonstrate a syntax or contain only part of a script. If you want to try one, you'll have to fill in the missing pieces before loading it in.

### Bad Scripts

```dscript_red
my_bad_script:
    type: tusk
    scrapt:
    - delete system32
    - narrote 'This ain't work""
```

Scripts that are bad and should not be used have a red outline. These scripts usually demonstrate common mistakes or pitfalls, and are presented only as examples of what **NOT** to do.
