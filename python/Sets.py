# creating sets

a = set ([0,1,2,3,4,5])
b= set ([2,4,6,8])

print a.union(b)

print a.intersection(b)

# Counts using a dictionary

band = ["mel", "geri", "victoria", "mel", "emma"]

counts = {}

for name in band :
     if name not in counts:
        counts[name] =1
     else: 

        counts[name] +=1
for name in counts:
     print name, counts[name]

#Truth testing an empty dictionary

if {}: print "hi"

d = {"maggie": "uk", "ronnie": "usa"}

print d.items()
print d.keys()
print d.values()
print d.get("maggie")
print d.setdefault("ronnie")







