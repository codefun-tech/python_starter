# Command Line Tricks

## Starship

[Starship](https://starship.rs/) is a cross-shell prompt that is fast, customizable, and easy to use. It can display information about the current directory, git status, and more.

## SSH

```shell
ssh-keygen -t ed25519 -C "your_email@example.com"
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

## proxychains

```shell
# Install proxychains-ng
sudo apt install proxychains4
```

Edit the configuration file `/etc/proxychains.conf`:

```text
[ProxyList]
socks5 127.0.0.1 1080
```

Then you can run any command with proxychains:

```shell
proxychains4 curl "http://httpbin.org/ip"
```
