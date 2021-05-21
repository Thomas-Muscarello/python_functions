#Functions can also give back values.
#To do so, you must use "return".
#Return must be the last line in the function beucase it will break out of the function once read

#Function cubes a number
def cube(num):
    return num*num*num

#To call
print(cube(4))

#You can also set the value of a function to a variable:
result = cube(3)
#To call
print(result)