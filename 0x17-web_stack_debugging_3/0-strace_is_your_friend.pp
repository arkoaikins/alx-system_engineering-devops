# A puppet code to fix the issue on why Apache is returnung a 500 error
exec { 'fix 500 error':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path => '/usr/local/bin/:/bin/'
}
