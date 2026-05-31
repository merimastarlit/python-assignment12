# Task 2: Cumulative
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connecting to the database
conn = sqlite3.connect("./db/lesson.db")
cursor = conn.cursor()

# qeuring the total price for each order by joining the orders, line_items, and products tables, and then grouping by order_id to get the total price for each order, and ordering by order_id to get the cumulative total price in the correct order.
query = """
SELECT orders.order_id, SUM(products.price * line_items.quantity) AS total_price
FROM orders

JOIN line_items ON orders.order_id = line_items.order_id
JOIN products ON line_items.product_id = products.product_id
GROUP BY orders.order_id
ORDER BY orders.order_id



"""

# Execute and fetch results
cursor.execute(query)
task2 = cursor.fetchall()
print(task2)

conn.close()

# creating a dataframe from the results of the query, and then calculating the cumulative total price for each order by using the cumsum() method, which calculates the cumulative sum of the total_price column, and then plotting the cumulative total price by order_id using a line plot.
task2_df = pd.DataFrame(task2, columns=["order_id", "total_price"])

def cumulative(row):
   totals_above = task2_df['total_price'][0:row.name+1]
   return totals_above.sum()

task2_df['cumulative'] = task2_df['total_price'].cumsum()

# Line Plot
task2_df.plot(x="order_id", y="cumulative", kind="line", color="orange", title="Cumulative Total Price by Order")
plt.show()

