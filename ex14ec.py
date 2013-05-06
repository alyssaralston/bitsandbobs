from sys import argv

script, husband_name = argv
prompt = '> '

print "Hi Alyssa, this is the %s script. How's %s?" % (script, husband_name)
print "It's not creepy that I know your husband's name, right?"
approval = raw_input(prompt)

print "Great - you said '%s' when I asked you if it was creepy." % approval
