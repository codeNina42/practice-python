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
frinds=["apple","orange",5,3.45,False,"akash","sabik"]
print(frinds[1])
frinds[0]="hi"
print(frinds[6])
#arr=input("enter a value").split()
text = "hi,hello,banana,mango"
arr = text.split(",")
print(arr)
text="hi ,my name is sajid Ahsan seyam"
print(text.upper())

friends = ["apple", "orange", "hlw", "hi"]
print(friends[0:2])

fruits = ["apple", "banana", "cherry"]
print("Original:", fruits)#original method

#----------------main list methods-------------

fruits.append("mango")           # add at end
print("append:", fruits)

fruits.insert(1, "orange")       # insert at index 1
print("insert:", fruits)

fruits.remove("banana")          # remove by value
print("remove:", fruits)

fruits.pop(2)                    # remove by index
print("pop:", fruits)

print("index of apple:", fruits.index("apple"))  # find index

fruits.extend(["grape", "kiwi"]) # add multiple
print("extend:", fruits)

print("count of apple:", fruits.count("apple"))  # count item

fruits.sort()                    # sort ascending
print("sort:", fruits)

fruits.reverse()                 # reverse order
print("reverse:", fruits)

copy_fruits = fruits.copy()      # copy list
print("copy:", copy_fruits)

fruits.clear()                   # clear all items
print("clear:", fruits)

