# dotfile-manager

这个脚本可以用来管理多个设备间的配置文件 (dotfiles)。

## 安装

先决条件:
- Python 3.8+
- `git`
- `nvim` 或 `VSCode` 用于diff

然后通过`pipx`安装（推荐）:

```bash
pipx install dotfile-manager-aquanjsw
```

## 使用示例

1. 在第一台设备`A`上
    1. 添加配置文件到本地数据库
        ```bash
        dotfile-manager r zsh ~/.zshrc
        dotfile-manager r zsh ~/.oh-my-zsh/custom/custom.zsh
        dotfile-manager r nvim ~/.config/nvim/init.lua
        ```
    2. 然后推送数据库（默认为`~/.dotfiles`文件夹）到远程仓库
2. 在第二台设备`B`上
    1. 从远程仓库拉取数据库
        ```bash
        # REMOTE="https://github.com/xxx/dotfiles.git"
        git clone $REMOTE ~/.dotfiles
        ```
    2. 同步配置文件
        ```bash
        # 注册dotfiles，即使dotfile不存在
        dotfile-manager r zsh ~/.zshrc
        dotfile-manager r zsh ~/.oh-my-zsh/custom/custom.zsh
        dotfile-manager r nvim ~/.config/nvim/init.lua

        # 建议commit备份
        cd ~/.dotfiles && git add . && git commit -m "add B"

        # 仅同步 '~/.zshrc'
        dotfile-manager s A zsh .zshrc

        # 同步应用 'zsh'
        dotfile-manager s A zsh

        # 同步所有dotfiles
        dotfile-manager s A

        # 如果你想将dotfiles恢复到本地数据库的dirty working tree
        dotfile-manager s B

        # 未来，如果你想将本地更改同步到本地数据库
        dotfile-manager s
        ```

> [!TIP]
> 如果你不慎注册了错误的记录, 你可能需要使用一些外部工具进行修改, 比如
> [DB Browser for SQLite](https://sqlitebrowser.org/),
> [VSCode SQLite3 Editor extension](https://marketplace.visualstudio.com/items?itemName=yy0931.vscode-sqlite3-editor)
> 等等。