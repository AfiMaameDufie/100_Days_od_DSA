age = 10
name = "Afi"
print("My name is {0}. I am {1} years old.".format(name,age))
print("My name is %s. I am %s years old." % (name, age))
print("My name is {name}. I am {age} years old.".format(name=name, age=age))

# >>> age = 10
# >>> name = "Afi"
# >>> print("My name is {0}. I am {1} years old.".format(name,age))
# My name is Afi. I am 10 years old.
# >>> print("My name is %s. I am %s years old." % (name, age))
# My name is Afi. I am 10 years old.
# >>> print("My name is {name}. I am {age} years old.".format(name=name, age=age))
# My name is Afi. I am 10 years old.
