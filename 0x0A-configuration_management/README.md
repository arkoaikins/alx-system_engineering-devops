# Configuration management

##Overview
- This is a system Deveops project
- Configuration management has to do with the systematic handling changes to a system in a way that it maintains integrity over time

Different configuration management tools are available
- Puppet
- Ansible
- Chef and Salt
In this project the configuration management tool used is
 - Puppet

## Installing Puppet
- install puppet 5.5 on Ubuntu 20.4
```bash
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
```
No need to upgrade versions, This project is simply a set of tasks just to familiarize with the basic level syntax which is virtually identical newer
versions of Puppet

[Puppet 5 Docs](https://intranet.alxswe.com/rltoken/fsIr2xFkJHTkaXwqZFFcbA)

- Install puppet-lint
```bash
$ gem install puppet-lint
```
