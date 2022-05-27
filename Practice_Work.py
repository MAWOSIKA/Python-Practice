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
