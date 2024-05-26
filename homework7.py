"""just a dockstring"""

# Zadanie1
# 5948
# 4 korovy i 4 byka
W = 0
while W <= 5948:
    W += 1
print(W, "= SUCCESS!")

# zadanie3
a = 2, 3, 4, 5, 6, 7, 8
B = 0
STAT1 = 2
STAT2 = 3
STAT3 = 6
STAT4 = 8
for i in a:
    if i == STAT1:
        B += 1
    if i == STAT2:
        B += 1
    if i == STAT3:
        B += 1
    if i == STAT4:
        B += 1
C = int((len(a)))
print(C - B)
