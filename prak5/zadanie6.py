import random 
def ticket_random():
    ticket=set()
    while len(ticket)<6:
        ticket.add(random.randint(1,49))
    return ticket
def issort(a):
    b=a
    for i in b:
        for j in b:
            if i<j:
                t=i
                i=j
                j=t
    if a==b:
        return True
    else:
        return False
dsa=ticket_random()
print(dsa)
print(issort(dsa))

