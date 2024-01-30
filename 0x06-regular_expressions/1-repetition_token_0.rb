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

# Check if the input string matches the pattern
if match = input_string.match(pattern)
  puts match[1] # Output the matched repetition part
else
  puts "No match"
end
