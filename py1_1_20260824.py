# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 10:41:43 2026

@author: chihh
"""

# %% 1. Basic variables
name = "Hank"
age = 27
scores = [88, 92, 95, 81, 90]

student = {
    "name": name,
    "age": age,
    "scores": scores
}

average_score = sum(scores) / len(scores)

print("Student:", student)
print("Average:", average_score)


# %% 2. NumPy — check Variable Explorer
import numpy as np

np.random.seed(42)

matrix = np.random.randint(1, 100, size=(5, 4))

column_means = matrix.mean(axis=0)
row_means = matrix.mean(axis=1)

print("\nMatrix:")
print(matrix)

print("\nColumn means:")
print(column_means)


# %% 3. pandas — double-click df in Variable Explorer
import pandas as pd

df = pd.DataFrame({
    "product": ["A", "B", "C", "D", "E", "F"],
    "category": ["X", "X", "Y", "Y", "X", "Y"],
    "sales": [120, 180, 90, 240, 150, 210],
    "cost": [80, 100, 70, 130, 90, 120]
})

df["profit"] = df["sales"] - df["cost"]
df["margin"] = df["profit"] / df["sales"]

summary = (
    df.groupby("category")
      .agg(
          total_sales=("sales", "sum"),
          avg_profit=("profit", "mean"),
          avg_margin=("margin", "mean")
      )
)

print("\nDataFrame:")
print(df)

print("\nSummary:")
print(summary)


# %% 4. Functions — useful for debugger
def calculate_discount(price, discount_rate):
    discount = price * discount_rate
    final_price = price - discount
    return final_price


prices = [100, 250, 80, 500]

discounted_prices = []

for price in prices:
    new_price = calculate_discount(price, 0.2)
    discounted_prices.append(new_price)

print("\nDiscounted prices:")
print(discounted_prices)


# %% 5. Matplotlib — check Spyder Plots pane
import matplotlib.pyplot as plt

plt.figure()

plt.bar(df["product"], df["profit"])

plt.title("Profit by Product")
plt.xlabel("Product")
plt.ylabel("Profit")

plt.show()


# %% 6. Scatter plot
plt.figure()

plt.scatter(df["sales"], df["profit"])

plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")

plt.show()


# %% 7. Random simulation
random_numbers = np.random.normal(
    loc=100,
    scale=15,
    size=1000
)

simulation_mean = random_numbers.mean()
simulation_std = random_numbers.std()

print("\nSimulation mean:", simulation_mean)
print("Simulation std:", simulation_std)

plt.figure()

plt.hist(random_numbers, bins=30)

plt.title("Random Simulation")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.show()


# %% 8. Exception handling
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = np.nan

    return result


normal_result = safe_divide(10, 2)
error_result = safe_divide(10, 0)

print("\nNormal result:", normal_result)
print("Divide by zero result:", error_result)


# %% 9. Class — preview of your 95-896 OOP
class Product:
    def __init__(self, name, price, cost):
        self.name = name
        self.price = price
        self.cost = cost

    def profit(self):
        return self.price - self.cost

    def margin(self):
        return self.profit() / self.price


product_a = Product("Laptop", 1200, 850)
product_b = Product("Monitor", 400, 260)

products = [product_a, product_b]

for product in products:
    print(
        product.name,
        "Profit:",
        product.profit(),
        "Margin:",
        round(product.margin(), 3)
    )


# %% 10. Final objects to inspect in Variable Explorer

final_results = {
    "student_average": average_score,
    "matrix": matrix,
    "sales_dataframe": df,
    "category_summary": summary,
    "discounted_prices": discounted_prices,
    "simulation_mean": simulation_mean
}

print("\nDone! Now explore variables inside Spyder.")