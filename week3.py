#list
l=[1,'o',2.5,9,10]
print(l)
l.append(20)
print(l)
l.insert(0,100)
print(l)
l.pop()
print(l)
l.remove(2.5)
m=l.copy()
print(m)
print(l)

#tuple
t=(1,'o',2.5,9,10) 
print(t)
print(t.count(1))
print(t.index(2.5))




#dictionary
d={"name":"john","age":30,"city":"new york"}
print(d)
print(d["name"])        
d["age"]=31
print(d)  
print(d.keys())
print(d.values())   
print(d.items())
print(d.get("name"))
print(d.pop("age"))
print(d)  

#set
s={1,'o',2.5,9,10}
print(s)
s.add(20)
print(s)
s.remove(2.5)
print(s)
s.difference({1,9})
print(s)
s.pop()
print(s)
s.discard(10)
print(s)
s.intersection({1,9})
print(s)