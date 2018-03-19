SublimeLinter-contrib-ansible-review
====================================

[![Build Status](https://travis-ci.org/nvtkaszpir/SublimeLinter-contrib-ansible-review.svg?branch=master)](https://travis-ci.org/nvtkaszpir/SublimeLinter-contrib-ansible-review)

This linter plugin for [SublimeLinter][docs] provides an interface to [ansible-review](https://github.com/willthames/ansible-review). It will be used with files that have the “Ansible” syntax.

## Known limitations

* Messages such as ``WARN: Best practice...`` are not shown, because of they do not match regex. Not to mention
that some of them are just wrong (for example indentation rules for YAML).

* You must set syntax for given file to be Ansible, and then you can run `Lint this view`.

## Installation
SublimeLinter 4 must be installed in order to use this plugin. If SublimeLinter 4 is not installed, please follow the instructions [here][installation].

### Linter installation
Before using this plugin, you must ensure that `ansible-review` is installed on your system. To install `ansible-review`, do the following:

1. Install [Python](http://python.org/download/) and [pip](http://www.pip-installer.org/en/latest/installing.html).

1. Install `ansible-review` by typing the following in a terminal:
   ```
   [sudo] pip install ansible-review
   ```

**Note:** This plugin requires `ansible-review` 0.13.4 or later.
Actually it was not tested with anything older.

### Syntax installation
Also ensure that [Ansible](https://github.com/clifford-github/sublime-ansible) is installed in Sublime Text. To install `Ansible`, do the following:

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette][cmd] and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `ansible`. Among the entries you should see `Ansible`. If that entry is not highlighted, use the keyboard or mouse to select it.

**Note:** If `Ansible` syntax is not installed this plugin will not work.

#### Syntax configuration
To be able to automatically open the `.yml` files in an Ansible project with the Ansible syntax, `ApplySyntax` needs to be configured with the settings below. If this is not done the `.yml` files will be opend with the YAML syntax and the linter plugin will not work without manually change the syntax for every file.

The settings can be found under:

```
Sublime Text -> Preferences -> Package Settings -> ApplySyntax -> Settings - User
```

```
    "syntaxes": [{
        "name": "Ansible/Ansible",
        "rules": [
          {"file_name": ".*/tasks/.*.yml$"},
          {"file_name": ".*/handler/.*.yml$"},
          {"file_name": ".*/*_vars/.*.yml$"},
          {"file_name": ".*/roles/.*.yml$"},
          {"file_name": ".*/playbooks/.*.yml$"},
          {"file_name": ".*/.*ansible.*/.*.yml$"}
        ]
      }]
```

### Linter configuration
In order for `ansible-review` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once you have installed and configured `ansible-review`, you can proceed to install the SublimeLinter-contrib-ansible-review plugin if it is not yet installed.

### Plugin installation

This package is not in the PackageControl, but you can use it by cloning repo:

```bash
cd ~/.config/sublime-text-3/Packages
git clone https://github.com/nvtkaszpir/SublimeLinter-contrib-ansible-review
```

After that restart SublimeText.

### Recommended plugin
It is highly recommended to also install the Sublime plugin [Trailing Spaces](https://github.com/SublimeText/TrailingSpaces) by using [Package Control][pc]. And to set the `Trim On Save` option to `true`.

The settings can be found under:

```
Sublime Text -> Preferences -> Settings
```

```
    { "trailing_spaces_trim_on_save": true }
```

## Settings
For general information on how SublimeLinter works with settings, please see [Settings][settings]. For information on generic linter settings, please see [Linter Settings][linter-settings].

In addition to the standard SublimeLinter settings, SublimeLinter-contrib-ansible-review provides its own settings. Those marked as “Inline Setting” or “Inline Override” may also be [used inline][inline-settings].

|Setting|Description|Inline Setting|Inline Override|
|:------|:----------|:------------:|:-------------:|
|c|CONFIGFILE, Location of configuration file|&#10003;|&#10003;|
|d|RULESDIR, Location of standards rules, directory|&#10003;|&#10003;|
|r|STANDARDS_FILTER, limit standards to specific names|&#10003;|&#10003;|
|s|Only check rules whose id/tags do not match these values.|&#10003;|&#10003;|

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modifications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.
- Please use descriptive variable names, no abbreviations unless they are very well known.

Thank you for helping out!

[docs]: http://sublimelinter.readthedocs.org
[installation]: http://sublimelinter.readthedocs.org/en/latest/installation.html
[locating-executables]: http://sublimelinter.readthedocs.org/en/latest/usage.html#how-linter-executables-are-located
[pc]: https://sublime.wbond.net/installation
[cmd]: http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
[settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html
[linter-settings]: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
[inline-settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html#inline-settings
