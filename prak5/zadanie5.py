import random 
def ticket_random():
    ticket=set()
    while len(ticket)<6:
        ticket.add(random.randint(1,49))
    return sorted(ticket)
print(ticket_random())