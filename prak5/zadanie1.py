class section:
    def __init__(self,fname,kurs):
        self.name=fname
        self.kurs=kurs
def sort(a):
    for i in a:
        for j in a:
            if i.kurs<j.kurs:
                tempk=i.kurs
                tempn=i.name
                i.kurs=j.kurs
                j.kurs=tempk
                i.name=j.name
                j.name=tempn
    return a
dias=[]
n=int(input("n:"))
for j in range(n):
    name=input("fname:")
    k=int(input("class:"))
    dias.append(section(name,k))
dias=sort(dias)
for i in dias:
    print(f"{i.name}\t{i.kurs}")