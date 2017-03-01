#Looping through a string

s= 'i love writing python'
for item in s:
   print item,

# print the different element of 5

print s[4]

print s[-1]

print len(s)

#other things just picks out zero element as a string not a list

print s[0]
print s[0] [0]
print s[0] [0] [0]

#splitting a string to loop through a list of words

split_s = s.split()
 
print split_s
   
for item in split_s:
    if item.find('i') > -1:

      print "i found 'i' in : '{0}' ".format(item)


#useful aspects of strings

something = 'completely different'

print something.count('t')

print something.find('plete')

print something.split('e')

thing2 = something.replace('different', 'silly')
print thing2



