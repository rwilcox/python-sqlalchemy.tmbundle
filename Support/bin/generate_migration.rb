#!/usr/bin/env ruby

require "#{ENV["TM_SUPPORT_PATH"]}/lib/ui"
require "#{ENV["TM_SUPPORT_PATH"]}/lib/textmate"
name = TextMate::UI.request_string(
  :title => "Migration Generator", 
  :default => "adding table foo",
  :prompt => "Name/describe the new migration:",
  :button1 => 'Create'
)

if ENV['SQLALCHEMY_MANAGE_SCRIPT']
  system "cd `dirname #{ENV['SQLALCHEMY_MANAGE_SCRIPT']}` && python #{ENV['SQLALCHEMY_MANAGE_SCRIPT']} script '#{name}'"
  TextMate.rescan_project
  puts "Migration created, find it in your version folder"
else 
  puts "Please define SQLALCHEMY_MANAGE_SCRIPT to point to your manage.py script"
end