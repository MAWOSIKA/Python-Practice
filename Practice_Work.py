#Naming and using Variables

from email import message


message= "Hello Python Crash Course Reader"
print(message)

#Strings
name ="maryann awosika"
print(name.title())

movie = " the cat in the hat"
print (movie.upper())
print(movie.lower())

#using variables with strings
first_name= "maryann"
last_name = "awosika"
full_name = f"{first_name} {last_name}"
print(full_name)
print(full_name.title())
print ("Hello,", full_name.title() ,"!")
message = f"Hello, {full_name.title()}"
print(message)

#Adding white spaces to strings
phrase = "python code"
print("\tThis", "\n\tis", "\n\t", phrase.title())

# creating program to calculate savings

greeting= "Hello "
name= "Bob"


hourly_wage= 20
hours_per_week= 40
income_per_week = (hourly_wage*hours_per_week)
print(income_per_week)
weeks_per_year= 48
income_per_year = (income_per_week*weeks_per_year)
print(name,"'s yearly income is")
print(income_per_year)


#Expense calculation for savings calculator program
name = "Bob"
spend_per_week=400
spend_per_year= spend_per_week*52
print(name+"'s yearly spend is: ")
print(spend_per_year)


# --- Calculate the yearly savings ---
savings_per_year= (income_per_year-spend_per_year)
print(name+ "'s yearly savings:")
print(savings_per_year)


#sample imperial to metric calculations
feet=6
inches=3
cm=(30*feet+3*inches)
print(cm)


#practice years to hours calculations
hours_per_day=24
days_per_year=365
age= 35
hours_lived= age*days_per_year*hours_per_day
print(hours_lived)

# --- Display a greeting ---
greeting = "Hello "
name= "AWOSIKA"
print(greeting + name)

# --- Calculate the yearly income ---


hourly_wage= 20
hours_per_week= 40
income_per_week= hourly_wage * hours_per_week
weeks_per_year= 48
income_per_year= weeks_per_year * income_per_week

print(name+ "'s yearly income is:")
print(income_per_year)

# --- Calculate the yearly spend ---

spend_per_week= 400
spend_per_year= spend_per_week *52
print(name + "'s yearly spend is:")
print(spend_per_year)


# --- Calculate the yearly savings ---

savings_per_year= income_per_year - spend_per_year
print(name+"'s yearly savings:")
print( savings_per_year)


#practicing functions

print(max(5,10))
print(min(5,10))

#practicing storing function output in a variable

x=min(5,10)
print(x)

a=len("hello")
print(a)

length1= len("cat")
length2=len("mouse")
print(max(length1,length2))

x=75*42
y=66*61
print(min(x,y))


#defining functions examples
def f(x):
    result = x+2
    return result

print(f(1))
print(f(2))
print(f(10))

def g(y):
    result=y*5
    return result

print(g(10))

#example function definition with multiple inputs
def h(a, b):
    result = a + b
    return result

print(h(1, 2))
print(h(5, 7))

#function  definition with multiple calls
def h(a, b):
    result = a + b
    return result

print(h(1, 2))
print(h(5, 7))



#example of changing the name of the function
def test(x):
    return x+2

print(test(1))

def h(z):
    return z*z

print(h(10))



#changing the parameters
def add_together(a, b):
    return a + b
    
print(add_together(3, 4))



def times_three(number):
    result = number * 3
    return result

print(times_three(8))



def add_five(n):
    return n + 5

print(add_five(10))

print(add_five(20))



def make_greeting(name):
    greeting = "Hello, " + name
    return greeting

greeting = make_greeting("Alice")
print(greeting)

greeting = make_greeting("Bob")
print(greeting)

def forty_two():
   return 42

print(forty_two())

def f():
    print("never reached")
    return 123
    
y = f()
print(y)

def f():
    print("make this reachable")
    return 123
    

y = f()
print(y)

def say_hi():
    print("hi")

say_hi()


#Call a function from scratch
def square(number):
    return number * number

print(square(5))
print(square(50))



name1 = "Camilla"
name2 = "Eve"

#Passing arguments in variables
def make_greeting(name):
    greeting = "Hello, " + name
    return greeting

print(make_greeting(name1))
print(make_greeting(name2))


#Mixing built-in and custom functions
def square(number):
    return number * number

x=len("Alice")
print(square(x))

#Calling functions from within functions
def square_length(string):
    length = len(string)
    return length * length

print(square_length("Bob"))

#A function with side effects

def show_greeting(name):
    greeting = "Hello, " + name
    print(greeting)

show_greeting("Daniel")

#defining functions for happy birthday song

def print_happy_birthday(name):
    print("Happy birthday to you")
    print("Happy birthday to you")
    print("Happy birthday dear " + name)
    print("Happy birthday to you")

print("For Alice:")
print_happy_birthday("Alice")

print("And for Bob:")
print_happy_birthday("Bob")



def hello(string):
    print("Hello there, " + string)
hello("Bob")

def goodbye(name):
    print("Goodbye, " + name)

goodbye("Bob")


def multiply(x, y):
    return x*y
    

print(multiply(5, 7))
print(multiply(2, 3))


#examples of Random function from scratch
  
def f(x):
    return x+2

def g(y):
    return y*5

def square(number):
    return number * number

def double_up(x):
    return x *2


def square(number):
    result = number * number
    return result

print(square(5))

def add_three(a, b, c):
    return a + b + c

print(add_three(1,2,3))
def say_hello():
    greeting= "Hello, world!"
    return greeting
    
print(say_hello())

def say_hello():
    print("Hello, world!")

say_hello()


#Sum of lengths
def length_sum(string1,string2):
    length1= len(string1)
    length2= len(string2)
    return length1+length2


def length_sum(string1, string2):
    length1 = len(string1)
    length2 = len(string2)
    result = length1 + length2
    return result
    
print(length_sum("abc", "def"))


#Imperial to metric again
def convert(feet, inches):
    cm= 30.48*feet + 2.54*inches
    return cm

#Multiple functions
def f(x):
    return x+3
def g(y):
    return 5*f(y)
print(g(3))

#Temperature conversion
def c_to_f(degrees):
    result = degrees * 9 / 5
    result = result + 32
    return result

print(c_to_f(25))
print(c_to_f(100))