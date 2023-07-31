x=input("enter a string")
for i in x:
    print(i)

    #print ASCII value
    for i in x:
        print(i,ord(i))
#print upper case
for i in x:
    print(i,i.upper(i))

# to print length of string
count=0
for i in x:
    count+=1
print("the length is",count)
