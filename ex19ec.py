from sys import argv

prompt = ">"

print "How many blocks of cheese do you have?"
amount_of_cheese = raw_input(prompt)
print "How many boxes of crackers do you have?"
amount_of_crackers = raw_input(prompt)

def cheese_and_crackers(amount_of_cheese, amount_of_crackers):
  print "You have %r blocks of cheese and %r boxes of crackers." % (amount_of_cheese, amount_of_crackers)
	print "That's a total of %s square-shaped containers of food." % (int(amount_of_cheese) + int(amount_of_crackers))

print cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can do all kinds of things with this function. Let's change up the amounts!"
cheese_and_crackers(10, 50)
