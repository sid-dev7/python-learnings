#inetersections
s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}
# {30, 40}
print(s1.intersection(s2))
# {30, 40}
print(s2.intersection(s1))

#union 
s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}
# {10, 20, 30, 40, 50, 60}
print(s1.union(s2))
# {10, 20, 30, 40, 50, 60}
print(s2.union(s1))


#difference 
s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}
# {10, 20}
print(s1.difference(s2))
# {50, 60}
print(s2.difference(s1))


#change
