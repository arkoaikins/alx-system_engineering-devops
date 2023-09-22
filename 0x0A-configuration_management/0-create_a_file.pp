# A file in /tmp
# file path is /tmp/school
# permission is 0744
# File owner is www-data
# File group is www-data
# File contains I love Puppet

file {'/tmp/school':
    ensure  => 'file',
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0744',
    content => 'I love Puppet',
}
