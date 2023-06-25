# this manifest script kills the killmenow
exec { 'Kill the process':
  command => 'pkill -f killmenow'
}
