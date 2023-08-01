#!/usr/bin/env ruby
#regular expression that matches hbttn with t fron 2 to 5
#so matching hbttn,hbtttn,hbttttn and hbtttttn
puts ARGV[0].scan(/hbt{2,5}n/).join
