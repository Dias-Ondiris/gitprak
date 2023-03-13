n = int(input()) 

phone_book = {}  

for i in range(n):
    phone, name = input().split()  
    phone_book[name] = phone 

query = input()  
if query in phone_book :
    print(phone_book[query]) 
else:
    print('Телефонкітапшасында жоқ')  
print('Қосу?иа/жоқ')
jauap=input()
if jauap=='иа':
    phone_book[query]=input("номер:")
    
for name, phone in phone_book.items():
    print(name, phone)

