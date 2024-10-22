# sopel-slap

Plugin for Sopel that lets users slap each other in fun ways

## Installation

```sh
pip install sopel-slap
```

_Substitute the appropriate `pip` command based on your environment (e.g.
`pip3` or `pip3.10` on systems with multiple Python versions available)._

_If your Sopel configuration requires it, run `sopel-plugins enable slap`,
passing the appropriate config name to `-c` if you have multiple bots._

## Configuration

The easiest way to configure this plugin is via Sopel's built-in wizard:

```sh
sopel-plugins configure slap
```

Available settings are described below.

### The `verbs` option

`verbs` is a list of verbs to choose from when slapping people. If set, it
overrides the default list.

Probably the easiest way to make a custom list is to just press Enter twice
when the config wizard asks for a list of verbs, which will add the default
list to your bot's `.cfg` file. Then you can use your favorite text editor.

_(We're aware that Sopel's wizard doesn't have great UX when it comes to
entering lists. It'll get worked on someday, probably.)_

### The `reflexive` option

`reflexive` is the pronoun the bot uses when someone with authorization does
`.slap BotNick`. By default, this is set to "itself".

## Commands

<dl>
  <dt>.slap</dt>
  <dd>Make the bot slap you</dd>

  <dt>.slap nickname [reason]</dt>
  <dd>Slap someone else, with an optional reason</dd>
</dl>

_If your bot has a non-default `prefix`, substitute it for `.` above._

## Credits

This is based on [the original `slap.py`][original-slap.py] by Michael Yanovich
from [sopel-extras][], dating back to the late '00s/early '10s. It's been
rewritten more or less from scratch to do things in the modern Sopel way. The
only meaningful behavior change was dropping substitution of the caller's nick
for `me` and `myself`, as it's quite possible for a real person to use either of
those as a nick and _no one_\* should be safe from slaps!

\* — No one except the bot and its admins, that is.

[original-slap.py]: https://github.com/sopel-irc/sopel-extras/blob/81ee756223474cacdac6f5847772d6085d006a50/slap.py
[sopel-extras]: https://github.com/sopel-irc/sopel-extras
