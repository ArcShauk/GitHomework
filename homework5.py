"""just a dockstring"""

# Replace symbols “#” to the “/” in the line 'www.my_site.com#about

# via Fstring
SLASH = "/"
print(f"www.my_site.com{SLASH}about")

# Via Replace:
SITE = "www.my_site.com#about"
print(SITE.replace("#", "/"))

# Write programmthat adds ‘ing’ to the words
A = "ing"
print(f"Ty{A} nie{A} chakaj{A}, siurpryzau{A} nia{A} budzie{A}.")

# in the line “Ivanou Ivan” replase => "Ivan Ivanou"

# Via unpacking
NAME = "Ivan"
SURNAME = "Ivanou"
NAME, SURNAME = SURNAME, NAME
print(NAME, SURNAME)

# Write programm that deletes space on the start, on the end of the line
PROBELY_UHODI = " ъуъ "
print(PROBELY_UHODI.strip())

# Change "pARiS" >> "Paris"""
CITY = "pARiS"
print(CITY.capitalize())
