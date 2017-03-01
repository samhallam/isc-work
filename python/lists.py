# lists and slicing

mylist = [1,2,3,4,5]

print mylist[2]

print mylist[1]

print mylist[1:]

print mylist[:]

print mylist[1:4]



# create a list from a range


list = range(1,10,1)
print list

list = range(1,11,1)
print list

list[0]=10
print list

list.append(11)
print list

list2=[12,13,14]
list.extend(list2)
print list

#combining lists and loops

forward=[]
backward=[]
values = ["a", "b", "c"]
for item in values:
    forward.append(item)
    backward.insert(0,item)
print "forward", forward
print "backward", backward

forward.reverse()
print "forward", forward

# what else to do with a list

countries=["uk", "usa", "uk", "uae"]
countries.count("uk")






