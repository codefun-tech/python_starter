# Command Line Tricks

## Starship

[Starship](https://starship.rs/) is a cross-shell prompt that is fast, customizable, and easy to use. It can display information about the current directory, git status, and more.

## SSH

```shell
ssh-keygen -t ed25519 -C "your_email@example.com"
```

## Bash

```shell
export https_proxy=http://127.0.0.1:1080
export http_proxy=http://127.0.0.1:1080
export all_proxy=socks5://127.0.0.1:1080
```

## Git

### SSH Protocol

For remote has a format like:

```text
git@github.com:username/repository.git
```

install openbsd-netcat:

```shell
sudo apt install netcat-openbsd
```

Export the `GIT_SSH_COMMAND` environment variable:

```shell
export GIT_SSH_COMMAND='ssh -o ProxyCommand="/usr/bin/nc.openbsd -X 5 -x 127.0.0.1:1080 %h %p"'
```

Or add the following configuration to `~/.ssh/config`:

```text
Host github
  HostName github.com
  User git
  ProxyCommand /usr/bin/nc.openbsd -X 5 -x 127.0.0.1:1080 %h %p
```

### HTTP or HTTPS Protocol

For remote has a format like:

```text
https://github.com/username/repository.git
```

Set global configuration:

```shell
git config --global http.proxy socks5://127.0.0.1:1080
git config --global https.proxy socks5://127.0.0.1:1080
```

Show current configuration:

```shell
git config --global --get http.proxy socks5
git config --global --get https.proxy socks5
```

Unset global configuration:

```shell
git config --global --unset http.proxy socks5
git config --global --unset https.proxy socks5
```

## Curl

```shell
curl -x "socks5://user:pwd@127.0.0.1:1234" "http://httpbin.org/ip"
curl --socks5 "127.0.0.1:1234" "https://ip.oxylabs.io/" --proxy-user user:pwd
```

## proxychains-ng

```shell
# Install proxychains-ng
sudo apt install proxychains4
```

Edit the configuration file `/etc/proxychains4.conf`:

```text
[ProxyList]
socks5 127.0.0.1 1080
```

Then you can run any command with proxychains:

```shell
proxychains4 curl "http://httpbin.org/ip"
```

## Glow

[Glow](https://github.com/charmbracelet/glow) is a terminal-based markdown reader that allows you to view markdown files with syntax highlighting and formatting.

```shell
glow            # List all markdown files in the current directory and below
glow README.md   # View the README.md file
glow -t Rainbow README.md  # View the README.md file with the Rainbow theme
```

## zoxide

[zoxide](https://github.com/ajeetdsouza/zoxide) is a smarter cd command that allows you to quickly navigate your filesystem using a ranking algorithm based on your usage patterns.

```shell
eval "$(zoxide init bash)"  # For bash
eval "$(zoxide init zsh)"   # For zsh
eval "$(zoxide init fish)"  # For fish
```

```shell
zoxide add /path/to/directory    # Add a directory to zoxide's database
zoxide query                     # List all directories in zoxide's database
zoxide query keyword             # Search for a directory using a keyword
zoxide query -ls                # List all directories in zoxide's database with their scores
zoxide query -ls keyword        # List all directories that match the keyword with their scores
zoxide remove /path/to/directory # Remove a directory from zoxide's database
```

```shell
z                   # add current directory to zoxide's database
z keyword           # navigate to the most frequently used directory that matches the keyword
z keyword keyword2  # navigate to the most frequently used directory that matches both keywords
```

```shell
zi keyword      # navigate to the least frequently used directory that matches the keyword
```
