#manifest that kills a process named killmenow

exec { 'process kill killmenow':
  path        => 'usr/bin',
  command     => 'pkill killmenow',
  onlyif      => 'pgrep killmenow',
  refreshonly => true,
}
