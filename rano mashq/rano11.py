from random import*
a=randint(1,3)
print(a)
m=["olma","anor","orik"]
k=len(m)
if a>k:
    print("meva yoq")
else:
    m.insert(a,"kivi")
print(m)

