import pandas as pd
import matplotlib.pyplot as plt

#Load recipe breakdown
recipes = pd.read_csv("recipes.csv")
#Load ingredient cost
ingredients = pd.read_csv("ingredients_prices.csv")
#Load resturant prices
resturant = pd.read_csv("restaurant_prices.csv")

print("Recipes:")
print(recipes.head())

print("\nRestaurant Prices:")
print(resturant.head())

#merge recipes with ingredient prices so each meal has a price
merged =recipes.merge(ingredients, on=["ingredient", "unit"], how="left")

#calculate line cost per ingredient
merged["line_cost"] = merged["quantity"] * merged["avg_price_per_unit"]

#Total cost per recipe
home_totals = merged.groupby("recipe", as_index=False)["line_cost"].sum()
home_totals.rename(columns={"line_cost": "home_total_cost"}, inplace=True)

print(home_totals)

comparison = home_totals.merge(resturant, on="recipe", how="left")

comparison["home_cost_per_serving"] = (comparison["home_total_cost"] / comparison["servings"]).round(2)

#Join with resturant preices to compare to eating out
comparison = home_totals.merge(resturant, on="recipe", how="left")
comparison["home_cost_per_serving"] = (comparison["home_total_cost"] / comparison["servings"]).round(2)
comparison["savings_per_serving"] = (
comparison["out_price_per_serving_USD"] - comparison["home_cost_per_serving"]).round(2)

print(comparison)

plt.figure(figsize=(8,5))
plt.bar(comparison["recipe"], comparison["savings_per_serving"], color="green")
plt.xticks(rotation=45, ha="right")
plt.ylabel("Savings per Serving (USD)")
plt.title("Cooking at Home vs Eating Out")
plt.show()
