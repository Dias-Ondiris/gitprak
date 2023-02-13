m=[]
while(True):
    n=int(input())
    if n==0:
        break
    m.append(n)
m.sort(reverse=True)
print("result:")
for i in m:
    print(i)