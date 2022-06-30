
from pprint import pprint


file_name = "C:/Users/ysbondarenko/Desktop/Work/netology/homework/8_ООП_2/OOP_2.txt"


def recipe_list_processing(file_name: str) -> dict:
    cook_book = {}
    index_line = 0
    with open(file_name, "r", encoding="utf-8") as file:
        count_line = sum(1 for line in file)

    with open(file_name, "r", encoding="utf-8") as file_1:
        list_ingredient = []

        for line in file_1:

            str_item = line[:len(line) - 1]

            if (line.find("|") + 1) != 0:
                ingredient = {}
                ingredient_name = line.split("|")[0]
                ingredient['ingredient_name'] = ingredient_name[:len(
                    ingredient_name) - 1]
                ingredient['quantity'] = line.split("|")[1].replace(" ", "")
                ingredient['measure'] = line.split(
                    "|")[2].replace("\n", "").replace(" ", "")
                list_ingredient.append(ingredient)

            else:

                if str_item != '' and not str_item.isdigit() and (str_item.find("|") + 1) == 0:
                    dish = str_item

            index_line += 1

            if str_item == '' or index_line == count_line:
                cook_book[dish] = list_ingredient
                del list_ingredient
                list_ingredient = []

    return cook_book


def get_shop_list_by_dishes(dishes, person_count) -> dict:

    cook_book = recipe_list_processing(file_name)
    grocery_list = {}

    for item_dish in dishes:
        if item_dish in cook_book:
            for list_item in cook_book.get(item_dish):
                if not list_item.get('ingredient_name') in grocery_list:
                    quantity_ingredients = {}
                    quantity_ingredients['measure'] = list_item.get('measure')
                    quantity_ingredients['quantity'] = int(list_item.get(
                        'quantity')) * person_count
                    grocery_list[list_item.get(
                        'ingredient_name')] = quantity_ingredients
                else:
                    quantity_ingredients_new = {}
                    quantity_ingredients_new = grocery_list[list_item.get(
                        'ingredient_name')]
                    quantity_ingredients_new['quantity'] = quantity_ingredients_new['quantity'] + int(list_item.get(
                        'quantity')) * person_count
                    grocery_list[list_item.get(
                        'ingredient_name')] = quantity_ingredients_new
        else:
            print(f'Блюда "{item_dish}" нет в списке.')
    pprint(grocery_list)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 2)
