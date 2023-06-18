number = numero = 25.2

print(id(number), id(numero)) # Same identifier, so same memory adress

number = 11.7

print(id(number), id(numero)) # Different identifiers, after reassigning "number"

sum = number + numero

print(type(sum)) # See the type of a variable
print(id(sum)) # See the unique identifier of a variable

print(number, numero, sum)

Rogerinho = "Good dog."
rogerinho = "Also good dog."

print(id(Rogerinho), id(rogerinho))

# Camel Case naming pattern
numberOfSubs = 5

# Pascal Case naming pattern
NumberOfSubs = 5

# Snake Case naming pattern
number_of_subs = 5

