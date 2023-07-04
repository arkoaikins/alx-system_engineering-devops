#!/usr/bin/env ruby
#Regular expression that matches hbtn, hbttn, hbttt, hbttttn
puts ARGV[0].scan(/hbt{1,4}n/).join
