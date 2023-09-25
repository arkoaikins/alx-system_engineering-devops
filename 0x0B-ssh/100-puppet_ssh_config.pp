#!/usr/bin/env bash
# use Puppet to make changes to configuration file

file_line { 'set_ssh_private_key':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/school',
}

file_line { 'disable_password_authentication':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'PasswordAuthentication no',
}
