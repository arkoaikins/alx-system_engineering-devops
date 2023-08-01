#!/usr/bin/env ruby
#Regular expression that matches hbtn, hbttn, hbttt, hbttttn
puts ARGV[0].scan(/hbt+n/).join
