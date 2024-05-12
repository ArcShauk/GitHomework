# 1. Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
# Через Fstring:
slash = "/"
print(f"www.my_site.com{slash}about")

#Через Replace:
site = "www.my_site.com#about"
print(site.replace("#", "/"))

# 2. Напишите программу, которая добавляет ‘ing’ к словам
ing = "ing"
print(f"Ty{ing} nie{ing} chakaj{ing}, siurpryzau{ing} nia{ing} budzie{ing}.")

# 3. В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
#Через распаковку
name = "Ivan"
surname = "Ivanou"
name, surname = surname, name
print(name, surname)

#Через дополнительную переменную
name2 = "Ivan"
surname2 = "Ivanou"
add2 = name2
name2 = surname2
surname2 = add2
print(name2, surname2)

#. 4. Напишите программу которая удаляет пробел в начале, в конце строки
probely_uhodi = " ъуъ "
print(probely_uhodi.strip())

# 5. Имена собственные всегда начинаются с заглавной буквы, за которой следуют строчные буквы.
# Исправьте данное имя собственное так, чтобы оно соответствовало этому утверждению. "pARiS" >> "Paris"
city = "pARiS"
print(city.capitalize())