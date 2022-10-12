cook_book = {}

with open('cook_book.txt', 'r', encoding = 'utf8') as file:
    for line in file:
        dishes_name = line.strip()
        cook_book[dishes_name] = []
        ingredients_count = file.readline()
        for i in range(int(ingredients_count)):
            ing = file.readline()
            name, amount, ms = ing.split(' | ')
            measurement = ms.strip()
            ingredient = {'ingredient_name' : name,'quantity' : amount,'measure' : measurement}
            cook_book[dishes_name].append(ingredient)
        file.readline()
print(cook_book)


person_count = 3
dishes = ['Омлет', 'Фахитос']

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            new_ingredient_shop_list = ingredient
            product = new_ingredient_shop_list['ingredient_name']
            weight = new_ingredient_shop_list['measure']
            amount = int(new_ingredient_shop_list['quantity']) * person_count
            weight_amount = {'measure' : weight, 'quantity' : amount}
            if product not in shop_list:
                shop_list[product] = weight_amount
            else: 
                shop_list[product]['quantity'] = shop_list[product]['quantity'] + amount
         
    print(shop_list)
            
get_shop_list_by_dishes(dishes, person_count, cook_book)
