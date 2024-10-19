# dotfile-manager

[中文README](doc/README-zh-hans.md)

This is a simple dotfiles manager that I use to manage my dotfiles
(configuration files) across multiple devices

## Install

Prerequisites:
- Python 3.8+
- `git`
- `nvim` or `VSCode` for diffing

Then install the package via `pipx` (recommended):

```bash
pipx install dotfile-manager-aquanjsw
```

## Example

1. On the first device `A`
    1. Add dotfiles to local database
        ```bash
        dotfile-manager r zsh ~/.zshrc
        dotfile-manager r zsh ~/.oh-my-zsh/custom/custom.zsh
        dotfile-manager r nvim ~/.config/nvim/init.lua
        ```
    2. Then push the database (the `~/.dotfiles` folder by default) to remote
2. Then on another device `B`
    1. Pull the database from remote
        ```bash
        # REMOTE="https://github.com/xxx/dotfiles.git"
        git clone $REMOTE ~/.dotfiles
        ```
    2. Sync the dotfiles
        ```bash
        # Register anyway, even if the dotfile does not exist
        dotfile-manager r zsh ~/.zshrc
        dotfile-manager r zsh ~/.oh-my-zsh/custom/custom.zsh
        dotfile-manager r nvim ~/.config/nvim/init.lua

        # Commit the backup is recommended
        cd ~/.dotfiles && git add . && git commit -m "add B"

        # Sync only the dotfile '~/.zshrc'
        dotfile-manager s A zsh .zshrc

        # Sync only the app 'zsh'
        dotfile-manager s A zsh

        # Sync all the dotfiles
        dotfile-manager s A

        # If you want to restore the dotfiles to the dirty working tree
        # of your local database
        dotfile-manager s B

        # In the future, if you want to sync the local changes to
        # local database
        dotfile-manager s
        ```

> [!TIP]
> If you've registered a wrong record by mistake, you may want to use
> some external tools like [DB Browser for SQLite](https://sqlitebrowser.org/),
> [VSCode SQLite3 Editor extension](https://marketplace.visualstudio.com/items?itemName=yy0931.vscode-sqlite3-editor), etc.
