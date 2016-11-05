from sys import argv

script, user_name = argv

prompt = '_ '

print "Hi, %s. I am the %s script" % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)


if likes == 'no':
    msg = 'That\'s not a nice thing to say to me'
else:
    msg = 'Awwww, shucks, I like you too!'



print """
Alright, so you said  %r about liking me. %r.
You live in %r. Not sure where that is.
And you have a %r computer. Nice!
""" % (likes, msg, lives, computer)
