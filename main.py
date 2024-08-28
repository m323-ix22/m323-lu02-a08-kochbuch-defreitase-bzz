"""xxx"""

import json


def adjust_recipe(recepy, amount_people):
    adjusted_ingredients = {}
    original_servings = recepy['servings']
    factor = amount_people / original_servings

    for ingredient, amount in recepy['ingredients'].items():
        adjusted_ingredients[ingredient] = amount * factor

    adjusted_recipe = {
        'title': recepy['title'],
        'ingredients': adjusted_ingredients,
        'servings': amount_people
    }
    return adjusted_recipe


def load_recipe(json_string):
    return json.loads(json_string)


if __name__ == '__main__':
    # Beispiel für die Datenstruktur eines Rezepts
    recipe_json = '{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, ' \
                  '"Minced Meat": 500}, "servings": 4}'
    recipe = load_recipe(recipe_json)
    adjust_recipe(recipe, 3)
