#string is when we write any statement in between single or double quotes it is called string.
# \n means new line
#'''or""" is used to write multi line string
import string


s="hello world"
print(type(s))

a='''hello i am siddhesh\n
nowdays i am learning python \n
and i am enjoying it'''

print(a)

#indexing:- in python indexing start from 0 if we are couting from left to right and if we are counting from right to left indexing start from -1.

s="hello world"
print(s[2])

print('how are you?'[-4])

#length of string:- we can find the length of string by using len() function.

c="i am learning python"
print(len(c))

#slicing:- slicing is used to get the part of string from the whole string.
#in slicing (start index:end index:step).
#if we did not give start string then it will start from 0 index
#if we did not give end index then it will go till the end of string
#if we did not give step then it will take default step as 1
#end index is always exclusive means it will not include the character at end index.

t="hello world"

print(t[0:7:1])

print(t[1:5:1]) #start from 'e' and end on 'o'

print(t[-1:0:-1])#it will reverse string

print (t[:6:])#it will print from 0 index to 5 index

print(t[:len(t):])#it will print whole string

print(t[:-5:-2])#it will print from last index to 5 index with step -2

#string is immutable means we cannot change the value of string once it is created but we can create a new string by changing the value of existing string.
#exx..,

s="python"
new_s="J"+s[1:]
print(new_s)

#concatination:- it is used to join two or more strings.

f_name="siddhesh"
l_name="garware"

full_name = f_name+" "+l_name
print(full_name)

#repitition:- it is used to repeat the string for n times.(*)

k=("hello "*6)
print(k)

j=("-"*10)

print (j)

#membership operator:- it is used to check whether the string is present in another string or not. (in, not in)

k="helloo sir"
print("l" in k)

print("s" not in k)

#escape sequence:- it is used to print the special character in string. (\n, \t, \\, \', \", etc.)

print("hello \ni am learn\ting \"python")








