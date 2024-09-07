'''version 1'''

a = str(input())
b = str(input())


count_list= []
for j in range(len(a)):
    check = 0
    count = 0
    for i in range(len(a)):
        a_index = i

        if a[a_index] == b[check]:
            check += 1
        else:
            check = 0
            if a[a_index] == b[check]:
                check += 1
        if check == len(b):
            count += 1
            check = 0
    count_list.append(count)
    a = a[1:]

print(max(count_list))
