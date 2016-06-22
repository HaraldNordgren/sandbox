#!/usr/bin/ruby

file = File.open("requirements.txt", "r")

puts file.readlines().grep(/requests/).size > 0

if file.readlines(ARGV[0]).grep(/requests/).size > 0
    puts'gfgfgdgdfgdg'
end

#if File.readlines("testfile.txt").grep(/monitor/).any?

#if File.readlines("testfile.txt").grep(/monitor/).size > 0
#  puts 'sfdf'
#end
