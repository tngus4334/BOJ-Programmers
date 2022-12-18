
endday_List = [31,28,31,30,31,30,31,31,30,31,30,31]
wok_list = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
month, day = map(int,input().split())

day_index = 0
for endday in range(month-1):
    day_index = day_index + endday_List[endday]
    
day_index = (day_index + day) % 7

print(wok_list[day_index-1])