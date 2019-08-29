#bottleneck problem

n = int(input("enter number of bottles : ")) #no need for it though
r = input("enter radii : ")
list1=r.split()
#print(list1)
list2=sorted(list1)
#print(list2)

count = 0
d = {}

d = {x:list2.count(x) for x in list2} #made a dictionary from list items and their counts

#print(d)
#print(max(d.values()),"--------------- answer --- ",max(d.keys()))
#a = max(d.keys())
b = max(d.values())
print(" answer is : ",b)
#for key in list2:
#d={key:list.count(key)}
