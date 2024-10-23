# dotfile-sync

An auxiliary tool for syncing dotfiles using `scp`.

The only usage is:

```bash
dotfile-sync <remote-host> <remote-path> <local-path>
```

Example:

![example](assets/example.gif)

which is roughly equivalent to:

```bash
# Make tmpdirs
tmp=$(mktemp -d)
mkdir -p $tmp/local
mkdir -p $tmp/remote

# We work on tmps
cp ~/.zshrc $tmp/local/.zshrc
scp <remote-host>:~/.zshrc $tmp/remote/.zshrc

# Show diff
git diff --no-index $tmp/local/.zshrc $tmp/remote/.zshrc

# If you choose to edit interactively
git difftool --no-index $tmp/local/.zshrc $tmp/remote/.zshrc

# If you choose to sync with local tmp
#   local backup
cp ~/.zshrc ~/.zshrc.dsbak
#   sync
cp $tmp/local/.zshrc ~/.zshrc
```

## Install

```bash
pipx install dotfile-sync
```