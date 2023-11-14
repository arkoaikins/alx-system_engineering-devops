# Puppet code to eliminate failed requests and improve overall server performance

# improve the limit of the server
exec { 'improve server':
  command => 'sed -i "s/15/3000/" /etc/default/nginx',
  path    => '/usr/local/bi/:/bin/'
}

#Restart the webserver
exec{'restart the server':
  command => 'nginx restart',
  path    => '/etc/init.d/',
}
