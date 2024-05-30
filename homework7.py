"""just a dockstring"""

# Zadanie1
number = "2310"
enter_number = 0
count_cows = 0
count_bulls = 0
invalid_value = False
while enter_number != number:
    enter_number = input("Enter number here: ")
    for i in enter_number:
        resul_count = enter_number.count(i)
        if resul_count >1:
            print("Number invalid, please, enter number with unique numbers")
            invalid_value = True
            break
    if invalid_value:
        continue
    for o in number:
        current_count_cows = enter_number.count(o)
        if current_count_cows == 1:
            count_cows += 1
    for u in range(4):
        if number[u] == enter_number[u]:
            count_bulls += 1
    print("Bulls = ", count_bulls )
    print("Cows = ", count_cows - count_bulls)
    print()
    count_cows = 0
    count_bulls = 0
else: print("You won!")


#zadanie2 ne vypolnil, ne ponimaju kak



# #zadanie3
a = 2, 3, 4, 5, 6, 7, 8
b = 0
stat1 = 2
stat2 = 3
stat3 = 6
stat4 = 8
for i in a:
    if i == stat1:
        b +=1
    if i == stat2:
        b += 1
    if i == stat3:
            b += 1
    if i == stat4:
        b += 1
c = int((len(a)))
print(c - b)