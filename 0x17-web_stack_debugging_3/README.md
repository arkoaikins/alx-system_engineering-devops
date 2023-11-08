# debugging :page_with_curl:0x17 Web stack debugging #3

![image](https://github.com/arkoaikins/alx-system_engineering-devops/assets/110135034/b3f0b849-0154-4c2f-9fff-686f47b7b9b2)

## In this project :bulb:

I debugged a Wordpress website running on a LAMP stack.

## Requirements
- Puppet manifests must pass puppet-lint version 2.1.1 without any errors
- Puppet manifests must run without error

### Installation of puppet
`$ apt-get install -y ruby`
`$ gem install puppet-lint -v 2.1.1`

### Task 0
Using strace, find out why Apache is returning a 500 error. Once you find the issue,
fix it and then automate it using Puppet (instead of using Bash as you were previously doing).

HINTS
- `strace` can attach to a current running process
- You can use [tmux](https://intranet.alxswe.com/rltoken/UsSRoxIYdq0l0QUIuDNnSw) to run [strace](https://intranet.alxswe.com/rltoken/ueMevAif95DjyW2sqVCMoA) in one window and `curl` in another one
Requirements:
  - Your `0-strace_is_your_friend.pp` file must contain Puppet code
  - You can use whatever Puppet resource type you want for you fix

Filename:`0-strace_is_your_friend.pp`

how to run `curl -sI 127.0.0.1`, `puppet apply 0-strace_is_your_friend.pp`, `curl -s 127.0.0.1:80 | grep Holberton`
