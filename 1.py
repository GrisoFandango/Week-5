x = 15
y = 5
# +  is a concatenator, but can concatenate only
#strings. Because X and Y are integers, we need
#to put str() to concatenate the result
print("X + Y is equal\t" + str(x + y))
print("X * Y is equal\t" + str(x * y))
print("X - Y is equal\t" + str(x - y))
print("X / Y is equal\t" + str(x / y))
#Here instead we used comma, that is not a
#concatenator,so, does not need the use of
#str()
print("X + Y is equal\t",x+y)
print("X * Y is equal\t",x*y)
print("X / Y is equal\t",x/y)
print("X - Y is equal\t",x-y)
