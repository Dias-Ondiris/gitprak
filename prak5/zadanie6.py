import random 
def ticket_random():
    ticket=set()
    while len(ticket)<6:
        ticket.add(random.randint(1,49))
    return ticket
def issort(a):
    if a==sorted(a):
        return True
    else:
        return False
dsa=ticket_random()
print(dsa)
print(issort(dsa))

