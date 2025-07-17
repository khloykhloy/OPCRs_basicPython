fruits = ["pomme", "banane", "orange"]
fruits.append("kiwi")
fruits.remove("orange")
fruits[1] = "ananas"
print("La liste des fruits contient : " + str(len(fruits)) + "éléments.")
fruits.sort()
print(fruits)