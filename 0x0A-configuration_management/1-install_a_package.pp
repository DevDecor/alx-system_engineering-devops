# this manifest script creates a file if not exist
package { 'Install flask':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => 'pip3'
}
