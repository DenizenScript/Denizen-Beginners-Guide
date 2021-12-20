How Sample Scripts Are Formatted In This Guide
----------------------------------------------

When you see a sample script anywhere in this guide, it wil be categorized into one of three color-coded types: Good, Needs-Change, or Bad.

```eval_rst
.. contents:: Table of Contents
    :local:
```

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

### Imperfect Scripts

```dscript_yellow
my_imperfect_script:
    type: task
    script:
    - narrate "ur flag is <player.flag[waffle]> unless <player.has_flag[waffle]> is false oopsie"
```

Imperfect scripts have a green outline. These scripts are valid for learning material but shouldn't be used as-is.

### Bad Scripts

```dscript_red
my_bad_script:
    type: tusk
    scrapt:
    - delete system32
    - narrote 'This ain't work""
```

Scripts that are bad and should not be used have a red outline. These scripts usually demonstrate common mistakes or pitfalls, and are presented only as examples of what **NOT** to do. These scripts may contain typos, errors, misformatting, bad logic, or even just simply outdated syntaxes.
