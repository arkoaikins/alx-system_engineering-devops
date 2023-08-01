#!/usr/bin/env ruby
#regular expression that matches hbn hbtn hbttn hbtttn hbttttn
puts ARGV[0].scan(/hbt*n/).join
