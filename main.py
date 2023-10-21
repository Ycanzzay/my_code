shopping_list = ["яблоко", "молоко", "хлеб", "яйца", "сок"]
s = 0
while s<len(shopping_list):
    print(shopping_list[s])
    s+=1
shopping_list.remove("молоко")
print(shopping_list)
shopping_list.remove("яблоко")
shopping_list.insert(0,"банан")
print(shopping_list)
for shopping_list in shopping_list:
    print(shopping_list)

