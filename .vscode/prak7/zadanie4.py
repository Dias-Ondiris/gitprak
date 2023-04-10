
vacation_schedule = {} 
def add_otpusk():
    n = int(input()) 
    for i in range(n):
        name, day, month = input().split()
        if name not in vacation_schedule:
            vacation_schedule[name] = []
        vacation_schedule[name].append(month)
add_otpusk()
query_month = input()
def search(query_month):
    result = []
    for name, months in vacation_schedule.items():
        if query_month in months:
            result.append(name)
    return result
result=search(query_month)
if result:
    print(*result)
else:
    print("Никто не идет в отпуск в указанный месяц")