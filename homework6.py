"""just a dockstring"""

# Transform string "Robin Singh" into list
stroka1 = "Robin Singh"
spisok1 = stroka1.split()
print(spisok1)

# Transform string "I love arrays they are my favorite" into list
stroka2 = "I love arrays they are my favorite"
spisok2 = stroka2.split()
print(spisok2)

# 3
Name = ["Ivan", "Ivanou"]
Horad = "Minsk"
Kraina = "Belarus"
stroka3 = " ".join(Name)
print(f"Привет, {stroka3}! Добро пожаловать в {Horad} {Kraina}")

# Transform list into the string
spisok4 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
stroka4 = " ".join(spisok4)
print(stroka4)

# Create list with 10 elements, input new value into the 3rd position, delete 6th element
spisok5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
spisok5.insert(2, "hoba!")
del spisok5 [6]
print(spisok5)
