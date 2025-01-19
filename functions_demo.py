#If one flower has an even number of petals and the other has an odd number of petals, then Timmy and Sarah are in love.
#Otherwise, they are not in love.
#the task is to write a function that checks the number of petals on each flower and determines whether they are in love or not based on the rule.

def lovefunc( timmys_petals,sarahs_petals):
    if (timmys_petals %2 == 0 and sarahs_petals %2 != 0) or (timmys_petals %2 !=  0 and sarahs_petals %2 ==0):
        return True
    return False
print (lovefunc(4,5))


# print a function with two arugument  if name equals hello print hello boss
# otherwise print hello guest

def greet(name,owner):
    if (name == owner):
        return "hello boss"
    else:
        return "hello guest"

    
print( greet("rika","rika"))
print( greet("rika", "bob"))


# using addtive inverse
# inverting of "+" to"-" and "-" to "+"

def invert (lst):
    return [-num for num in lst]

print(invert([1,2,3,4,5]))
print(invert([1,-2,3,-4,5]))

#what century is it when it is a strinf

def what_century(year):
    
    year = int(year)
    century = (year+99) // 100
    return century
print(what_century(2025))
print(what_century(1906))

def what_century(year):
    # Convert the input year string to an integer
    year = int(year)
    # Calculate the century
    century = (year + 99) // 100

    # Determine the correct ordinal suffix
    if 10 <= century % 100 <= 20:  # Special case for 11th, 12th, 13th
        suffix = "th"
    else:
        last_digit = century % 10
        if last_digit == 1:
            suffix = "st"
        elif last_digit == 2:
            suffix = "nd"
        elif last_digit == 3:
            suffix = "rd"
        else:
            suffix = "th"

    # Combine the century number and suffix
    return f"{century}{suffix}"
print(what_century(2145))

#Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
def even_or_odd(number):
    if number %2==0 :
        return "even" 
    else:
        return "odd"
print(even_or_odd(47))

#    OR 
def even_or_odd(number):
    return 'Odd' if number & 1 else 'Even'


#    OR

def even_or_odd(number):
    return "Even" if number % 2 else "Odd"

   #  return "truthy_value" if condition else "falsy_value"




