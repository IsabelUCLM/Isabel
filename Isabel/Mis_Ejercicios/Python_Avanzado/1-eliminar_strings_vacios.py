# 17/04/2023
lista = ["a", "b", "c", "", ""]
no_strings = []

for string in lista:
    if string != "" and string != " " and string != "c":
        no_strings.append(string)

print(no_strings)




