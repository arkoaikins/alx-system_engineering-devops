#!/usr/bin/env ruby
#regular expression
puts ARGV[0].scan(/^\d{10,10}$/).join
