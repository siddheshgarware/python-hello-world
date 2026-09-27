#method:-In Python, a method is a function that is associated with an object or a class. Unlike a standalone function (which can be called anywhere in your code), a method must be called on an object using dot notation (e.g., object.method()).
#ex: lower()

#CaseMethod

s='Hello world'
print(s.lower())#make all letter in lowercase
print(s.strip())#Removing unwanted spaces
print(s.lstrip())#removing left spaces 
print(s.rstrip())#removing right spaces
print(s.capitalize())#Only the very first character becomes uppercase.
print(s.swapcase())#Uppercase becomes lowercase and lowercase becomes uppercase. 

#SearchMethods

#FIND()
a="i am learning python"
t=a.find("python")
print(t)
c=a.find("java")#java is not there so it will show -1
print(c)

# #INDEX()
# f=a.index("python")
# print(f)
# k=a.index("java")#java is not there so it will give ValueError

#Count()
text=("python is fun and python is powerful")
print(text.count("python"))

# replace()
text="i love java"
print(text.replace("java","python"))

#split()  very imp
sentence="i am learning python"
print(sentence.split())

# we can split using a specific separator too:
sentence2="apple,ball,notebook,study"
print(sentence2.split(","))

#limit split with max split
print(sentence2.split(",",2))

# String → split() → List

#join()
words = ["Python", "is", "awesome"]
print(" ".join(words))

print("-".join(words))


# Correct:

#" ".join(words)

#Wrong: 

#words.join(" ")

# Think:

# split()
# String → List

# join()
# List → String

#is...methods (it shows true or false)

#isdigit() to check all characters are digits
print("12345".isdigit())#it will show true
print("1234abcd".isdigit())#it will show false

#isalpha() to check all characters are letters
print("abcd".isalpha())#it will show true
print("abcd124".isalpha())#it will show false

#isalnum() is all character are numbers or letter?
print("helloworld".isalnum())#it will show true
print("hello world".isalnum())#it will show false becuase there is a space

#isspace()
print(" ".isspace())#true

# isupper()
print("HELLO WORLD".isupper())#true

#islower()
print("hellow world".islower())#true

#istitle()
print("Hello World".istitle())#true because it is like a tittle

#starstwith()
print("python".startswith("py"))#true

#endswith()
print('python'.endswith("on"))#true

#padding  & allignment

#center()
n='python'
print(n.center(20,'-'))

#ljust()
print(n.ljust(20,"-"))

#rjust
print(n.rjust(20,"-"))

#zfill() this will add zero to the left 
print('6'.zfill(5))#it will show five time zero in left

#*string formating

#fstring
a="sidhesh"
b="18"

print(f"my name is {a} and my age is {b}.")

c=60
d=40

print(f"Total={c+d}")

t="python"
print(f"i am learning {t.upper()}")


#Decimal formating

# .2f
n=98.3479
print(f"{n:.2f}")#it will print two decimal degits

p=95.2
print(f"{p:.2f}")

#adding commas in big numbers
money=1000000
print(f"{money:,}")

#fomrmat()
name= "siddhesh"
age="18"

print('Hello i am {}!'.format(name))

print("my name is {} and my age is {}".format(name,age))

#%formatting
n= "python"
print("i am learning %s"% n)

#r" "(raw string)
print(r"C:\Users\siddh\OneDrive\Desktop\PythonCodes")#sometime we want to add special a=character but also want to not show its like using \ so ud this










