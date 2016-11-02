name = "Babs Craig"
age = 29 #true story
height = 178
weight = 104 #kg
eyes = 'Brown'
teeth = "white"
hair = 'black'

height_in_feet = height * 0.0328
weight_in_pounds = weight * 2.2

print "Let's talk about %s." % name
print "He's %s inches and %d feet tall." % (height, height_in_feet)
print "He's %d kilograms and %d pounds heavy" % (weight, weight_in_pounds)
print "That's actually pretty heavy"
print "He's got %s eyes and %s hair" % (eyes, hair)
print "His teeth are usually %s depending on what he's had to eat that day" % teeth

#Not so tricky to a JavaScript ninja sir
print "If I add %d, %d and %d I get %d" % (age, height, weight, age + height + weight)
