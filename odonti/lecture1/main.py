
# first funtion program
name = input("what is your name:")
# print("Hello World")
print("hello, name")

# another way to concatenate:
print("Hello", end = " ")
print(name)


# fstrings
print(f"Hello, '{name}'")

# strip function:
print(f"{name.strip()}")



# addin integers:
a = 4
b = 5
z = a + b
print(z)

# ask user for the numbers:
num1 = int(input("whats num1: "))
num2 = int(input("whats num2:"))
m = num1 + num2

a = int(input("whats a:"))
b = int(input("whats b:"))
v = a + b
print(m , v)



# ask users for their name and remove whitespace from the str and capitalize the first letter of each word:
name = input("whats your name?: ").strip()
print(f"Hello, {name}")

# changing name to uppercase:
name = input("What is you name? : ").upper()
print(name)


# asking for users first and last name with whitespaces and first letter to be uppercase
first_name = input("What is your first name?: ")
last_name = input("What is your last name?: ")
name = first_name.strip().title() + " " + last_name.strip().title()
print(f"Hello, {name}")


# DEF FUNCTIONS:
# printing hollo world: 
def hello():
    print("Hello World")
hello()

def name():
    print("Isaac")
name()

def father():
    print("Afrifa")
father()

calculations
def add():
    a = 4
    b = 5
    c = a + b
    print(c)
add()

def sub():
    n = int(input("what's n?: "))
    h = int(input("what's h?: "))
    nun = n - h
    print("the number nun:", nun)
   

sub()



from email import message


def name():
    name = input("whats your name?: ")
    print("Hello,", name.strip().upper())
name()


# greetings with users name: calling it multiple times
def greet(name):
    message = f"Hello, {name.strip().title()}"
    return message
greetings = greet("isaac")
print(greetings)
print(greetings)
print(greetings)

# calling the cat functions multiple times:
def cat():
    print("meow")
cat()
cat()
cat()

#  without using a function, this is how our code would be like:
temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)

# with the help of a function: you can call out multiple functions
def fahrenheit_to_celsius(temperature):
    return (temperature - 32) * 5 / 9
print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

# a function that returns value:
def get_greetings():
    return "Hello, World"
message = get_greetings()
print(message)

# returning the value with first letter upper:
def my_name():
    return "isaac".title()
name = my_name()
print(name)

# creating my own function with f - string:
def greetings():
    greet = f"Hello My dear, {my_name()}"
    return greet
message = greetings()
print(message)


# creating my own function with f - string in concatenation:
def my_function(fname):
    print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")


    
# creating my own function using the main():
def main():
    mate = (input("Who is your favourite class mate?: "))

    hello() 

def hello(to = "world"):
    print("hello,", to)

main()


# asking for users input and calling it using the main function:
def main():
    church = input("who is your choir leader? : ")
    
    greet()
def greet(hi = "man"):
    print("welcom", hi)

main()

# taking users input and return a value:
def main():
    num = int(input("What is x? : "))
    print("The square of x is:" ,square(num))

def square(n):
    return n*n    
main()


# user input his own message and print it out:
sentence = input("what is your name? ")
print(sentence)



# creating your a function: using (def)
def lovers_of_money():
    message = "This is my funny statement"
    print(message)
lovers_of_money()
lovers_of_money()
lovers_of_money()


# taking a users funny input:
def car_fun():
    message = input("What is your funny statement?: ")
    print(message)
car_fun()
car_fun()
car_fun()
car_fun()

# using def main:
def main():
    father = input("what is your father's name? : ")
    print("I love you", father)
main()


# asking users for their age:
def main():
    age = int(input("How old are you? : "))
    print("I am ", age ,"years old")
main()

