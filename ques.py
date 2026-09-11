#beginner level python string assignment
#Q1. Create a string with your name. Print its length and data type.
n="siddhesh garware"
print(len(n),type(n))

#Q2. Print the first and last character of the string 'DataScience'
g="Datascience"
print(g[0],g[-1])

#Q3. Using negative indexing, print the 3rd character from the end of 'PyMaster'.
j='pymaster'
print(j[-3])

#Q4. Slice 'PROGRAMMING' to extract only 'GRAM'.
h='programming'
print(h[3:7])

#Q5. Reverse the string 'India' using slicing.
o='india'
print(o[::-1])

#intermiddiate level python string assignment

#Q6. Check whether 'Python' is present in 'I love Python programming'.
y="i love python programming"
print('python'in y)

#Q7. Concatenate 'Hello' and 'World' with a space between them.
i='hello'
p='world'
print(i+' '+p)

#Q8. Repeat '*' 20 times to print a separator line.
print('*'*20)

#Q9. Extract every alternate character from 'ABCDEFGHIJ'.
t="ABCDEFHIJ"
print(t[::2])

#Q10. From 'PyMaster India', extract 'India' using slicing.
r='pymaster india'
print(r[9:15])

#Think & Apply questions

#Q11. Try s[0] = 'X' on any string. Observe and explain the error you get.
    
#s='hello'
#s[0]='x'
# this will give error because string are immutable in python means it does change once it get created.we can create a new string by cahnging the valueof existing string but we cannot change the value of existing string.

#correction

s='heloo'
new_s = 'x'+(s[1::])
print(new_s)


#Q12. Write a print statement that outputs: He said "Hello" (include the quotes).

print('He said \"Hello"' )

#Q13. Print a Windows file path: C:\Users\Rajeev\Desktop using escape characters.

print('C:\\Users\\Rajeev\\Desktop')

#Q14. What does s[1:-1] do? Test it on at least three different strings
s="hello everyone"

print(s[1:-1])

s="i am siddhesh"

print(s[1:-1])

s="i like python"

print(s[1:-1])

#Q15. Can you find a slice expression that returns an empty string from 'PYTHON'? Find two different ways.

i='PYTHON'
#first way 
print(i[9::])

#second way
print(i[:0:8])




