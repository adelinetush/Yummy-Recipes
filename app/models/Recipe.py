class Recipe:
    def __init__(self, name, description, ingredients):
        self.name = name
        self.description = description
        self.ingredients = []
        self.ingredients.append(ingredients)

    def set_name(self, name):
        self.name = name

    def set_description(self, description):
        self.description = description

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def remove_ingredient(self, ingredient):
        self.ingredients.remove(ingredient)