#!/usr/bin/env python
from subprocess import Popen, PIPE

scpt = '''
on run {targetBuddyPhone, targetMessage}
	tell application "Messages"
		set targetService to 1st service whose service type = iMessage
		set targetBuddy to buddy targetBuddyPhone of targetService
		send targetMessage to targetBuddy
	end tell
end run'''

args = ['4042728020','Hello']

p = Popen(['osascript', '-'] + args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
stdout, stderr = p.communicate(scpt)
print (p.returncode, stdout, stderr)
