# this manifest script creates a file if not exist
package { 'Install flask':
  ensure   => installed,
  name     => 'flask',
  provider => 'pip3'
}
