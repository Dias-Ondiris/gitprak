
phone_book = {}  
def add_contact():
    n = int(input()) 
    for i in range(n):
        phone, name = input().split()  
        phone_book[name] = phone 
def search(query):
    if query in phone_book :
        print(phone_book[query]) 
    else:
        print('Телефон кітапшасында жоқ')  
        print('Қосу?иа/жоқ')
        query = input()  
        jauap=input()
        if jauap=='иа':
            phone_book[query]=input("номер:")
add_contact()
query=input()
search(query)
for name, phone in phone_book.items():
    print(name, phone)

