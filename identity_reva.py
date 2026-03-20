#Integer
a = 7
print("Integer Before:", id(a))
a = a + 5
print("Integer After:", id(a))

#Float
b = 8.5
print("\nFloat Before:", id(b))
b = b + 2.5
print("Float After:", id(b))

#String
c = "computational"
print("\nString Before:", id(c))
c = c + ""
print("String After:", id(c))

#List
L = [1, 2, 3]
print("\nList Before:", id(L))
L.append(4)
print("List After:", id(L))

#Tuple
t = (1, 2, 3)
print("\nTuple Before:", id(t))
t = t + (4,)
print("Tuple After:", id(t))

#sets 
s = {1,2,3}
print("\nset Before:", id(s))
s.add(4)
print("set after:", id(s))