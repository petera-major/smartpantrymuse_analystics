# SmartPantryMuse Recipe App Data Analysis  

## Project Overview
This project analyzes **real data from my own recipe app**.  
The goal was to uncover user diet trends, popular ingredients, recipe choices, and compare **cooking at home vs eating out costs**.  

Instead of using a random dataset, I pulled from my **Firestore app data**, cleaned it into CSVs, and built an analytics pipeline in **Python + pandas**.  

---

## Data Sources
- `users.join.csv` → app users & their dietary goals  
- `ingredients_prices.csv` → average ingredient costs (home cooking)  
- `recipes.csv` → recipe–ingredient breakdown with quantities  
- `restaurant_prices.csv` → estimated restaurant prices for the same meals  
- Results CSVs (ready for Tableau/Excel):
  - [`results/top_diets.csv`](results/top_diets.csv)  
  - [`results/top_ingredients.csv`](results/top_ingredients.csv)  
  - [`results/top_recipes.csv`](results/top_recipes.csv)  

---

##  Key Insights
### 1. User Trends
- **Top 5 diets chosen by users**:  
  - Low FODMAP  
  - MaxCalories = 900  
  - High-protein  
  - Ketogenic  
-  *Shows health-conscious user base.*

### 2. Ingredient Trends
- **Most used ingredients**: Avocado, Chicken, Rice.  
-  *Staple, versatile, cost-effective items.*

### 3. Recipe Trends
- **Top 3 recipes**: Guacamole, Hummus, Pesto.  
-  *Plant-forward and affordable meal prep.*

### 4. Cost Savings
- Cooking at home saves **~$1.50–$2.20 per serving** compared to eating out.  
- Biggest saving: **Veggie Fried Rice (~$2.20/serving)**.  
- Lowest saving: **Coleslaw (~$0.30/serving)**.  

---

## Visuals
Examples of analysis & charts created with Python (matplotlib/seaborn) and exportable to Tableau:  
- Bar chart: Top 5 Diet Goals (descending)  
- Bar chart: Home vs Restaurant Costs per Recipe  
- Bar chart: Savings per Serving  

#DashBoard and Individual Charts Results
![Results Dashboard](visuals/dashboard.png)

---

## Recommendations
- Highlight **cost savings** directly in the app to improve user engagement.  
- Encourage recipes with **high savings per serving** (fried rice, stir fry).  
- Use Tableau/Excel dashboards for easy presentation of trends.  
- Future step: track ingredient prices over time for **predictive savings analysis**.  

---

## Tech Stack
- **Python** → data cleaning, analysis, exports  
- **pandas** → data wrangling & SQL-style queries  
- **matplotlib** → visualization  
- **Tableau & Excel** → dashboard-ready reports  
- **Firestore → CSV export** → real app data  

---

## Impact
- Demonstrates end-to-end data analysis with **real app data**.  
- Shows how data can provide **business impact** (cost savings + user trends).  
- Perfect example of blending **technical skills** (Python, SQL-like analysis) with **business storytelling** (insights, recommendations).  

---

*This project highlights my ability to take raw app data → clean & analyze it → deliver insights that matter.*  
