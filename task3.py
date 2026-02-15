# Task 3: Interactive Visualizations with Plotly

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

import plotly.express as px
import plotly.data as pldata
df = pldata.wind(return_type='pandas')


# printing the first 10 rows
print(df.head(10))

# checking the unique values in the 'strength' column, earlier it gave some error on mismatch int and float
print(df['strength'].unique())


# because there are some unique numbers wit + sign, we need to get rid of them.
df['strength'] = df['strength'].str.strip('+')

#now the colums contains either 1 or 2 numbers, so we need to split it to two columns, and one of them with show NaN for the second columns, as there is only one number. So, we need to do splitting for those two numbers and assign them to low and high columns. 
df[['low','high']] = df['strength'].str.split('-', expand=True)

# now each column contains only one number, but they are still in string format, so we need to convert them to float.
df['low'] = df['low'].astype(float)
df['high'] = df['high'].astype(float)

# there are some NaN values in the high column, so we need to fill them with the values from the low column, because they are the same.
df['high'] = df['high'].fillna(df['low'])

# now we can calculate the strength column as the average of low and high columns, and we can use it for our scatter plot.
df['strength'] = (df['low'] + df['high']) / 2

    
# Scatter Plot wiith color in directin as it is a wind data, we can see the direction of the wind with different colors, and we can also see the strength of the wind with the size of the points, and the frequency of the wind with the y-axis.
fig = px.scatter(df, x='strength', y='frequency', color='direction',
                 title="Wind Data, Strength vs. Frequency")

# lastly, we can show the plot and save it as an html file, so we can open it in the browser and interact with it.
fig.write_html("wind.html", auto_open=True)