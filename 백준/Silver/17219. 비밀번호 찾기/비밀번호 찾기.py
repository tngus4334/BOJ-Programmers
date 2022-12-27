n, m = map(int,input().split())

site_password_dic = {}
look_for_site_name = []
for _ in range(n):
    site, password = map(str, input().split())
    site_password_dic[site] = password

for _ in range(m):
    look_for_site_name.append(input())
for i in range(m):
    print(site_password_dic[look_for_site_name[i]])