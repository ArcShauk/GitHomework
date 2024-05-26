"""just a dockstring"""

# Transform string "Robin Singh" into list
STROKA1 = "Robin Singh"
SPISOK1 = STROKA1.split()
print(SPISOK1)

# Transform string "I love arrays they are my favorite" into list
STROKA2 = "I love arrays they are my favorite"
SPISOK2 = STROKA2.split()
print(SPISOK2)

# Task 3
NAME = ["Ivan", "Ivanou"]
HORAD = "Minsk"
KRAINA = "Belarus"
STROKA3 = " ".join(NAME)
print(f"Привет, {STROKA3}! Добро пожаловать в {HORAD} {KRAINA}")

# Transform list into the string
SPISOK4 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
STROKA4 = " ".join(SPISOK4)
print(STROKA4)

# Create list with 10 el., input new value to 3rd pos., del 6th el
SPISOK5 = [1, 2, 3, 4, 5, 6, 7, "treba", 9, 10]
SPISOK5.insert(2, "hoba!")
del SPISOK5[6]
print(SPISOK5)
