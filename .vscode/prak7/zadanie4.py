n = int(input()) 
vacation_schedule = {} 

for i in range(n):
    name, day, month = input().split()
    if name not in vacation_schedule:
        vacation_schedule[name] = []
    vacation_schedule[name].append(month)

query_month = input()

result = []
for name, months in vacation_schedule.items():
    if query_month in months:
        result.append(name)

if result:
    print(*result)
else:
    print("Никто не идет в отпуск в указанный месяц")