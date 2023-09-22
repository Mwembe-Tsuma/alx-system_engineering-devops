#manifest that kills a process named killmenow

exec { 'process kill killmenow':
  command     => 'pkill killmenow',
  path        => '/usr/bin',
  onlyif      => 'pgrep killmenow',
  refreshonly => true,
}
