# Increase the ULIMIT of the default file

# fixing for nginx
exec { 'fix-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
  notify  => Exec['nginx-restart'], # Notify the nginx-restart
} ->

# Restart Nginx
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/',
  refreshonly => true,
}
