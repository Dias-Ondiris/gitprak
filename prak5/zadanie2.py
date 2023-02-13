class section:
    def __init__(self,fname,b1,b2,b3):
        self.name=fname
        self.b1=b1
        self.b2=b2
        self.b3=b3
def select(a,name):
    for i in a:
        if i.name==name:
            print(f"{i.name}\t{i.b1}\t{i.b2}\t{i.b3}")
            return i
dias=[]
n=int(input("n:"))
for j in range(n):
    dias.append(section(input("fname:"),int(input("baga 1:")),int(input("baga 2:")),int(input("baga 3:"))))
d=select(dias,input("student name:"))
