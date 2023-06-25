# this manifest script kills the killmenow
exec { 'kill_killmenow_process':
  command  => 'pkill -f killmenow',
  provider => shell,
  onlyif   => 'pgrep -f killmenow',
}

