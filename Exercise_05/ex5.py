name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height_cm = height * 2.54
weight = 180 # lbs
weight_kg = weight * 0.45359237
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print("Let's talk about %s" % age)
print("He's %d inches tall" % height)
print("He's %d pounds heavy" % weight)
print("Actually that's not too heavy")
print("He's got %s eyes and %s hair" % (eyes, hair))
print("His teeth are usually %s depending on the coffee." % teeth)

# this line is tricky, try to get it exactly right
print("If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight))
print("eyes - %r, age - %r" % (eyes, age))
print("height in centimetres - %f, weight in kilos - %f" % (height_cm, weight_kg))