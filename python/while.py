# creating a while loop

num = 1
while num <= 10:
    num += 2
    print num

#creating a for loop

mylist = [23, "hi", 2.4**-10]
count = 0

while count < 3:
    item = mylist[count]
    print item, mylist.index(item)
    count += 1

#testing truth 

x = 1
if x: print x, " is True"
