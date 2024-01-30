#!/usr/bin/env ruby

# Check if there is exactly one command-line argument
if ARGV.length != 1
  puts "Usage: #{$0} <string>"
  exit 1
end

# Extract the argument
input_string = ARGV[0]

# Define the regular expression to match the specified repetition pattern
pattern = /hb(t{2,5})n/

# Use scan to find matches and output the matched repetition part
matches = input_string.scan(pattern)

if matches.any?
  puts matches.flatten.join
else
  puts "No match"
end
