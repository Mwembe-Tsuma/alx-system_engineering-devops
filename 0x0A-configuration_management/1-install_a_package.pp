#Creating a puppet file in /tmp/school

package { 'puppet-lint':
  ensure   => '2.1.0',
  provider => 'gem',
}
