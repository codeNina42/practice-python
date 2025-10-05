#python -i "$(FULL_CURRENT_PATH)"
#chapter 2
#--------------------variable.py-------------------------------------
#integer number
print("integer number")
a=1
b=2
print(a+b)


#float number

a=20.5
b=30.5
print("float number")
print(a+b)

#string

print("string")
a="harry"
print(a)


#boolean

print("boolean")

a=True
print(a)

#special character

print("soecial character")

_samer="hi"
print(_samer)
#S@mmer="hi"
#print(samer) is not working becase it is not working
 
#----------------------operator---------------------

# arithmetic operator
a = 34
b = 4
c = a + b
print("arithmetic oparator")
print(c)

#assingment oparator
a=4-2 #assin 4-2 in a
print(a)
#increment/decrement/multiple/division
b=7
b-=3
print(b)

#comparison oparator(true/false/==)
d=5>4
print(d)

d=5==5
print(d)

#logical oparator
# Logical operators
print("Logical operators\n")

# Example
e = True or False
print(e)  # True

print("True or False =", True or False)  # fixed typo

# ------------------- Truth Table -------------------
print("\nTruth table for OR (or):")
print("A\tB\tA or B")
for A in [True, False]:
    for B in [True, False]:
        print(A, "\t", B, "\t", A or B)

print("\nTruth table for AND (and):")
print("A\tB\tA and B")
for A in [True, False]:
    for B in [True, False]:
        print(A, "\t", B, "\t", A and B)

print("\nTruth table for NOT (not):")
print("A\tNot A")
for A in [True, False]:
    print(A, "\t", not A)


print("A\tB\tA AND B")
for A in [True, False]:
    for B in [True, False]:
        print(A, "\t", B, "\t", A and B)

#---------------------------typr casting--------------------------------
print("type pasting")
a=31
t=type(a)
print(t)
#string for type casting
a="seyam"
t=type(a)
print(t)
b=31.2
t=type(b)
print(t)

#-------------------------input function-------------------------------
a=int(input("enter number 1 :"))
b=int(input ("enter number 2 : "))

#---------------------------string _----------------------------
name="seyam"
print(name[0:3])
print(name[-4:-1]) #-5,-4,-3,-2,-1,0
print(name[1:3])
print(name[0:5])
print(name[1:])
print(name[0:])
word="abcdefghijklmnopqrstuvwxyx"
print(word[1:9:4])
name="seyam are"
print(len(name))
print(name.endswith("yama"))#ends with
print(name.startswith("sey"))#start with
print(name.capitalize())#capitalize the first latter
print(name.lower())#lower case
print(name.upper())#upper case
print(name.title())#title
print(name.strip())#cut the space inside the collon
print(name.replace("seyam","snake"))
print(name.split())
words = ["Seyam", "is", "learning", "Python"]
sentence = " ".join(words)
print(sentence)#join the substring

print(name.find("a"))#same
print(name.find("e"))#find the alphabatic index
print(name.count("e"))#count the alphabet happend
print(name.startswith("sey"))


print("number is :" , a)
print("number is: " ,b)
print ("sum is :" ,a+b)

#alhamdulillah xhapter 2 is complete
