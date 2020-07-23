from collections import Counter
#c=[i for i in range(5)[:3]]
#print(c)
'''for i in range(6) [:4]:
    print(i)
'''
#dictionary can not convert in list but can be converted in list of list
s=[]
c={'e':3,'w':4,'d':3,'q':2,'z':4}
print(c['e'])
for i in c:
    s.append([i,c[i]])# if key is using inside for loop dont use double quotes else use doublequotes outside loop
print(s)
print(sorted(s))
c=[i[1] for i in s ]
print(c)
print(Counter(c))
