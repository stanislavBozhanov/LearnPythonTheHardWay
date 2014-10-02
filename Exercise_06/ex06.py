# this is a format string assigned to a variable called x
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and thos who %s." %(binary, do_not)
print(x)
print(y)

print("I said: %r." % x)
print("I also said: '%s'." % y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# we print a formated stirng splitted in two variables
print(joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side."

print w + e