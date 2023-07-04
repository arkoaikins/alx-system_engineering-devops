#!/usr/bin/env ruby
#regular expression that matches hbtn and htn
puts ARGV[0].scan(/hb?tn/).join
