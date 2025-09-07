import pandas as pd

users = pd.read_csv("users.join.csv")
top_diets = users['diet'].value_counts().head(4)
top_diets = top_diets.reset_index()
top_diets.columns = ["diet", "count"]
top_diets.to_csv("top_diets.csv", index=False)

ingredient = pd.read_csv("ingredients_prices.csv")
top_ingredient = ingredient['ingredient'].value_counts().head(3)
top_ingredient = top_ingredient.reset_index()
top_ingredient.columns = ["ingredient", "count"]
top_ingredient.to_csv("top_ingredient.csv", index=False)

recipes = pd.read_csv("recipes.csv")
top_recipe = recipes['recipe'].value_counts().head(3)
top_recipe = top_recipe.reset_index()
top_recipe.columns = ["recipe", "count"]
top_recipe.to_csv("top_recipes.csv", index=False)

print("exports complete")
